# -*- coding: utf-8 -*-
import os
import glob
import re

html_template = '''
<!-- SHADCN PORTFOLIO GALLERY -->
<section class="py-5" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
    <div class="container">
        <div class="mb-5 d-flex flex-column align-items-start" style="gap: 12px;">
            <div style="display: inline-flex; align-items: center; border-radius: 9999px; background-color: #111827; color: #ffffff; padding: 6px 16px; font-size: 13px; font-weight: 600; font-family: 'Rubik', sans-serif; letter-spacing: 1px; text-transform: uppercase;">
                Deliverables
            </div>
            <h2 style="font-family:'Rubik', sans-serif; font-size: 42px; font-weight: 500; color: #111827; letter-spacing: -1.5px; margin: 0; line-height: 1.1;">
                Project Showcase
            </h2>
            <p style="color: #6b7280; font-size: 18px; font-family:'Rubik', sans-serif; margin: 0; max-width: 600px; line-height: 1.6;">
                Visual representations of our enterprise deliverables and real-world project deployments.
            </p>
        </div>
        
        <div style="display: grid; gap: 32px; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
            <div style="border-radius: 12px; overflow: hidden; border: 1px solid #e5e7eb; background: #f8fafc;">
                <img src="../img/bg1.webp" alt="Project 1" style="width: 100%; height: 280px; object-fit: cover; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            </div>
            <div style="border-radius: 12px; overflow: hidden; border: 1px solid #e5e7eb; background: #f8fafc;">
                <img src="../img/bg2.webp" alt="Project 2" style="width: 100%; height: 280px; object-fit: cover; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            </div>
            <div style="border-radius: 12px; overflow: hidden; border: 1px solid #e5e7eb; background: #f8fafc;">
                <img src="../img/bg3.webp" alt="Project 3" style="width: 100%; height: 280px; object-fit: cover; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            </div>
        </div>
    </div>
</section>

<!-- SHADCN DARK BENTO GRID (FEATURES) -->
<section class="py-5" style="background-color: #0a0a0a; padding-top: 80px !important; padding-bottom: 80px !important;">
    <div class="container" style="max-width: 1000px;">
        <div class="text-center mb-5 pb-2 mx-auto" style="max-width: 700px;">
            <span style="color: #fb383b; font-family: 'Rubik', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px; display: inline-block;">INCLUDED IN SCOPE</span>
            <h2 style="font-family:'Rubik', sans-serif; font-size: 42px; font-weight: 500; color: #ffffff; letter-spacing: -1px; margin-bottom: 20px; line-height: 1.15;">
                Features & Deliverables
            </h2>
            <p style="color: #a1a1aa; font-size: 16px; font-family:'Rubik', sans-serif; margin: 0; line-height: 1.6;">
                Everything engineered, tested, and deployed when you integrate this specific service into your infrastructure.
            </p>
        </div>

        <style>
            .feature-dark-grid { display: grid; grid-template-columns: 1fr; border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; overflow: hidden; }
            .feature-dark-cell { padding: 40px; border-bottom: 1px solid rgba(255,255,255,0.1); background-color: transparent; transition: background-color 0.2s ease; }
            .feature-dark-cell:hover { background-color: rgba(255,255,255,0.02); }
            @media (min-width: 768px) { .feature-dark-grid { grid-template-columns: repeat(2, 1fr); } .feature-dark-cell { border-right: 1px solid rgba(255,255,255,0.1); } .feature-dark-cell:nth-child(2n) { border-right: none; } .feature-dark-cell:nth-last-child(-n+2) { border-bottom: none; } }
            @media (min-width: 1024px) { .feature-dark-grid { grid-template-columns: repeat(3, 1fr); } .feature-dark-cell:nth-child(2n) { border-right: 1px solid rgba(255,255,255,0.1); } .feature-dark-cell:nth-child(3n) { border-right: none; } .feature-dark-cell:nth-last-child(-n+3) { border-bottom: none; } }
            .fd-icon { font-size: 18px; color: #ffffff; margin-right: 12px; }
            .fd-title { font-family: 'Rubik', sans-serif; font-size: 16px; font-weight: 500; color: #ffffff; margin: 0; }
            .fd-desc { font-family: 'Rubik', sans-serif; color: #a1a1aa; font-size: 14px; line-height: 1.6; margin: 12px 0 0 0; }
        </style>

        <div class="feature-dark-grid">
            <div class="feature-dark-cell">
                <div class="d-flex align-items-center"><div class="fd-icon"><i class="fal fa-layer-group"></i></div><h3 class="fd-title">Custom Architecture</h3></div>
                <p class="fd-desc">Tailored frameworks built precisely for your operational bottlenecks without generic template bloat.</p>
            </div>
            <div class="feature-dark-cell">
                <div class="d-flex align-items-center"><div class="fd-icon"><i class="fal fa-code-branch"></i></div><h3 class="fd-title">API Synchronization</h3></div>
                <p class="fd-desc">Seamlessly wired into your existing CRM, database, and marketing stack for fluid data transfer.</p>
            </div>
            <div class="feature-dark-cell">
                <div class="d-flex align-items-center"><div class="fd-icon"><i class="fal fa-shield-check"></i></div><h3 class="fd-title">Enterprise Security</h3></div>
                <p class="fd-desc">Rigorous data protection, strict auth protocols, and secure cloud deployment standards.</p>
            </div>
            <div class="feature-dark-cell">
                <div class="d-flex align-items-center"><div class="fd-icon"><i class="fal fa-bolt"></i></div><h3 class="fd-title">Speed Optimization</h3></div>
                <p class="fd-desc">Stripped of unnecessary code to ensure sub-second response times and elite performance.</p>
            </div>
            <div class="feature-dark-cell">
                <div class="d-flex align-items-center"><div class="fd-icon"><i class="fal fa-users-cog"></i></div><h3 class="fd-title">Human Fallback</h3></div>
                <p class="fd-desc">Intelligent escalation paths designed to hand off processes to your team before failure.</p>
            </div>
            <div class="feature-dark-cell">
                <div class="d-flex align-items-center"><div class="fd-icon"><i class="fal fa-box-open"></i></div><h3 class="fd-title">Full Handover</h3></div>
                <p class="fd-desc">You own the system. Complete documentation, codebase handover, and administrative access.</p>
            </div>
        </div>
    </div>
</section>

<!-- DIRECT BOOKING LINK -->
<section class="py-5" style="background-color: #ffffff; padding-top: 80px !important;">
    <div class="container text-center">
        <div class="mb-5 mx-auto" style="max-width: 600px;">
            <h2 style="font-family: 'Rubik', sans-serif; font-size: 38px; font-weight: 600; color: #111827; letter-spacing: -1px; margin-bottom: 15px;">
                Ready to Start? <span style="color: #fb383b;">Book a Consultation</span>
            </h2>
            <p style="color: #6b7280; font-size: 18px; margin: 0 auto;">Select a time below to schedule your direct consultation meeting with our engineering team.</p>
        </div>
        <!-- Calendly inline widget begin -->
        <div class="calendly-inline-widget" data-url="https://calendly.com/contact-flowvello/30min?hide_event_type_details=1&hide_gdpr_banner=1" style="min-width:320px;height:700px;"></div>
        <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
        <!-- Calendly inline widget end -->
    </div>
</section>
'''

files = glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html')
count = 0

for file_path in files:
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        html = f.read()
    
    # We want to keep everything up to the END of <section class="fv-page-hero">...</section>
    hero_match = re.search(r'(?s)(.*?</section>)', html)
    
    # We want to keep everything from <!-- FOOTER --> to the end
    footer_match = re.search(r'(?s)(<!-- FOOTER -->.*)', html)
    
    # If the file has a different footer tag, try <footer
    if not footer_match:
        footer_match = re.search(r'(?s)(<footer.*)', html)
        
    if hero_match and footer_match:
        hero_content = hero_match.group(1)
        # However, .*?</section> matches the FIRST </section> which is indeed the hero's closing tag.
        
        # Build the new file
        new_html = hero_content + '\n\n' + html_template + '\n\n' + footer_match.group(1)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
            
        count += 1
    else:
        print(f"Skipped {os.path.basename(file_path)} (Regex failed)")

print(f"Successfully redesigned {count} service detail pages!")
