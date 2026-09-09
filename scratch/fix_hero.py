# -*- coding: utf-8 -*-
import re
import codecs

with codecs.open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

hero_replacement = """
   <!-- PAGE HERO -->
   <section class="fv-page-hero" style="background: url('img/about-hero-bg.jpg') no-repeat center center; background-size: cover; padding: 160px 0 80px; position: relative; overflow: hidden;">
      <div style="position:absolute;inset:0;background-image:radial-gradient(rgba(0,0,0,.04) 1.5px,transparent 1.5px);background-size:24px 24px;z-index:0;"></div>
      <div class="container" style="position:relative;z-index:1;">
         <div class="row">
            <div class="col-lg-10">
               <span class="fv-eyebrow" style="color:var(--fv-red); display:inline-block; margin-bottom:14px; font-size:13px; font-weight:700; letter-spacing:2px; text-transform:uppercase;">ABOUT FLOW VELLO</span>
               <h1 style="color: #111827; font-family: 'Rubik', sans-serif; font-size: 64px; font-weight: 500; letter-spacing: -1.5px; line-height: 1.1; margin-bottom: 24px; text-transform: none;">We build the systems that make businesses run better<span style="color:var(--fv-red);">.</span></h1>
               <p style="color: #4b5563; font-family: 'Rubik', sans-serif; font-size: 20px; line-height: 1.6; margin-bottom: 40px; font-weight: 400; max-width: 800px; text-transform: none; letter-spacing: 0;">Flow Vello helps businesses eliminate repetitive work, connect disconnected systems and build smarter operations through automation, AI agents and custom software.</p>
            </div>
         </div>
      </div>
   </section>
"""

# Replace existing hero
html = re.sub(r'<!-- PAGE HERO -->.*?</section>', hero_replacement, html, flags=re.DOTALL)

with codecs.open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero updated with light background and index.html typography.")
