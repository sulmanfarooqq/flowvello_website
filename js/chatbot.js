/* ============================================
   FLOW VELLO — CHATBOT ENGINE (Static, No API)
   ============================================ */
(function(){
   'use strict';

   /* ---- Knowledge base ---- */
   var KB = [
      { keywords:['hello','hi','hey','good morning','good evening','howdy'], reply:'Hello! Welcome to Flow Vello. I can tell you about our services, process, or help you get in touch. What would you like to know?' },
      { keywords:['who are you','what is this','what is flow vello','about flow vello','about you'], reply:'Flow Vello is an AI automation and software agency. We build workflow automation, custom AI agents, WhatsApp automation, executive dashboards and custom software for growing businesses. Based in Pakistan, serving globally.' },
      { keywords:['service','services','what do you do','what you do','offer',' offerings'], reply:'We offer 6 core services:', topics:['Workflow Automation','AI Agents','WhatsApp & Messaging','AI Customer Support','Sales Automation','Executive Dashboards'] },
      { keywords:['workflow','automation','automate'], reply:'Workflow Automation: We connect your business tools and automate multi-step processes, handoffs, notifications and routine operations. This cuts manual work and speeds up your operations. Want details on any other service?' },
      { keywords:['ai agent','ai agents','custom ai','agent'], reply:'Custom AI Agents: We build task-focused agents trained on your business data. They execute tasks, make decisions, and adapt to your workflows — not just chatbots, but real working agents that qualify leads, route tickets, update CRMs and more.' },
      { keywords:['whatsapp','messaging','message','chat'], reply:'WhatsApp & Messaging Automation: We automate customer conversations, lead capture, order updates, reminders and human handoffs through WhatsApp and other messaging channels.' },
      { keywords:['customer support','support','help desk','helpdesk'], reply:'AI Customer Support: We deploy policy-aware AI support with knowledge retrieval, smart routing and human escalation. It handles repetitive questions so your team can focus on complex cases.' },
      { keywords:['sales','lead','leads','crm'], reply:'Sales Automation: We capture, qualify and follow up with leads automatically while keeping your CRM and sales pipeline consistently updated. No lead falls through the cracks.' },
      { keywords:['dashboard','dashboards','report','analytics','reporting'], reply:'Executive Dashboards: We bring your operational data into focused dashboards so leadership can see performance metrics without digging through spreadsheets. Real-time, from every connected system.' },
      { keywords:['software','development','web app','mobile app','app'], reply:'Software Development: We transform your concepts into scalable solutions — from bespoke internal tools to full web and mobile applications. Agile process, faster time-to-market.' },
      { keywords:['process','how it works','how you work','workflow','steps'], reply:'We follow a clear 6-stage process:\n\n1. Discovery — Find the bottleneck\n2. Strategy — Design the roadmap\n3. Proposal — Make the scope clear\n4. Build — Execute the system\n5. QA & Launch — Test before release\n6. Support — Improve after launch\n\nEach stage keeps everything visible from first conversation to post-launch.' },
      { keywords:['pricing','cost','price','how much','budget','quote'], reply:'Pricing depends on scope, complexity, number of integrations and ongoing support. Simple workflow automations cost less than full AI agent systems. We scope everything transparently before any commitment. Want to get a quote?' },
      { keywords:['contact','reach','get in touch','talk','call','email'], reply:'You can reach us at:\n\nEmail: contact@flowvello.com\nLocation: Islamabad, Pakistan (serving globally)\n\nOr fill out the form on our Contact page and we will get back to you within one business day.', topics:['Go to Contact Page'] },
      { keywords:['location','where','address','based'], reply:'We are based in Islamabad, Pakistan and serve businesses globally. Our team works across time zones to support clients worldwide.' },
      { keywords:['industry','industries','sector','niche'], reply:'We serve multiple industries: Ecommerce & Retail, Real Estate, SaaS & Tech, Service Businesses, Healthcare, Logistics, Finance, and more. The technology changes by industry — the goal stays the same: fewer manual steps, faster response, better visibility.' },
      { keywords:['security','secure','privacy','data'], reply:'Enterprise-grade security is built into every system. Your proprietary data stays yours. We build with strict access controls, data privacy, and policy-aware logic from the start.' },
      { keywords:['ai','artificial intelligence','machine learning','llm','chatgpt'], reply:'We integrate AI practically — not as decoration. Our AI solutions include custom AI agents, AI customer support with knowledge retrieval, and AI-powered workflow automation. We connect to top-tier models and your proprietary data.' },
      { keywords:['case study','case studies','client','result','results','portfolio'], reply:'We are currently onboarding our first clients under the Flow Vello name. Real case studies — the challenge, what we built, and the measured result — will be published on our Case Studies page as projects complete.', topics:['Go to Case Studies'] },
      { keywords:['faq','question','questions','answer'], reply:'Our FAQ covers topics like what we automate, how we work with existing tools, project timelines, AI security, and pricing. You can check it out on our FAQ page.', topics:['Go to FAQ Page'] },
      { keywords:['about','who','team','company'], reply:'Flow Vello is your partner for business process automation, custom AI agents, and software development. We focus on solving real operational problems — not selling templates. Learn more on our About page.', topics:['Go to About Page'] },
      { keywords:['thank','thanks','appreciate'], reply:'You are welcome! Is there anything else I can help you with?' },
      { keywords:['bye','goodbye','see you'], reply:'Goodbye! Feel free to come back anytime. Have a great day!' }
   ];

   var FALLBACK = "I am not sure I understand that. I can help with questions about our services, process, pricing, or how to reach us. Try asking about a specific topic or pick one below:";

   var SERVICE_PAGES = {
      'workflow automation':'service.html',
      'ai agents':'service.html',
      'whatsapp & messaging':'service.html',
      'ai customer support':'service.html',
      'sales automation':'service.html',
      'executive dashboards':'service.html'
   };

   var PAGE_LINKS = {
      'go to contact page':'contact.html',
      'go to faq page':'faq.html',
      'go to about page':'about.html',
      'go to case studies':'case-studies.html',
      'go to services':'service.html'
   };

   /* ---- DOM helpers ---- */
   function el(tag, cls, html){
      var e = document.createElement(tag);
      if(cls) e.className = cls;
      if(html) e.innerHTML = html;
      return e;
   }

   /* ---- Build widget DOM ---- */
   function buildWidget(){
      // trigger button
      var trigger = el('button','fv-chatbot-trigger');
      trigger.innerHTML = '<i class="fal fa-comments icon-chat"></i><i class="fal fa-times icon-close"></i>';
      trigger.setAttribute('aria-label','Open chat');
      document.body.appendChild(trigger);

      // window
      var win = el('div','fv-chatbot-window');
      win.innerHTML =
         '<div class="fv-chatbot-header">'+
            '<div class="fv-chatbot-header-avatar"><i class="fal fa-robot"></i></div>'+
            '<div class="fv-chatbot-header-info">'+
               '<h4>Flow Vello Assistant</h4>'+
               '<span>Ask me anything about our services</span>'+
            '</div>'+
         '</div>'+
         '<div class="fv-chatbot-messages"></div>'+
         '<div class="fv-chatbot-quick-actions">'+
            '<button class="fv-chat-quick-btn" data-q="What services do you offer?">Services</button>'+
            '<button class="fv-chat-quick-btn" data-q="How does your process work?">Process</button>'+
            '<button class="fv-chat-quick-btn" data-q="How much does it cost?">Pricing</button>'+
            '<button class="fv-chat-quick-btn" data-q="How can I contact you?">Contact</button>'+
         '</div>'+
         '<div class="fv-chatbot-input">'+
            '<input type="text" placeholder="Type your question..." />'+
            '<button class="fv-chatbot-send"><i class="fal fa-paper-plane"></i></button>'+
         '</div>';
      document.body.appendChild(win);

      return { trigger:trigger, win:win, messages:win.querySelector('.fv-chatbot-messages'), input:win.querySelector('input'), sendBtn:win.querySelector('.fv-chatbot-send'), quickActions:win.querySelector('.fv-chatbot-quick-actions') };
   }

   /* ---- Match user input ---- */
   function matchInput(text){
      var t = text.toLowerCase().replace(/[^\w\s]/g,'');
      for(var i=0;i<KB.length;i++){
         for(var j=0;j<KB[i].keywords.length;j++){
            if(t.indexOf(KB[i].keywords[j]) !== -1){
               return KB[i];
            }
         }
      }
      return null;
   }

   /* ---- Add message ---- */
   function addMessage(container, type, html){
      var msg = el('div','fv-chat-msg '+type, html);
      container.appendChild(msg);
      container.scrollTop = container.scrollHeight;
      return msg;
   }

   /* ---- Typing indicator ---- */
   function showTyping(container){
      var t = el('div','fv-chat-typing','<span></span><span></span><span></span>');
      container.appendChild(t);
      container.scrollTop = container.scrollHeight;
      return t;
   }

   /* ---- Render bot reply ---- */
   function botReply(container, match){
      var typing = showTyping(container);
      var delay = 600 + Math.random()*800;
      setTimeout(function(){
         typing.remove();
         var html = match.reply.replace(/\n/g,'<br>');
         addMessage(container,'bot',html);

         // topics / quick links
         if(match.topics && match.topics.length){
            var pills = el('div','fv-chat-topic-pills');
            match.topics.forEach(function(t){
               var pill = el('button','fv-chat-topic-pill',t);
               pill.addEventListener('click',function(){
                  handleUserInput(container, t);
               });
               pills.appendChild(pill);
            });
            container.appendChild(pills);
            container.scrollTop = container.scrollHeight;
         }
      }, delay);
   }

   /* ---- Handle user input ---- */
   function handleUserInput(container, text){
      if(!text || !text.trim()) return;
      addMessage(container,'user',text);
      var match = matchInput(text);
      if(match){
         botReply(container,match);
      } else {
         var typing = showTyping(container);
         setTimeout(function(){
            typing.remove();
            var html = FALLBACK + '<div class="fv-chat-topic-pills" style="margin-top:10px;">'+
               '<button class="fv-chat-topic-pill" data-q="services">Services</button>'+
               '<button class="fv-chat-topic-pill" data-q="process">Process</button>'+
               '<button class="fv-chat-topic-pill" data-q="pricing">Pricing</button>'+
               '<button class="fv-chat-topic-pill" data-q="contact">Contact</button>'+
            '</div>';
            addMessage(container,'bot',html);
            // attach listeners to fallback pills
            container.querySelectorAll('.fv-chat-topic-pill[data-q]').forEach(function(pill){
               pill.addEventListener('click',function(){
                  handleUserInput(container, pill.getAttribute('data-q'));
               });
            });
         }, 500);
      }
   }

   /* ---- Init ---- */
   function init(){
      var w = buildWidget();
      var isOpen = false;

      // toggle
      w.trigger.addEventListener('click',function(){
         isOpen = !isOpen;
         w.trigger.classList.toggle('active',isOpen);
         w.win.classList.toggle('open',isOpen);
         if(isOpen && w.messages.children.length === 0){
            addMessage(w.messages,'bot','Hi there! I am the Flow Vello assistant. I can tell you about our services, process, pricing, or help you get in touch. What would you like to know?');
         }
         if(isOpen) w.input.focus();
      });

      // send
      function send(){
         var val = w.input.value.trim();
         if(!val) return;
         w.input.value = '';
         handleUserInput(w.messages, val);
      }
      w.sendBtn.addEventListener('click',send);
      w.input.addEventListener('keydown',function(e){ if(e.key==='Enter') send(); });

      // quick action buttons
      w.quickActions.querySelectorAll('.fv-chat-quick-btn').forEach(function(btn){
         btn.addEventListener('click',function(){
            handleUserInput(w.messages, btn.getAttribute('data-q'));
         });
      });

      // topic pills (delegated)
      w.messages.addEventListener('click',function(e){
         var pill = e.target.closest('.fv-chat-topic-pill');
         if(!pill) return;
         var txt = pill.textContent.trim();
         // check if it's a page link
         var link = PAGE_LINKS[txt.toLowerCase()];
         if(link){
            window.location.href = link;
            return;
         }
         // check if it's a service
         var svcKey = txt.toLowerCase();
         if(SERVICE_PAGES[svcKey]){
            window.location.href = SERVICE_PAGES[svcKey];
            return;
         }
         handleUserInput(w.messages, txt);
      });
   }

   if(document.readyState==='loading'){
      document.addEventListener('DOMContentLoaded',init);
   } else {
      init();
   }
})();
