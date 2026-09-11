# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_section = '''     <section class="fv-contact-scheduling" style="background-color: #0b0f19; padding-top: 80px; padding-bottom: 80px; min-height: 100vh;">
        <div class="container">
           <h1 class="wow fadeInUp text-center" data-wow-delay="0.1s" style="color: #ffffff; font-family: 'Rubik', sans-serif; font-size: 42px; font-weight: 600; margin-bottom: 60px;">Lets Work Together!</h1>
           
           <!-- CLEAN NATIVE CALENDLY EMBED -->
           <div class="wow fadeInUp" data-wow-delay="0.2s" style="max-width: 1060px; margin: 0 auto; border-radius: 8px; overflow: hidden; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);">
              <div class="calendly-inline-widget" data-url="https://calendly.com/contact-flowvello/30min?hide_gdpr_banner=1" style="min-width:320px;height:700px;"></div>
              <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
           </div>
           
           <!-- Three column footer info -->'''

html = re.sub(r'(?s)<section class="fv-contact-scheduling" style="background-color: #0b0f19; padding-top: 80px; padding-bottom: \n80px;">.*?<!-- Three column footer info -->', new_section, html)
# Try second regex just in case there's no newline in padding-bottom
html = re.sub(r'(?s)<section class="fv-contact-scheduling".*?<!-- Three column footer info -->', new_section, html)

with open('c:/Users/my/Desktop/chatgpt/contact.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Contact page Calendly widget rebuilt.")
