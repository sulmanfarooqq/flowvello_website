(function(){
   var GEMINI_API_KEY = "AIzaSyAIUJJtjM9jFVXdfcz5Bh03LRhFTUaJY1k";
   var SYSTEM_PROMPT = "You are the Flow Vello AI Assistant. You are a brutally honest, highly technical Sales Development Rep for an enterprise digital agency. Your job is to qualify leads and convince them to book a consultation. You ask about their bottlenecks (inefficient workflows, outdated software, poor conversion). If they want to book a call, reply exactly with the string: [BOOK_CALL_TRIGGER]";

   var conversationHistory = [
      { role: "user", parts: [{ text: SYSTEM_PROMPT }] },
      { role: "model", parts: [{ text: "Understood. I will act as the Flow Vello AI Assistant and qualify leads." }] }
   ];
   
   function el(tag, cls, html){
      var e = document.createElement(tag);
      if(cls) e.className = cls;
      if(html) e.innerHTML = html;
      return e;
   }

   function buildWidget(){
      var trigger = el('button','fv-chatbot-trigger');
      trigger.innerHTML = '<i class="fal fa-comment-alt-lines icon-chat"></i><i class="fal fa-times icon-close"></i>';
      trigger.setAttribute('aria-label','Open AI Assistant');
      document.body.appendChild(trigger);

      var win = el('div','fv-chatbot-window');
      win.innerHTML =
         '<div class="fv-chatbot-hero">'+
            '<h2>AI. <span>Chat.</span> Experience.</h2>'+
            '<p>How can I help you today?</p>'+
         '</div>'+
         '<div class="fv-chatbot-messages"></div>'+
         '<div class="fv-chatbot-input-container">'+
            '<div class="fv-chatbot-input-wrapper">'+
                '<button class="fv-chatbot-plus-btn"><i class="fal fa-plus"></i></button>'+
                '<input type="text" placeholder="Ask something with AI" id="fv-chat-input-field" />'+
                '<button class="fv-chatbot-send-btn" id="fv-chat-send-btn"><i class="fal fa-paper-plane"></i></button>'+
            '</div>'+
         '</div>';
      document.body.appendChild(win);

      return { 
          trigger: trigger, 
          win: win, 
          messages: win.querySelector('.fv-chatbot-messages'), 
          inputField: win.querySelector('#fv-chat-input-field'),
          sendBtn: win.querySelector('#fv-chat-send-btn')
      };
   }

   function addMessage(container, type, html){
      var msg = el('div','fv-chat-msg '+type, html);
      container.appendChild(msg);
      container.scrollTop = container.scrollHeight;
      return msg;
   }

   function showTyping(container){
      var t = el('div','fv-chat-typing','<span></span><span></span><span></span>');
      container.appendChild(t);
      container.scrollTop = container.scrollHeight;
      return t;
   }

   function injectCalendly(container){
      var calContainer = el('div', 'fv-chat-calendly-container');
      calContainer.innerHTML = '<div class="calendly-inline-widget" data-url="https://calendly.com/itproto/30min?hide_event_type_details=1&hide_gdpr_banner=1" style="min-width:100%;height:500px; border-radius: 8px;"></div>';
      container.appendChild(calContainer);
      container.scrollTop = container.scrollHeight;

      if(!document.getElementById('calendly-script')){
          var script = document.createElement('script');
          script.id = 'calendly-script';
          script.src = 'https://assets.calendly.com/assets/external/widget.js';
          script.async = true;
          document.body.appendChild(script);
      } else {
          if(window.Calendly){
              window.Calendly.initInlineWidget({
                  url: 'https://calendly.com/itproto/30min?hide_event_type_details=1&hide_gdpr_banner=1',
                  parentElement: calContainer.querySelector('.calendly-inline-widget')
              });
          }
      }
   }

   async function sendMessageToGemini(userText, w) {
      if(GEMINI_API_KEY === "YOUR_GEMINI_API_KEY_HERE") {
          addMessage(w.messages, 'bot', 'Error: Gemini API key is missing. Please add it to js/chatbot.js on line 3.');
          return;
      }

      var typing = showTyping(w.messages);

      conversationHistory.push({ role: "user", parts: [{ text: userText }] });

      try {
          const response = await fetch("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=" + GEMINI_API_KEY, {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ contents: conversationHistory })
          });

          const data = await response.json();
          typing.remove();

          if(data.error) {
              addMessage(w.messages, 'bot', 'API Error: ' + data.error.message);
              return;
          }

          var botReply = data.candidates[0].content.parts[0].text;
          conversationHistory.push({ role: "model", parts: [{ text: botReply }] });

          if(botReply.includes("[BOOK_CALL_TRIGGER]")) {
              var cleanReply = botReply.replace("[BOOK_CALL_TRIGGER]", "").trim();
              if(cleanReply) addMessage(w.messages, 'bot', cleanReply.replace(/\\n/g, '<br>'));
              addMessage(w.messages, 'bot', 'Please select a time below that works for your team:');
              injectCalendly(w.messages);
          } else {
              addMessage(w.messages, 'bot', botReply.replace(/\\n/g, '<br>'));
          }

      } catch (error) {
          typing.remove();
          addMessage(w.messages, 'bot', 'Network error. Could not reach AI server.');
      }
   }

   function init(){
      var w = buildWidget();
      var isOpen = false;
      var hasInitialized = false;

      w.trigger.addEventListener('click',function(){
         isOpen = !isOpen;
         w.trigger.classList.toggle('active',isOpen);
         w.win.classList.toggle('open',isOpen);
         
         if(isOpen && !hasInitialized){
            hasInitialized = true;
            addMessage(w.messages, 'bot', 'Hi, I am the Flow Vello AI. What brings you here today?');
         }
      });

      function handleSend() {
          var val = w.inputField.value.trim();
          if(!val) return;
          addMessage(w.messages, 'user', val);
          w.inputField.value = '';
          sendMessageToGemini(val, w);
      }

      w.sendBtn.addEventListener('click', handleSend);
      w.inputField.addEventListener('keydown', function(e){
          if(e.key === 'Enter') handleSend();
      });
   }

   if(document.readyState==='loading'){
      document.addEventListener('DOMContentLoaded',init);
   } else {
      init();
   }
})();
