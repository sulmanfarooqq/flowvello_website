# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

# 1. Delete redundant "Our Why" section
# Match from "<!-- PARTNER WITH US" to "<!-- WHY FLOW VELLO"
html = re.sub(r'(?s)<!-- PARTNER WITH US \(MODERN FEATURE WITH IMAGE\).*?<!-- WHY FLOW VELLO \(FEATURE GRID\)', '<!-- WHY FLOW VELLO (FEATURE GRID)', html)

# 2. Inject Ecosystem Flywheel Bento Box after Tech Stack
bento_html = '''
     <!-- ECOSYSTEM FLYWHEEL (BENTO BOX) -->
     <section class="fv-ecosystem-bento py-5" style="background-color: #f9fafb;">
        <div class="container py-5">
           <div class="text-center mb-5 pb-3">
              <span class="fv-eyebrow wow fadeInUp" style="display:inline-block; margin-bottom: 15px;">THE FLYWHEEL</span>
              <h2 class="wow fadeInUp" data-wow-delay="0.1s" style="font-family:'Rubik', sans-serif; font-size:46px; font-weight:600; color:#111827; letter-spacing:-1.5px;">One Unified Growth Engine.</h2>
              <p class="wow fadeInUp" data-wow-delay="0.2s" style="color:#6b7280; font-size:18px; max-width:600px; margin: 15px auto 0;">We don't just sell isolated services. We engineer a compounding ecosystem where your software, operations, and marketing feed each other.</p>
           </div>
           <style>
               .bento-grid { display: grid; gap: 24px; grid-template-columns: repeat(4, 1fr); grid-auto-rows: minmax(180px, auto); }
               .bento-box { background: #fff; border-radius: 20px; padding: 40px; border: 1px solid #e5e7eb; box-shadow: 0 4px 20px rgba(0,0,0,0.03); transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease; position: relative; overflow: hidden; }
               .bento-box:hover { transform: translateY(-5px); box-shadow: 0 15px 35px rgba(0,0,0,0.08); border-color: #fb383b; }
               .bento-icon { width: 56px; height: 56px; border-radius: 14px; background: #fdf2f2; color: #fb383b; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 25px; }
               
               .bento-dev { grid-column: span 4; }
               .bento-auto { grid-column: span 4; }
               .bento-creative { grid-column: span 4; }
               .bento-marketing { grid-column: span 4; }
               
               @media (min-width: 992px) {
                   .bento-dev { grid-column: span 2; grid-row: span 2; }
                   .bento-auto { grid-column: span 2; }
                   .bento-creative { grid-column: span 1; }
                   .bento-marketing { grid-column: span 1; }
               }
           </style>
           <div class="bento-grid wow fadeInUp" data-wow-delay="0.3s">
               <!-- Development (Large Box) -->
               <div class="bento-box bento-dev">
                   <div class="bento-icon"><i class="fal fa-browser"></i></div>
                   <h3 style="font-family:'Rubik', sans-serif; font-size: 26px; font-weight: 600; color: #111827;">1. Foundation</h3>
                   <span style="font-size: 12px; font-weight: 700; color: #fb383b; text-transform: uppercase; letter-spacing: 1.5px; display: block; margin-bottom: 15px;">Development</span>
                   <p style="color:#6b7280; font-size: 16px; line-height: 1.7; margin: 0;">We architect scalable custom software, e-commerce platforms, and robust web applications. This is the indestructible bedrock of your digital business.</p>
               </div>
               
               <!-- Automation -->
               <div class="bento-box bento-auto">
                   <div class="bento-icon"><i class="fal fa-robot"></i></div>
                   <h3 style="font-family:'Rubik', sans-serif; font-size: 22px; font-weight: 600; color: #111827;">2. Scale</h3>
                   <span style="font-size: 12px; font-weight: 700; color: #fb383b; text-transform: uppercase; letter-spacing: 1.5px; display: block; margin-bottom: 15px;">Automation</span>
                   <p style="color:#6b7280; font-size: 15px; line-height: 1.6; margin: 0;">We layer autonomous AI agents and API workflows over your foundation to eliminate manual labor and accelerate data processing.</p>
               </div>

               <!-- Creative -->
               <div class="bento-box bento-creative" style="padding: 30px;">
                   <div class="bento-icon" style="width: 48px; height: 48px; font-size: 20px; margin-bottom: 20px;"><i class="fal fa-pen-nib"></i></div>
                   <h3 style="font-family:'Rubik', sans-serif; font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 5px;">3. Brand</h3>
                   <span style="font-size: 11px; font-weight: 700; color: #fb383b; text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 10px;">Creative</span>
                   <p style="color:#6b7280; font-size: 14px; line-height: 1.5; margin: 0;">Elite UI/UX prototyping and digital branding.</p>
               </div>

               <!-- Marketing -->
               <div class="bento-box bento-marketing" style="padding: 30px;">
                   <div class="bento-icon" style="width: 48px; height: 48px; font-size: 20px; margin-bottom: 20px;"><i class="fal fa-bullhorn"></i></div>
                   <h3 style="font-family:'Rubik', sans-serif; font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 5px;">4. Traffic</h3>
                   <span style="font-size: 11px; font-weight: 700; color: #fb383b; text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 10px;">Marketing</span>
                   <p style="color:#6b7280; font-size: 14px; line-height: 1.5; margin: 0;">Relentless growth, SEO, and LinkedIn scaling.</p>
               </div>
           </div>
        </div>
     </section>
'''

html = re.sub(r'(?s)(</section>\s*)(<!-- WHY FLOW VELLO \(FEATURE GRID\))', r'\1' + bento_html + r'\n     \2', html)

# 3. Inject Technical Audit Lead Capture right above FAQ
lead_capture_html = '''
     <!-- MID-FUNNEL LEAD CAPTURE -->
     <section class="fv-lead-capture py-5" style="background-color: #111827; position: relative; overflow: hidden;">
        <div style="position: absolute; inset: 0; background-image: radial-gradient(#374151 1.5px, transparent 1.5px); background-size: 24px 24px; opacity: 0.2; z-index: 0;"></div>
        <div class="container py-5 text-center" style="position: relative; z-index: 1;">
           <span class="wow fadeInUp" style="color: #fb383b; font-family: 'Rubik', sans-serif; font-size: 12px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px; display: inline-block;">FREE TECHNICAL AUDIT</span>
           <h2 class="wow fadeInUp" data-wow-delay="0.1s" style="color: #ffffff; font-family: 'Rubik', sans-serif; font-size: 46px; font-weight: 600; line-height: 1.15; letter-spacing: -1.5px; max-width: 800px; margin: 0 auto 25px;">Stop guessing. Get a definitive architecture roadmap.</h2>
           <p class="wow fadeInUp" data-wow-delay="0.2s" style="color: #9ca3af; font-family: 'Rubik', sans-serif; font-size: 18px; line-height: 1.7; max-width: 600px; margin: 0 auto 40px;">Before you spend another dollar on disjointed SaaS tools, let our engineers audit your workflow and design a custom digital blueprint.</p>
           <a href="contact.html" class="fv-btn fv-btn-primary wow fadeInUp" data-wow-delay="0.3s" style="padding: 16px 36px; font-size: 16px;">Claim Your Free Audit <i class="fal fa-arrow-right ml-2"></i></a>
        </div>
     </section>
'''

html = re.sub(r'(?s)(<!-- FAQ PAGE -->\s*<section)', lead_capture_html + r'\n     \1', html)

with open('c:/Users/my/Desktop/chatgpt/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Homepage surgically restructured. Bento box and Lead Capture injected.")
