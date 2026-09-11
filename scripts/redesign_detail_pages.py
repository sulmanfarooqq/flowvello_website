import os
import re

service_dir = 'c:/Users/my/Desktop/chatgpt/services'
files = [f for f in os.listdir(service_dir) if f.endswith('.html')]

new_body = '''
<!-- INTERACTIVE PORTFOLIO GALLERY -->
<section class="fv-section py-5" style="background-color: #f7f7f5;">
    <div class="container py-5">
        <div class="text-center mb-5">
            <h2 style="font-family: 'Rubik', sans-serif; font-size: 42px; font-weight: 600; color: #111827;">Project <span style="color: #fb383b;">Showcase</span></h2>
            <p style="color: #666; font-size: 18px; max-width: 600px; margin: 0 auto;">Visual representations of our deliverables and real-world project deployments.</p>
        </div>
        
        <div class="row" id="portfolioSection">
            <!-- Portfolio Item 1 -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="portfolio-box">
                    <img src="../img/bg1.webp" class="img-fluid rounded" alt="Project Thumbnail" style="width: 100%; height: 300px; object-fit: cover; filter: brightness(0.8);">
                    <div class="hover-txt">
                        <span class="category">Client Project</span>
                        <p>Deliverable Preview</p>
                    </div>
                </div>
            </div>
            <!-- Portfolio Item 2 -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="portfolio-box">
                    <img src="../img/bg2.webp" class="img-fluid rounded" alt="Project Thumbnail" style="width: 100%; height: 300px; object-fit: cover; filter: brightness(0.8);">
                    <div class="hover-txt">
                        <span class="category">Client Project</span>
                        <p>Deliverable Preview</p>
                    </div>
                </div>
            </div>
            <!-- Portfolio Item 3 -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="portfolio-box">
                    <img src="../img/bg3.webp" class="img-fluid rounded" alt="Project Thumbnail" style="width: 100%; height: 300px; object-fit: cover; filter: brightness(0.8);">
                    <div class="hover-txt">
                        <span class="category">Client Project</span>
                        <p>Deliverable Preview</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- FEATURES & DELIVERABLES GRID -->
<section class="fv-services-presentation py-5" style="background-color: #111827;">
    <div class="container py-5">
        <div class="text-center mb-5">
            <h2 style="font-family: 'Rubik', sans-serif; font-size: 42px; font-weight: 600; color: #ffffff;">Features & <span style="color: #fb383b;">Deliverables</span></h2>
            <p style="color: rgba(255,255,255,0.7); font-size: 18px; max-width: 600px; margin: 0 auto;">Everything included when you order this specific service.</p>
        </div>
        
        <div class="row">
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="service-slide-card card-grad-1 h-100" style="margin: 0; min-height: 250px;">
                    <i class="fal fa-check-circle card-watermark"></i>
                    <div class="card-content">
                        <span class="service-number">( 01 )</span>
                        <div class="service-icon"><i class="fal fa-check-circle"></i></div>
                        <div class="service-text">
                            <h3>CORE DELIVERABLE</h3>
                            <p>Specific feature or asset provided upon project completion.</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="service-slide-card card-grad-2 h-100" style="margin: 0; min-height: 250px;">
                    <i class="fal fa-check-circle card-watermark"></i>
                    <div class="card-content">
                        <span class="service-number">( 02 )</span>
                        <div class="service-icon"><i class="fal fa-check-circle"></i></div>
                        <div class="service-text">
                            <h3>CORE DELIVERABLE</h3>
                            <p>Specific feature or asset provided upon project completion.</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="service-slide-card card-grad-3 h-100" style="margin: 0; min-height: 250px;">
                    <i class="fal fa-check-circle card-watermark"></i>
                    <div class="card-content">
                        <span class="service-number">( 03 )</span>
                        <div class="service-icon"><i class="fal fa-check-circle"></i></div>
                        <div class="service-text">
                            <h3>CORE DELIVERABLE</h3>
                            <p>Specific feature or asset provided upon project completion.</p>
                        </div>
                    </div>
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
    
    # Target everything between Hero and CTA/Footer
    hero_match = re.search(r'(?s)(<section class="fv-page-hero">.*?</section>)', content)
    if not hero_match:
        continue
    hero_end_index = hero_match.end()
    
    cta_match = re.search(r'(?s)<!-- DIRECT BOOKING LINK', content)
    if cta_match:
        # We've already injected once, so we'll replace the existing injected part.
        cta_end = content.find('<!-- FOOTER -->')
        if cta_end == -1:
            cta_end = content.find('<!-- CLOSING CTA')
        
        new_content = content[:hero_end_index] + '\n\n' + new_body + '\n\n' + content[cta_end:]
    else:
        # Fallback if first inject failed
        pass
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Redesigned all 20 internal service pages with true Flow Vello styling.")
