# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

new_grid = '''
              <div class="logo-grid">
                 <!-- Top Row -->
                 <div class="logo-grid-item bg-light border-right border-bottom relative-box">
                    <img src="https://cdn.worldvectorlogo.com/logos/salesforce-2.svg" alt="Salesforce">
                    <i class="fal fa-plus crosshair bottom-right d-none d-md-block"></i>
                 </div>
                 <div class="logo-grid-item bg-white border-right border-bottom relative-box">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/0/0e/Shopify_logo_2018.svg" alt="Shopify">
                    <i class="fal fa-plus crosshair bottom-right d-none d-md-block"></i>
                 </div>
                 <div class="logo-grid-item bg-light border-right border-bottom relative-box">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/3/33/Figma-logo.svg" alt="Figma">
                    <i class="fal fa-plus crosshair bottom-right d-none d-md-block"></i>
                 </div>
                 <div class="logo-grid-item bg-white border-bottom">
                    <img src="https://cdn.21st.dev/assets/mirror/2b/2bcdd4124223e3bf8e66bc08ce0ac32a6cc42ffe3584bbecfd377847176a188d.svg" alt="OpenAI">
                 </div>
  
                 <!-- Bottom Row -->
                 <div class="logo-grid-item bg-white border-right relative-box">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/f/fd/Zapier_logo.svg" alt="Zapier">
                 </div>
                 <div class="logo-grid-item bg-light border-right relative-box">
                    <img src="https://cdn.worldvectorlogo.com/logos/hubspot.svg" alt="HubSpot">
                 </div>
                 <div class="logo-grid-item bg-white border-right relative-box">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Stripe_Logo%2C_revised_2016.svg" alt="Stripe">
                 </div>
                 <div class="logo-grid-item bg-light">
                    <img src="https://cdn.worldvectorlogo.com/logos/aws-2.svg" alt="AWS">
                 </div>
              </div>
'''

match = re.search(r'(?s)(<div class="logo-grid">)(.*?)(</div>\s*</div>\s*</div>\s*</section>)', html)
if match:
    new_html = html[:match.start(1)] + new_grid + html[match.start(3):]
    with open('c:/Users/my/Desktop/chatgpt/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Replaced Next.js with Salesforce, restored original OpenAI logo.")
else:
    print("Regex failed.")
