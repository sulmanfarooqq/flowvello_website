# -*- coding: utf-8 -*-
import re
import codecs

with codecs.open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Strip inline typography
html = re.sub(r'font-family:\s*\'Rubik\',sans-serif;\s*', '', html)
html = re.sub(r'font-size:\s*[0-9]+px;\s*', '', html)
html = re.sub(r'line-height:\s*[0-9.]+;\s*', '', html)
html = re.sub(r'letter-spacing:\s*[-0-9.]+px;\s*', '', html)

# Fix the Hero section
hero_replacement = """
   <!-- PAGE HERO -->
   <section class="fv-page-hero" style="background: url('img/about-hero-bg.jpg') no-repeat center center; background-size: cover;">
      <div style="position:absolute;inset:0;background:rgba(29, 30, 34, 0.85);z-index:0;"></div>
      <div style="position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.04) 1.5px,transparent 1.5px);background-size:24px 24px;z-index:0;"></div>
      <div class="container" style="position:relative;z-index:1;">
         <div class="row">
            <div class="col-lg-8">
               <span class="fv-eyebrow" style="color:rgba(255,255,255,.6);">ABOUT FLOW VELLO</span>
               <h1>We build the systems that make businesses run better<span style="color:var(--fv-red);">.</span></h1>
               <p style="color:rgba(255,255,255,0.8); font-weight:300;">Flow Vello helps businesses eliminate repetitive work, connect disconnected systems and build smarter operations through automation, AI agents and custom software.</p>
            </div>
         </div>
      </div>
   </section>
"""

# Replace existing hero
html = re.sub(r'<!-- PAGE HERO \(VISUAL\) -->.*?</section>', hero_replacement, html, flags=re.DOTALL)

with codecs.open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Typography inline styles stripped and Hero updated.")
