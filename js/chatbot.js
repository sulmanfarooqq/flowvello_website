(function(){
   var GEMINI_API_KEY = "AIzaSyAIUJJtjM9jFVXdfcz5Bh03LRhFTUaJY1k";
   var SYSTEM_PROMPT = `You are the Flow Vello AI Assistant. You are a brutally honest, highly technical Sales Development Rep for an enterprise digital agency. Keep all responses EXTREMELY SHORT (1-2 sentences max). Be punchy, professional, and authoritative. Your job is to qualify leads and convince them to book a consultation. If they want to book a call, reply exactly with the string: [BOOK_CALL_TRIGGER]

AGENCY CONTEXT:
Flow Vello (also known as Proto IT Consultants) is an elite AI, automation, and software development agency.
Services:
1. Workflow Automation (cutting manual work, API syncs, complex CRM/ERP integrations)
2. AI Agents & Customer Support (autonomous agents trained on business data)
3. Executive Dashboards (custom real-time metrics across all systems)
4. Software Development (Web Apps, Mobile Apps, scalable cloud infrastructure)
5. Digital Operations (HubSpot, Monday.com, Pipedrive, Odoo setups)

Industries served: Real Estate, B2B SaaS, E-Commerce, Legal, Healthcare, Financial, and more.
Core Value Proposition: We don't do plug-and-play gimmicks. We build autonomous AI agents, decouple frontends, deploy scalable cloud databases, and build unified systems that replace legacy tools and cut manual data entry so enterprise companies can scale revenue.

If someone asks what we do, give a very brief 1-sentence punchy summary of our relevant service and ask what their current bottleneck is. DO NOT list all services. DO NOT write paragraphs. Always push them toward booking a call if they have a real problem.`;

   var conversationHistory = [
      { role: "user", parts: [{ text: SYSTEM_PROMPT }] },
      { role: "model", parts: [{ text: "Understood. I will act as the Flow Vello AI Assistant, keep responses brutally short, and qualify leads." }] }
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
         '<div class="fv-chat-quick-actions">'+
            '<button class="fv-chat-quick-btn" data-query="I want to book a meeting">🗓️ Book Meeting</button>'+
            '<button class="fv-chat-quick-btn" data-query="What services do you offer?">⚙️ Services</button>'+
            '<button class="fv-chat-quick-btn" data-query="How much does it cost?">💰 Pricing</button>'+
         '</div>'+
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
          quickActions: win.querySelectorAll('.fv-chat-quick-btn'),
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
   
   function addWordByWordMessage(container, text) {
       var msg = el('div', 'fv-chat-msg bot', '');
       container.appendChild(msg);
       
       var words = text.split(' ');
       words.forEach(function(word, index) {
           var span = document.createElement('span');
           span.className = 'fv-word-reveal';
           span.style.animationDelay = (index * 0.03) + 's';
           span.innerHTML = word + '&nbsp;';
           msg.appendChild(span);
       });
       
       container.scrollTop = container.scrollHeight;
       return msg;
   }

   function showTyping(container){
      var t = el('div','fv-chat-typing-shimmer','System Architect AI is thinking...');
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
              if(cleanReply) addWordByWordMessage(w.messages, cleanReply);
              setTimeout(function() {
                  addWordByWordMessage(w.messages, "Please select a time below that works for your team:");
                  injectCalendly(w.messages);
              }, (cleanReply.split(' ').length * 30) + 400); // Wait for first sentence to finish animating
          } else {
              addWordByWordMessage(w.messages, botReply);
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
            addWordByWordMessage(w.messages, 'Hi, I am the Flow Vello AI. What brings you here today?');
         }
      });

      function handleSend(val) {
          var text = val || w.inputField.value.trim();
          if(!text) return;
          addMessage(w.messages, 'user', text);
          if(!val) w.inputField.value = ''; // Only clear if it came from input field
          sendMessageToGemini(text, w);
      }

      w.sendBtn.addEventListener('click', function() { handleSend(); });
      w.inputField.addEventListener('keydown', function(e){
          if(e.key === 'Enter') handleSend();
      });
      
      // Quick Action Buttons
      w.quickActions.forEach(function(btn) {
          btn.addEventListener('click', function() {
              var query = this.getAttribute('data-query');
              handleSend(query);
          });
      });
   }

   if(document.readyState==='loading'){
      document.addEventListener('DOMContentLoaded',init);
   } else {
      init();
   }
})();


