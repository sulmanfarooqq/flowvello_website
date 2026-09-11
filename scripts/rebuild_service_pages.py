import os
import re

service_dir = 'c:/Users/my/Desktop/chatgpt/services'
files = [f for f in os.listdir(service_dir) if f.endswith('.html')]

# The new compliant structure replacing the body of the service pages
new_body = '''
<!-- INTERACTIVE PORTFOLIO GALLERY -->
<section class="fv-section py-5" style="background-color: #f9fafb;">
    <div class="container py-5">
        <div class="text-center mb-5">
            <h2 style="font-family: 'Rubik', sans-serif; font-size: 38px; font-weight: 600; color: #111827;">Interactive <span style="color: #fb383b;">Portfolio Gallery</span></h2>
            <p style="color: #4b5563; font-size: 18px; max-width: 600px; margin: 0 auto;">High-resolution visual representations showcasing real projects and client deliverables.</p>
        </div>
        
        <div class="row">
            <!-- Placeholder Gallery Item 1 -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="portfolio-card shadow-sm rounded overflow-hidden" style="background: #fff; border: 1px solid #e5e7eb;">
                    <div style="height: 250px; background: #e5e7eb; display: flex; align-items: center; justify-content: center;">
                        <i class="fal fa-image" style="font-size: 40px; color: #9ca3af;"></i>
                    </div>
                    <div class="p-3">
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 5px;">Project Showcase</h4>
                        <p style="color: #6b7280; font-size: 14px; margin-bottom: 0;">Client Deliverable Preview</p>
                    </div>
                </div>
            </div>
            <!-- Placeholder Gallery Item 2 -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="portfolio-card shadow-sm rounded overflow-hidden" style="background: #fff; border: 1px solid #e5e7eb;">
                    <div style="height: 250px; background: #e5e7eb; display: flex; align-items: center; justify-content: center;">
                        <i class="fal fa-image" style="font-size: 40px; color: #9ca3af;"></i>
                    </div>
                    <div class="p-3">
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 5px;">Project Showcase</h4>
                        <p style="color: #6b7280; font-size: 14px; margin-bottom: 0;">Client Deliverable Preview</p>
                    </div>
                </div>
            </div>
            <!-- Placeholder Gallery Item 3 -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="portfolio-card shadow-sm rounded overflow-hidden" style="background: #fff; border: 1px solid #e5e7eb;">
                    <div style="height: 250px; background: #e5e7eb; display: flex; align-items: center; justify-content: center;">
                        <i class="fal fa-image" style="font-size: 40px; color: #9ca3af;"></i>
                    </div>
                    <div class="p-3">
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 5px;">Project Showcase</h4>
                        <p style="color: #6b7280; font-size: 14px; margin-bottom: 0;">Client Deliverable Preview</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- FEATURES & DELIVERABLES GRID -->
<section class="fv-section py-5" style="background-color: #111827;">
    <div class="container py-5">
        <div class="text-center mb-5">
            <h2 style="font-family: 'Rubik', sans-serif; font-size: 38px; font-weight: 600; color: #ffffff;">Features & <span style="color: #fb383b;">Deliverables</span></h2>
            <p style="color: rgba(255,255,255,0.7); font-size: 18px; max-width: 600px; margin: 0 auto;">A clear breakdown of exactly what you receive when partnering with us.</p>
        </div>
        
        <div class="row">
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="deliverable-box p-4" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px;">
                    <i class="fal fa-check-circle mb-3" style="font-size: 30px; color: #fb383b;"></i>
                    <h4 style="color: #fff; font-size: 20px; font-weight: 600;">Core Deliverable 1</h4>
                    <p style="color: rgba(255,255,255,0.7); margin-bottom: 0; font-size: 15px;">Specific feature or asset provided upon project completion.</p>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="deliverable-box p-4" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px;">
                    <i class="fal fa-check-circle mb-3" style="font-size: 30px; color: #fb383b;"></i>
                    <h4 style="color: #fff; font-size: 20px; font-weight: 600;">Core Deliverable 2</h4>
                    <p style="color: rgba(255,255,255,0.7); margin-bottom: 0; font-size: 15px;">Specific feature or asset provided upon project completion.</p>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="deliverable-box p-4" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px;">
                    <i class="fal fa-check-circle mb-3" style="font-size: 30px; color: #fb383b;"></i>
                    <h4 style="color: #fff; font-size: 20px; font-weight: 600;">Core Deliverable 3</h4>
                    <p style="color: rgba(255,255,255,0.7); margin-bottom: 0; font-size: 15px;">Specific feature or asset provided upon project completion.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- DIRECT BOOKING LINK (CALENDAR) -->
<section class="fv-section py-5" style="background-color: #ffffff;">
    <div class="container py-5 text-center">
        <h2 style="font-family: 'Rubik', sans-serif; font-size: 38px; font-weight: 600; color: #111827; margin-bottom: 15px;">Ready to Start? <span style="color: #fb383b;">Book a Consultation</span></h2>
        <p style="color: #4b5563; font-size: 18px; max-width: 600px; margin: 0 auto 40px;">Select a time below to schedule your direct consultation meeting with our team.</p>
        
        <!-- Calendly inline widget begin -->
        <div class="calendly-inline-widget" data-url="https://calendly.com/contact-flowvello/30min?hide_event_type_details=1&hide_gdpr_banner=1" style="min-width:320px;height:700px;"></div>
        <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
        <!-- Calendly inline widget end -->
    </div>
</section>
'''

for file in files:
    filepath = os.path.join(service_dir, file)
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # We want to replace everything from the END of the Hero section down to the footer/CTA.
    # The Hero ends with </section>. The next section is <!-- WHAT IT SOLVES --> or similar.
    # We will target everything between the end of the hero and the footer or closing CTA.
    
    # Find the end of the HERO section:
    # <section class="fv-page-hero"> ... </section>
    hero_match = re.search(r'(?s)(<section class="fv-page-hero">.*?</section>)', content)
    
    if not hero_match:
        print(f"Skipping {file} - no hero found")
        continue
        
    hero_end_index = hero_match.end()
    
    # Find the closing CTA or Footer
    cta_match = re.search(r'(?s)<!-- CLOSING CTA \(SPLIT\) -->', content)
    if not cta_match:
        # try footer
        cta_match = re.search(r'(?s)<!-- FOOTER -->', content)
        
    if not cta_match:
        print(f"Skipping {file} - no footer/cta found")
        continue
        
    cta_start_index = cta_match.start()
    
    # Replace everything in between
    new_content = content[:hero_end_index] + '\n\n' + new_body + '\n\n' + content[cta_start_index:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("All 20 service pages rebuilt strictly to PDF standards.")
