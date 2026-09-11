import re

with open('c:/Users/my/Desktop/chatgpt/services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. FIX THE NAVBAR ACTIVE STATE
# The FAQ link currently has the 'active' class, remove it.
content = content.replace('<li class="nav-item active"><a class="nav-link" href="faq.html">FAQ</a></li>', '<li class="nav-item"><a class="nav-link" href="faq.html">FAQ</a></li>')
# Add active class to the services dropdown if it exists, or just ensure the current page is highlighted.
content = content.replace('<li class="nav-item dropdown">', '<li class="nav-item dropdown active">')


# 2. REBUILD THE DIRECTORY WITH HIGH-END STYLING (Dark Theme)
# We will use the service-slide-card layout wrapped in a normal grid.
new_directory_html = '''
<!-- MASTER SERVICES DIRECTORY -->
<section class="fv-services-presentation py-5" style="background-color: #111827;">
    <div class="container py-5">
        
        <!-- Dept 1: Development -->
        <div class="mb-5 pb-5">
            <div class="sec-header text-left mb-5">
               <h2 class="wow fadeInUp" style="color: #ffffff; font-size: 42px; font-weight: 600;">Development <span style="color: #fb383b;">Department</span></h2>
               <p class="wow fadeInUp" data-wow-delay="0.1s" style="color: rgba(255,255,255,0.7); font-size: 18px; max-width: 600px;">Engineering custom, scalable technical solutions.</p>
            </div>
            
            <div class="row">
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/web-applications.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-1 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fal fa-browser card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 01 )</span>
                            <div class="service-icon"><i class="fal fa-browser"></i></div>
                            <div class="service-text">
                                <h3>WEB APPLICATIONS</h3>
                                <p>Custom scalable web applications.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/web-based-games.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-2 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fal fa-gamepad card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 02 )</span>
                            <div class="service-icon"><i class="fal fa-gamepad"></i></div>
                            <div class="service-text">
                                <h3>WEB-BASED GAMES</h3>
                                <p>Interactive browser gaming experiences.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/wordpress-solutions.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-3 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fab fa-wordpress card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 03 )</span>
                            <div class="service-icon"><i class="fab fa-wordpress"></i></div>
                            <div class="service-text">
                                <h3>WORDPRESS SOLUTIONS</h3>
                                <p>Custom themes, plugins, and CMS buildouts.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/shopify-stores.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-4 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fab fa-shopify card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 04 )</span>
                            <div class="service-icon"><i class="fab fa-shopify"></i></div>
                            <div class="service-text">
                                <h3>SHOPIFY STORES</h3>
                                <p>E-commerce store design and optimization.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/wix-development.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-5 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fab fa-wix card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 05 )</span>
                            <div class="service-icon"><i class="fab fa-wix"></i></div>
                            <div class="service-text">
                                <h3>WIX DEVELOPMENT</h3>
                                <p>Fast, modern low-code web solutions.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/desktop-applications.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-6 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fal fa-desktop card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 06 )</span>
                            <div class="service-icon"><i class="fal fa-desktop"></i></div>
                            <div class="service-text">
                                <h3>DESKTOP APPLICATIONS</h3>
                                <p>Cross-platform desktop software.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
            </div>
        </div>

        <!-- Dept 2: Automation -->
        <div class="mb-5 pb-5">
            <div class="sec-header text-left mb-5">
               <h2 class="wow fadeInUp" style="color: #ffffff; font-size: 42px; font-weight: 600;">Automation <span style="color: #fb383b;">Department</span></h2>
               <p class="wow fadeInUp" data-wow-delay="0.1s" style="color: rgba(255,255,255,0.7); font-size: 18px; max-width: 600px;">Eliminating bottlenecks with intelligent systems.</p>
            </div>
            
            <div class="row">
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/ai-agents.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-1 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fal fa-robot card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 07 )</span>
                            <div class="service-icon"><i class="fal fa-robot"></i></div>
                            <div class="service-text">
                                <h3>AI AGENTS</h3>
                                <p>Autonomous task and customer workflow agents.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/custom-dashboards.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-2 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fal fa-chart-pie card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 08 )</span>
                            <div class="service-icon"><i class="fal fa-chart-pie"></i></div>
                            <div class="service-text">
                                <h3>CUSTOM DASHBOARDS</h3>
                                <p>Real-time operational data visualization.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/calling-agents.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-3 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fal fa-headset card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 09 )</span>
                            <div class="service-icon"><i class="fal fa-headset"></i></div>
                            <div class="service-text">
                                <h3>CALLING AGENTS</h3>
                                <p>AI-powered voice outreach and inbound calling.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/api-system-integration.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-4 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fal fa-plug card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 10 )</span>
                            <div class="service-icon"><i class="fal fa-plug"></i></div>
                            <div class="service-text">
                                <h3>API & INTEGRATION</h3>
                                <p>Seamless multi-platform data syncing.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/gohighlevel.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-5 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fal fa-funnel-dollar card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 11 )</span>
                            <div class="service-icon"><i class="fal fa-funnel-dollar"></i></div>
                            <div class="service-text">
                                <h3>GOHIGHLEVEL (GHL)</h3>
                                <p>Complete CRM automation and funnel setup.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
            </div>
        </div>

        <!-- Dept 3: Creative -->
        <div class="mb-5 pb-5">
            <div class="sec-header text-left mb-5">
               <h2 class="wow fadeInUp" style="color: #ffffff; font-size: 42px; font-weight: 600;">Creative <span style="color: #fb383b;">Development</span></h2>
               <p class="wow fadeInUp" data-wow-delay="0.1s" style="color: rgba(255,255,255,0.7); font-size: 18px; max-width: 600px;">High-impact visual identity and design.</p>
            </div>
            
            <div class="row">
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/graphic-design.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-1 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fal fa-pen-nib card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 12 )</span>
                            <div class="service-icon"><i class="fal fa-pen-nib"></i></div>
                            <div class="service-text">
                                <h3>GRAPHIC DESIGN</h3>
                                <p>Brand identity, social assets, and collateral.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/video-editing.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-2 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fal fa-video card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 13 )</span>
                            <div class="service-icon"><i class="fal fa-video"></i></div>
                            <div class="service-text">
                                <h3>VIDEO EDITING</h3>
                                <p>High-impact promotional and social media videos.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/social-media-design.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-3 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fal fa-share-alt card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 14 )</span>
                            <div class="service-icon"><i class="fal fa-share-alt"></i></div>
                            <div class="service-text">
                                <h3>SOCIAL MEDIA DESIGN</h3>
                                <p>Engaging feed graphics and ad creatives.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/3d-vfx.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-4 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fal fa-cubes card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 15 )</span>
                            <div class="service-icon"><i class="fal fa-cubes"></i></div>
                            <div class="service-text">
                                <h3>3D & VFX</h3>
                                <p>3D modeling, rendering, and visual effects.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/ui-ux-design.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-5 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fal fa-mobile-alt card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 16 )</span>
                            <div class="service-icon"><i class="fal fa-mobile-alt"></i></div>
                            <div class="service-text">
                                <h3>UI/UX DESIGN</h3>
                                <p>Modern web and mobile interface prototyping.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
            </div>
        </div>

        <!-- Dept 4: Sales & Marketing -->
        <div class="mb-5 pb-5">
            <div class="sec-header text-left mb-5">
               <h2 class="wow fadeInUp" style="color: #ffffff; font-size: 42px; font-weight: 600;">Sales & <span style="color: #fb383b;">Marketing</span></h2>
               <p class="wow fadeInUp" data-wow-delay="0.1s" style="color: rgba(255,255,255,0.7); font-size: 18px; max-width: 600px;">Data-driven growth and outbound strategies.</p>
            </div>
            
            <div class="row">
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/email-marketing.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-1 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fal fa-envelope-open-text card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 17 )</span>
                            <div class="service-icon"><i class="fal fa-envelope-open-text"></i></div>
                            <div class="service-text">
                                <h3>EMAIL MARKETING</h3>
                                <p>Targeted drip campaigns and lead nurturing.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/digital-marketing.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-2 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fal fa-bullhorn card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 18 )</span>
                            <div class="service-icon"><i class="fal fa-bullhorn"></i></div>
                            <div class="service-text">
                                <h3>DIGITAL MARKETING</h3>
                                <p>Omnichannel PPC, SEO, and paid growth.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/freelancing-platform-management.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-3 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fal fa-briefcase card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 19 )</span>
                            <div class="service-icon"><i class="fal fa-briefcase"></i></div>
                            <div class="service-text">
                                <h3>PLATFORM MANAGEMENT</h3>
                                <p>Upwork & Fiverr agency optimization.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <a href="services/linkedin-growth.html" class="d-block" style="text-decoration: none;">
                    <div class="service-slide-card card-grad-4 h-100" style="margin: 0; min-height: 280px;">
                        <i class="fab fa-linkedin-in card-watermark"></i>
                        <div class="card-content">
                            <span class="service-number">( 20 )</span>
                            <div class="service-icon"><i class="fab fa-linkedin-in"></i></div>
                            <div class="service-text">
                                <h3>LINKEDIN GROWTH</h3>
                                <p>B2B lead generation and personal branding.</p>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
            </div>
        </div>

    </div>
</section>
<!-- CLOSING CTA (SPLIT) -->
'''

# Swap out the garbage white background section I created earlier
content = re.sub(r'(?s)<!-- MASTER SERVICES DIRECTORY -->.*?<!-- CLOSING CTA \(SPLIT\) -->', new_directory_html, content)

# Change the hero background to match the dark theme and update text styling
hero_section = '''
<div class="col-lg-8 mx-auto text-center">
    <h1 class="wow fadeInUp" style="color: #ffffff; font-family: 'Rubik', sans-serif; font-size: 56px; font-weight: 600; letter-spacing: -1.5px; margin-bottom: 24px;">Our Complete <span style="color: #fb383b;">Service Catalog</span></h1>
    <p class="wow fadeInUp" data-wow-delay="0.1s" style="color: rgba(255,255,255,0.7); font-family: 'Rubik', sans-serif; font-size: 20px; line-height: 1.6; margin-bottom: 0;">Comprehensive solutions across Development, Automation, Creative, and Marketing to scale your business.</p>
</div>
'''

content = re.sub(r'(?s)<div class="col-lg-8 mx-auto text-center">.*?</div></div></div></section>', hero_section + '</div></div></section>', content)

with open('c:/Users/my/Desktop/chatgpt/services.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Professional dark theme directory applied successfully.")
