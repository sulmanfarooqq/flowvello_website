# -*- coding: utf-8 -*-
import re
import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html_updated = f.read()

# 1. Partner with Us
html_updated = re.sub(r'<h2 class="mb-5 text-center" style="[^"]*">', 
                      r'<h2 class="mb-5 text-center wow fadeInUp" style="font-family: \'Rubik\', sans-serif; font-size: 52px; font-weight: 600; line-height: 1.15; letter-spacing: -1.5px; max-width: 850px; margin-left: auto; margin-right: auto; color: #111827;">', 
                      html_updated)

# 2. Who We Help
html_updated = re.sub(r'<div class="col-lg-8">\s*<h2>Who We Help & Why</h2>', 
                      r'<div class="col-lg-10 mx-auto text-center">\n               <span class="fv-eyebrow wow fadeInUp" style="display:inline-block; margin:0 auto 15px;">WHO WE HELP</span><h2 class="wow fadeInUp" style="color: #111827; font-family: \'Rubik\', sans-serif; font-size: 52px; font-weight: 600; line-height: 1.15; letter-spacing: -1.5px; max-width: 850px; margin: 0 auto 30px;">Partner with Flow Vello to scale without chaos</h2>', 
                      html_updated)
html_updated = re.sub(r'<p class="presentation-subtitle">',
                      r'<p class="presentation-subtitle wow fadeInUp" style="max-width: 700px; margin: 0 auto 50px;">',
                      html_updated)

# 3. Industries
html_updated = re.sub(r'<h2 style="color:#1d1e22; font-family:\'Teko\', sans-serif; font-size:48px;">AUTOMATION FOR REAL BUSINESS OPERATIONS<span style="color:#fb383b;">\.</span></h2>',
                      r'<span class="fv-eyebrow wow fadeInUp" style="display:inline-block; margin:0 auto 15px;">INDUSTRIES</span><h2 class="wow fadeInUp" style="color:#111827; font-family:\'Teko\', sans-serif; font-size:64px; line-height:1.1; letter-spacing:1px; max-width:900px; margin:0 auto 40px; text-transform:uppercase;">AUTOMATION FOR REAL BUSINESS OPERATIONS<span style="color:#fb383b;">.</span></h2>',
                      html_updated)

# 4. Capabilities Grid
html_updated = re.sub(r'<h2 class="fw-bold mb-4" style="[^"]*">\s*Capabilities we build around\s*</h2>', 
                      r'<span class="fv-eyebrow wow fadeInUp" style="display:inline-block; margin:0 auto 15px; color:rgba(255,255,255,0.6);">CAPABILITIES</span><h2 class="wow fadeInUp" style="color: #ffffff; font-family: \'Rubik\', sans-serif; font-size: 52px; line-height: 1.15; letter-spacing: -1.5px; max-width: 850px; margin: 0 auto 50px;">Capabilities we build around</h2>', 
                      html_updated, flags=re.DOTALL)

# 5. Why Flow Vello
html_updated = re.sub(r'<h2 class="fw-bold" style="[^"]*">\s*NO TEMPLATES\. NO BUSYWORK\. <br>JUST THE RIGHT SYSTEM<span style="color: #fb383b;">\.</span>\s*</h2>',
                      r'<span class="fv-eyebrow wow fadeInUp" style="display:inline-block; margin:0 auto 15px;">WHY FLOW VELLO</span><h2 class="wow fadeInUp" style="color:#111827; font-family:\'Rubik\', sans-serif; font-size:52px; font-weight:600; line-height:1.15; letter-spacing:-1.5px; max-width:850px; margin:0 auto 50px;">NO TEMPLATES. NO BUSYWORK. <br>JUST THE RIGHT SYSTEM<span style="color: #fb383b;">.</span></h2>',
                      html_updated, flags=re.DOTALL)
# Make the section header of Why Flow Vello centered
html_updated = html_updated.replace('<div class="col-lg-6 mb-5 mb-lg-0">', '<div class="col-lg-10 mx-auto text-center mb-5">')
html_updated = html_updated.replace('<p class="fv-lead mb-4">', '<p class="fv-lead mb-4 wow fadeInUp" style="margin: 0 auto 40px; max-width: 700px;">')

# 6. Process
html_updated = re.sub(r'<h2 class="fw-bold mb-4" style="[^"]*">How We Work</h2>',
                      r'<span class="fv-eyebrow wow fadeInUp" style="display:inline-block; margin:0 auto 15px; color:rgba(255,255,255,0.6);">OUR PROCESS</span><h2 class="wow fadeInUp" style="color: #ffffff; font-family: \'Rubik\', sans-serif; font-size: 52px; font-weight: 600; line-height: 1.15; letter-spacing: -1.5px; max-width: 850px; margin: 0 auto 30px;">From bottleneck to better system.</h2>',
                      html_updated, flags=re.DOTALL)
html_updated = html_updated.replace('<!-- PROCESS (HOW WE WORK) -->\n   <section class="fv-section fv-process" style="background:var(--fv-dark); color:#fff;">', '<!-- PROCESS (HOW WE WORK) -->\n   <section class="fv-section fv-process text-center" style="background:var(--fv-dark); color:#fff;">')
html_updated = html_updated.replace('<div class="col-lg-8">', '<div class="col-lg-10 mx-auto text-center">')

# 7. FAQ
html_updated = re.sub(r'<h2 class="mb-4" style="[^"]*">\s*Frequently asked questions\s*</h2>',
                      r'<span class="fv-eyebrow wow fadeInUp" style="display:inline-block; margin:0 auto 15px;">FAQ</span><h2 class="wow fadeInUp" style="color: #111827; font-family: \'Rubik\', sans-serif; font-size: 52px; font-weight: 600; line-height: 1.15; letter-spacing: -1.5px; max-width: 850px; margin: 0 auto 50px;">Frequently asked questions</h2>',
                      html_updated, flags=re.DOTALL)
html_updated = html_updated.replace('<!-- FAQ (MODERN) -->\n   <section class="fv-section fv-faq">', '<!-- FAQ (MODERN) -->\n   <section class="fv-section fv-faq text-center">')

# 8. CORE SERVICES header
html_updated = re.sub(r'<h2 style="[^"]*">\s*Core Capabilities\s*</h2>',
                      r'<span class="fv-eyebrow wow fadeInUp" style="display:inline-block; margin:0 auto 15px;">SERVICES</span><h2 class="wow fadeInUp" style="color: #111827; font-family: \'Rubik\', sans-serif; font-size: 52px; font-weight: 600; line-height: 1.15; letter-spacing: -1.5px; max-width: 850px; margin: 0 auto 30px;">Core Capabilities</h2>',
                      html_updated, flags=re.DOTALL)
html_updated = html_updated.replace('<div class="col-lg-5 mb-5 mb-lg-0 fv-service-intro">', '<div class="col-lg-10 mx-auto text-center mb-5 fv-service-intro">')

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_updated)

print("Homepage sections re-centered and scaled up.")
