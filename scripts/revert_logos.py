# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

# I will use the exact original SVG URLs but inject the text underneath them so it looks like "before, along with a text too".
new_grid = '''
              <div class="logo-grid">
                 <!-- Top Row -->
                 <div class="logo-grid-item bg-light border-right border-bottom relative-box flex-column" style="flex-direction: column;">
                    <img src="https://cdn.21st.dev/assets/mirror/bd/bdf5f3ae72bcfda892a686c03b7932985c694e9a9828643c980601bbc9e53cb4.svg" alt="Nvidia">
                    <span style="margin-top: 10px; font-family: 'Rubik', sans-serif; font-size: 13px; font-weight: 600; color: #6b7280; letter-spacing: 0.5px; text-transform: uppercase;">Nvidia</span>
                    <i class="fal fa-plus crosshair bottom-right d-none d-md-block"></i>
                 </div>
                 <div class="logo-grid-item bg-white border-right border-bottom relative-box flex-column" style="flex-direction: column;">
                    <img src="https://cdn.21st.dev/assets/mirror/31/319eeae853dd1af99d442b6c16b6c38dc52a66a719f8e502c65f85d26255cbd3.svg" alt="Supabase">
                    <span style="margin-top: 10px; font-family: 'Rubik', sans-serif; font-size: 13px; font-weight: 600; color: #6b7280; letter-spacing: 0.5px; text-transform: uppercase;">Supabase</span>
                    <i class="fal fa-plus crosshair bottom-right d-none d-md-block"></i>
                 </div>
                 <div class="logo-grid-item bg-light border-right border-bottom relative-box flex-column" style="flex-direction: column;">
                    <img src="https://cdn.21st.dev/assets/mirror/90/90f01a9537335666282ae5acc80bd4305f86d085a92d60904c3aa3ccc4414570.svg" alt="GitHub">
                    <span style="margin-top: 10px; font-family: 'Rubik', sans-serif; font-size: 13px; font-weight: 600; color: #6b7280; letter-spacing: 0.5px; text-transform: uppercase;">GitHub</span>
                    <i class="fal fa-plus crosshair bottom-right d-none d-md-block"></i>
                 </div>
                 <div class="logo-grid-item bg-white border-bottom flex-column" style="flex-direction: column;">
                    <img src="https://cdn.21st.dev/assets/mirror/2b/2bcdd4124223e3bf8e66bc08ce0ac32a6cc42ffe3584bbecfd377847176a188d.svg" alt="OpenAI">
                    <span style="margin-top: 10px; font-family: 'Rubik', sans-serif; font-size: 13px; font-weight: 600; color: #6b7280; letter-spacing: 0.5px; text-transform: uppercase;">OpenAI</span>
                 </div>
  
                 <!-- Bottom Row -->
                 <div class="logo-grid-item bg-white border-right flex-column" style="flex-direction: column;">
                    <img src="https://cdn.21st.dev/assets/mirror/fc/fc7b090ebcfc468d24a1dc482b2db1fcbfd99ca14568552a30ce553d6dda7fcb.svg" alt="Turso">
                    <span style="margin-top: 10px; font-family: 'Rubik', sans-serif; font-size: 13px; font-weight: 600; color: #6b7280; letter-spacing: 0.5px; text-transform: uppercase;">Turso</span>
                 </div>
                 <div class="logo-grid-item bg-light border-right flex-column" style="flex-direction: column;">
                    <img src="https://cdn.21st.dev/assets/mirror/96/96517bce3574d648280ff639d01d9889f354b488b3f826db5df746d730232a0c.svg" alt="Clerk">
                    <span style="margin-top: 10px; font-family: 'Rubik', sans-serif; font-size: 13px; font-weight: 600; color: #6b7280; letter-spacing: 0.5px; text-transform: uppercase;">Clerk</span>
                 </div>
                 <div class="logo-grid-item bg-white border-right flex-column" style="flex-direction: column;">
                    <img src="https://cdn.21st.dev/assets/mirror/e8/e8514b1206f79e1abdafcc1d2632393cc7cfbcbbe25426ac5143b17b184b56b8.svg" alt="Claude">
                    <span style="margin-top: 10px; font-family: 'Rubik', sans-serif; font-size: 13px; font-weight: 600; color: #6b7280; letter-spacing: 0.5px; text-transform: uppercase;">Claude</span>
                 </div>
                 <div class="logo-grid-item bg-light flex-column" style="flex-direction: column;">
                    <img src="https://cdn.21st.dev/assets/mirror/56/5624b7c243ac8d60e848fb5ea222ec932c1600df54a2762238b37498372fb0c8.svg" alt="Vercel">
                    <span style="margin-top: 10px; font-family: 'Rubik', sans-serif; font-size: 13px; font-weight: 600; color: #6b7280; letter-spacing: 0.5px; text-transform: uppercase;">Vercel</span>
                 </div>
              </div>
'''

match = re.search(r'(?s)(<div class="logo-grid">)(.*?)(</div>\s*</div>\s*</div>\s*</section>)', html)
if match:
    new_html = html[:match.start(1)] + new_grid + html[match.start(3):]
    with open('c:/Users/my/Desktop/chatgpt/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Reverted to original tech stack with text names included.")
else:
    print("Regex failed.")
