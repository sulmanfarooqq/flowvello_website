# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

new_grid = '''
              <div class="logo-grid">
                 <!-- Top Row -->
                 <div class="logo-grid-item bg-light border-right border-bottom relative-box">
                    <img src="https://cdn.simpleicons.org/nextdotjs" alt="Next.js" title="Web Applications">
                    <i class="fal fa-plus crosshair bottom-right d-none d-md-block"></i>
                 </div>
                 <div class="logo-grid-item bg-white border-right border-bottom relative-box">
                    <img src="https://cdn.simpleicons.org/shopify" alt="Shopify" title="E-Commerce">
                    <i class="fal fa-plus crosshair bottom-right d-none d-md-block"></i>
                 </div>
                 <div class="logo-grid-item bg-light border-right border-bottom relative-box">
                    <img src="https://cdn.simpleicons.org/figma" alt="Figma" title="UI/UX Design">
                    <i class="fal fa-plus crosshair bottom-right d-none d-md-block"></i>
                 </div>
                 <div class="logo-grid-item bg-white border-bottom">
                    <img src="https://cdn.simpleicons.org/openai" alt="OpenAI" title="AI Agents">
                 </div>
  
                 <!-- Bottom Row -->
                 <div class="logo-grid-item bg-white border-right">
                    <img src="https://cdn.simpleicons.org/zapier" alt="Zapier" title="Workflow Automation">
                 </div>
                 <div class="logo-grid-item bg-light border-right">
                    <img src="https://cdn.simpleicons.org/wordpress" alt="WordPress" title="CMS Development">
                 </div>
                 <div class="logo-grid-item bg-white border-right">
                    <img src="https://cdn.simpleicons.org/supabase" alt="Supabase" title="Database Architecture">
                 </div>
                 <div class="logo-grid-item bg-light">
                    <img src="https://cdn.simpleicons.org/vercel" alt="Vercel" title="Cloud Deployment">
                 </div>
              </div>
'''

match = re.search(r'(?s)(<div class="logo-grid">)(.*?)(</div>\s*</div>\s*</div>\s*</section>)', html)
if match:
    new_html = html[:match.start(1)] + new_grid + html[match.start(3):]
    with open('c:/Users/my/Desktop/chatgpt/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Updated tech stack logo grid.")
else:
    print("Regex failed.")
