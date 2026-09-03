$(document).ready(function() {

   $("#hamburger").click(function() { $(".sidenav").toggleClass("active-nav"); });
   $("#showsidenav").click(function() { $(".sidenav").toggleClass("active-nav"); });

   $(".nav-item").click(function(){ $(this).siblings(".fal").toggleClass('active-fal'); });

   function checkWidth() {
      var windowSize = $(window).width();
      if (windowSize > 974) {
         $('#navigration .dropdown > .nav-link').removeClass('enabled').addClass('disabled');
         $('#navigration .dropdown-2 > .dropdown-item').removeClass('enabled').addClass('disabled');
      } else {
         $('#navigration .dropdown > .nav-link').removeClass('disabled').addClass('enabled');
         $('#navigration .dropdown-2 > .dropdown-item').removeClass('disabled').addClass('enabled');
      }
   }
   checkWidth();
   $(window).resize(checkWidth);

   $(window).scroll(function() {
      $("#navigration").css({ background: $(this).scrollTop() > 10 ? "#222429" : "none" });
   });

   $(".counter").counterUp({ delay: 10, time: 2000 });

   var owl = $('#homeSection .owl-carousel');
   owl.owlCarousel({ animateOut:'fadeOut', loop:true, nav:true, margin:0, autoplay:true, autoplayTimeout:3000, autoplayHoverPause:false, responsive:{0:{items:1}} });

   var mixer = mixitup('#portfolio');
   $(".indicator > span").click(function() { $(".indicator > span").removeClass("active"); $(this).addClass("active"); });

   var owl2 = $('#testimonialSection .owl-carousel');
   owl2.owlCarousel({ animateOut:'fadeOut', loop:true, nav:false, margin:30, autoplay:true, autoplayTimeout:3000, autoplayHoverPause:true, responsive:{0:{items:1},768:{items:2}} });

   var owl3 = $('#specialFeature .owl-carousel');
   owl3.owlCarousel({ animateOut:'fadeOut', loop:true, nav:false, margin:30, autoplay:true, autoplayTimeout:3000, autoplayHoverPause:true, responsive:{0:{items:1},768:{items:2},1024:{items:3}} });

   var wow = new WOW({ boxClass:'wow', animateClass:'animated', offset:0, mobile:true, live:true, scrollContainer:null, resetAnimation:true });
   wow.init();

   // Keep the new homepage sections visually consistent with the existing Flow Vello theme.
   var themeStyle = document.createElement('style');
   themeStyle.setAttribute('data-flowvello-theme','true');
   themeStyle.textContent = `
      .fv-section,.fv-partner,.fv-industries,.fv-trust,.fv-why,.fv-process,.fv-faq,.fv-cta{position:relative;overflow:hidden}
      .fv-section{padding:100px 0}.fv-partner{padding:60px 0;background:#f5f5f3;border-top:1px solid #e5e5e3;border-bottom:1px solid #e5e5e3}
      .fv-eyebrow{font-family:'Rubik',sans-serif;display:inline-block;margin-bottom:16px;font-size:12px;font-weight:700;letter-spacing:2.5px;color:#fb383b;text-transform:uppercase}
      .fv-lead,.fv-value p,.fv-industry p,.fv-service-card p,.fv-step p,.fv-faq-item p,.fv-why-card span{font-family:'Rubik',sans-serif}
      .fv-lead{max-width:680px;color:#666;line-height:1.8;font-size:16px}.fv-centered{margin-left:auto;margin-right:auto;text-align:center}
      .fv-partner-title{font-family:'Rubik',sans-serif;margin:0;font-size:14px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#1d1e22}
      .fv-value{height:100%;padding:25px 22px;background:#fff;border-left:3px solid #fb383b;transition:.4s;box-shadow:0 8px 30px rgba(29,30,34,.04)}
      .fv-value:hover{transform:translateY(-5px);box-shadow:0 15px 35px rgba(29,30,34,.09)}.fv-value h4{margin:0;color:#1d1e22;font-size:27px;line-height:1}.fv-value p{margin:13px 0 0;color:#666;line-height:1.7;font-size:14px}
      .fv-industries{padding:90px 0;background:#222429;color:#fff}.fv-industries h2{color:#fff}.fv-industry{height:100%;padding:30px 25px;border:1px solid rgba(255,255,255,.13);transition:.4s;position:relative}.fv-industry:before{content:'';position:absolute;left:0;top:0;width:0;height:3px;background:#fb383b;transition:.4s}.fv-industry:hover{border-color:#fb383b;transform:translateY(-6px)}.fv-industry:hover:before{width:100%}.fv-industry span,.fv-service-number,.fv-step .step-no{font-family:'Rubik',sans-serif;color:#fb383b;font-size:12px;font-weight:700;letter-spacing:2px}.fv-industry h3{color:#fff;margin:14px 0 10px;font-size:32px}.fv-industry p{margin:0;color:#bdbec2;line-height:1.7;font-size:14px}
      .fv-service-intro{padding-right:30px}.fv-service-card,.fv-step{height:100%;position:relative;padding:30px 27px;background:#fff;border:1px solid #e4e4e2;transition:.4s}.fv-service-card:before,.fv-step:before{content:'';position:absolute;left:0;top:0;width:3px;height:0;background:#fb383b;transition:.4s}.fv-service-card:hover,.fv-step:hover{border-color:#222429;transform:translateY(-6px);box-shadow:0 16px 35px rgba(29,30,34,.09)}.fv-service-card:hover{background:#222429}.fv-service-card:hover:before,.fv-step:hover:before{height:100%}.fv-service-card h3{margin:18px 0 12px;font-size:32px;line-height:.95}.fv-service-card p{margin:0;color:#666;line-height:1.7;font-size:14px}.fv-service-card:hover h3{color:#fff}.fv-service-card:hover p{color:#c6c7ca}.fv-service-card a{display:inline-block;margin-top:20px;color:#fb383b;font-family:'Rubik',sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px}
      .fv-trust{padding:35px 0;background:#f7f7f5;border-top:1px solid #e5e5e3;border-bottom:1px solid #e5e5e3}.fv-trust-label{font-family:'Rubik',sans-serif;margin:0 0 18px;font-size:12px;font-weight:700;letter-spacing:2px;color:#666;text-transform:uppercase}.fv-trust-list{display:flex;flex-wrap:wrap;gap:10px;justify-content:center}.fv-chip{font-family:'Rubik',sans-serif;padding:10px 16px;border:1px solid #ddd;background:#fff;font-size:12px;font-weight:600;transition:.3s}.fv-chip:hover{border-color:#fb383b;color:#fb383b}
      .fv-why{background:#f5f5f3}.fv-why-card{padding:25px 0;border-top:1px solid #ddd}.fv-why-card:last-child{border-bottom:1px solid #ddd}.fv-why-card strong{display:block;color:#1d1e22;font-size:25px;line-height:1;margin-bottom:8px}.fv-why-card span{color:#666;line-height:1.7;font-size:14px}
      .fv-process{background:#fff}.fv-step .step-no{display:block}.fv-step h3{font-size:30px;margin:16px 0 10px;line-height:.95}.fv-step p{color:#666;line-height:1.7;font-size:14px;margin:0}
      .fv-faq{background:#f5f5f3}.fv-faq-item{border-top:1px solid #ddd;padding:23px 0}.fv-faq-item:last-child{border-bottom:1px solid #ddd}.fv-faq-item h3{font-size:28px;line-height:1;margin:0 0 8px;color:#1d1e22}.fv-faq-item p{color:#666;line-height:1.7;margin:0;font-size:14px}
      .fv-cta{padding:90px 0;background:#222429;color:#fff;text-align:center}.fv-cta:before{content:'';position:absolute;right:-120px;top:-120px;width:360px;height:360px;border:1px solid rgba(251,56,59,.25);border-radius:50%}.fv-cta h2{color:#fff;font-size:70px;margin-bottom:15px}.fv-cta p{font-family:'Rubik',sans-serif;max-width:650px;margin:0 auto 28px;color:#c6c7ca;line-height:1.8}.fv-cta .btn{background:#fb383b;color:#fff;border-color:#fb383b}.fv-small-note{font-family:'Rubik',sans-serif;font-size:12px;color:#666;margin-top:15px}
      .fv-section .sec-header h2{margin-bottom:25px}.fv-section .sec-header h2 span,.fv-why .sec-header h2 span{color:#fb383b}
      @media(max-width:991px){.fv-section{padding:75px 0}.fv-service-intro{padding-right:0;margin-bottom:35px}.fv-cta h2{font-size:55px}}
      @media(max-width:767px){.fv-partner,.fv-industries,.fv-cta{padding:60px 0}.fv-cta h2{font-size:40px}.fv-industry h3,.fv-service-card h3,.fv-faq-item h3{font-size:27px}}
   `;
   document.head.appendChild(themeStyle);

   // SEO structured data for the homepage.
   if (!document.querySelector('script[data-flowvello-schema]')) {
      var schema = {"@context":"https://schema.org","@graph":[
         {"@type":"Organization","@id":"https://flowvello.com/#organization","name":"Flow Vello","url":"https://flowvello.com/","logo":"https://flowvello.com/img/softoweb.png","description":"Flow Vello builds workflow automation, AI agents, WhatsApp automation, executive dashboards and custom software for growing businesses."},
         {"@type":"WebSite","@id":"https://flowvello.com/#website","url":"https://flowvello.com/","name":"Flow Vello","publisher":{"@id":"https://flowvello.com/#organization"},"inLanguage":"en"},
         {"@type":"WebPage","@id":"https://flowvello.com/#webpage","url":"https://flowvello.com/","name":"Flow Vello | AI Automation, Agents & Software","description":"Flow Vello builds workflow automation, AI agents, WhatsApp automation, executive dashboards and custom software for growing businesses.","isPartOf":{"@id":"https://flowvello.com/#website"},"about":{"@id":"https://flowvello.com/#organization"},"inLanguage":"en"},
         {"@type":"Service","name":"Workflow Automation","serviceType":"Workflow Automation","provider":{"@id":"https://flowvello.com/#organization"},"areaServed":"Worldwide"},
         {"@type":"Service","name":"Custom AI Agents","serviceType":"AI Agent Development","provider":{"@id":"https://flowvello.com/#organization"},"areaServed":"Worldwide"},
         {"@type":"Service","name":"WhatsApp & Messaging Automation","serviceType":"WhatsApp Automation","provider":{"@id":"https://flowvello.com/#organization"},"areaServed":"Worldwide"},
         {"@type":"Service","name":"AI Customer Support","serviceType":"AI Customer Support Automation","provider":{"@id":"https://flowvello.com/#organization"},"areaServed":"Worldwide"},
         {"@type":"Service","name":"Sales Automation","serviceType":"Sales Automation","provider":{"@id":"https://flowvello.com/#organization"},"areaServed":"Worldwide"},
         {"@type":"Service","name":"Executive Dashboards","serviceType":"Business Intelligence Dashboards","provider":{"@id":"https://flowvello.com/#organization"},"areaServed":"Worldwide"}
      ]};
      var schemaScript=document.createElement('script');schemaScript.type='application/ld+json';schemaScript.setAttribute('data-flowvello-schema','true');schemaScript.text=JSON.stringify(schema);document.head.appendChild(schemaScript);
   }

   if (!document.querySelector('link[rel="canonical"]')) { var canonical=document.createElement('link');canonical.rel='canonical';canonical.href='https://flowvello.com/';document.head.appendChild(canonical); }

   var socialMeta={'og:type':'website','og:url':'https://flowvello.com/','og:title':'Flow Vello | AI Automation, Agents & Software','og:description':'Workflow automation, AI agents, WhatsApp automation, executive dashboards and custom software for growing businesses.','twitter:card':'summary_large_image','twitter:title':'Flow Vello | AI Automation, Agents & Software','twitter:description':'Workflow automation, AI agents, WhatsApp automation, executive dashboards and custom software for growing businesses.'};
   Object.keys(socialMeta).forEach(function(key){var attr=key.indexOf('twitter:')===0?'name':'property';if(!document.querySelector('meta['+attr+'="'+key+'"]')){var meta=document.createElement('meta');meta.setAttribute(attr,key);meta.content=socialMeta[key];document.head.appendChild(meta);}});

   $('.popup-with-zoom-anim').magnificPopup({type:'inline',fixedContentPos:false,fixedBgPos:true,overflowY:'auto',closeBtnInside:true,preloader:false,midClick:true,removalDelay:300,mainClass:'my-mfp-zoom-in'});

   $(".scroll-up").fadeOut();
   $(window).scroll(function(){ if($(this).scrollTop()>100){$(".scroll-up").fadeIn();}else{$(".scroll-up").fadeOut();} });
   $(".scroll-up").click(function(){ $("html").animate({scrollTop:0},1000); return false; });

});
