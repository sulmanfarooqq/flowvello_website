# -*- coding: utf-8 -*-
import re
import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def make_centered(text):
    if "homeSection" in text or "CLOSING CTA" in text or "NAV" in text or "FOOTER" in text:
        return text
    
    # Make headings massive and centered
    text = re.sub(r'(<h2[^>]*style="[^"]*)font-size:\s*\d+px;', r'\g<1>font-size: 52px; line-height: 1.15; letter-spacing: -1.5px; max-width: 850px; margin-left: auto; margin-right: auto; text-align: center; ', text)
    text = re.sub(r'(<p[^>]*style="[^"]*)max-width:\s*\d+px;', r'\g<1>max-width: 700px; margin-left: auto; margin-right: auto; text-align: center; ', text)
    
    # Center align eyebrow labels
    text = re.sub(r'class="fv-eyebrow"', r'class="fv-eyebrow" style="display:inline-block; margin-left:auto; margin-right:auto; text-align: center;"', text)
    
    # If a section row has text-left, keep text-left for inner items but center the section header
    # Let's just wrap h2 and p in a center div if they aren't already
    
    return text

html_updated = html

# Replace explicit strings to ensure the massive editorial look
# 1. Partner with Us
html_updated = re.sub(r'<h2 class="mb-5 text-center" style="[^"]*">', 
                      r'<h2 class="mb-5 text-center wow fadeInUp" style="font-family: \'Rubik\', sans-serif; font-size: 52px; font-weight: 600; line-height: 1.15; letter-spacing: -1.5px; max-width: 850px; margin-left: auto; margin-right: auto; color: #111827;">', 
                      html_updated)

# 2. Who We Help
html_updated = re.sub(r'<h2>Who We Help & Why</h2>', 
                      r'<span class="fv-eyebrow wow fadeInUp" style="display:inline-block; margin:0 auto 15px;">WHO WE HELP</span><h2 class="wow fadeInUp" style="color: #111827; font-family: \'Rubik\', sans-serif; font-size: 52px; font-weight: 600; line-height: 1.15; letter-spacing: -1.5px; max-width: 850px; margin: 0 auto 30px;">Partner with Flow Vello to scale without chaos</h2>', 
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
html_updated = re.sub(r'<h2 class="fw-bold" style="[^"]*">\s*NO TEMPLATES. NO BUSYWORK. <br>JUST THE RIGHT SYSTEM<span style="color: #fb383b;">\.</span>\s*</h2>',
                      r'<span class="fv-eyebrow wow fadeInUp" style="display:inline-block; margin:0 auto 15px;">WHY FLOW VELLO</span><h2 class="wow fadeInUp" style="color:#111827; font-family:\'Rubik\', sans-serif; font-size:52px; font-weight:600; line-height:1.15; letter-spacing:-1.5px; max-width:850px; margin:0 auto 50px;">NO TEMPLATES. NO BUSYWORK. <br>JUST THE RIGHT SYSTEM<span style="color: #fb383b;">.</span></h2>',
                      html_updated, flags=re.DOTALL)

# 6. Process
html_updated = re.sub(r'<h2 class="fw-bold mb-4" style="[^"]*">How We Work</h2>',
                      r'<span class="fv-eyebrow wow fadeInUp" style="display:inline-block; margin:0 auto 15px; color:rgba(255,255,255,0.6);">OUR PROCESS</span><h2 class="wow fadeInUp" style="color: #ffffff; font-family: \'Rubik\', sans-serif; font-size: 52px; font-weight: 600; line-height: 1.15; letter-spacing: -1.5px; max-width: 850px; margin: 0 auto 30px;">From bottleneck to better system.</h2>',
                      html_updated, flags=re.DOTALL)

# 7. FAQ
html_updated = re.sub(r'<h2 class="mb-4" style="[^"]*">\s*Frequently asked questions\s*</h2>',
                      r'<span class="fv-eyebrow wow fadeInUp" style="display:inline-block; margin:0 auto 15px;">FAQ</span><h2 class="wow fadeInUp" style="color: #111827; font-family: \'Rubik\', sans-serif; font-size: 52px; font-weight: 600; line-height: 1.15; letter-spacing: -1.5px; max-width: 850px; margin: 0 auto 50px;">Frequently asked questions</h2>',
                      html_updated, flags=re.DOTALL)

# Ensure sections with .col-lg-8 (which usually hold the headers) have text-center and mx-auto
html_updated = re.sub(r'<div class="col-lg-8(?! mx-auto)(.*?)">', r'<div class="col-lg-8 mx-auto text-center\1">', html_updated)
# And col-lg-7
html_updated = re.sub(r'<div class="col-lg-7(?! mx-auto)(.*?)">', r'<div class="col-lg-8 mx-auto text-center\1">', html_updated)
# And col-lg-6
html_updated = re.sub(r'<div class="col-lg-6(?! mx-auto)(.*?)">', r'<div class="col-lg-8 mx-auto text-center\1">', html_updated)
# Wait, replacing col-lg-6 with col-lg-8 mx-auto text-center will ruin split layouts like the "PARTNER WITH US" section.
# Let me undo that and be more precise. Let's just do it on the specific header containers.
