# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract NAV
nav_match = re.search(r'(?s)(.*?)(<section class="fv-page-hero">)', html)
if not nav_match:
    print("Failed to find nav")
    exit()
nav_content = nav_match.group(1)

# Extract CTA and Footer
cta_match = re.search(r'(?s)(<section class="fv-cta-split[^>]*>.*)', html)
if not cta_match:
    print("Failed to find cta")
    exit()
cta_and_footer = cta_match.group(1)

middle = '''
   <!-- HERO SECTION -->
   <section class="fv-page-hero" style="background-color: #f8fafc; padding: 120px 0 80px 0; border-bottom: 1px solid #e5e7eb;">
        <div class="container text-center">
           <span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s" style="color:#fb383b; letter-spacing:2px; font-weight: 700;">ABOUT FLOW VELLO</span>
           <h1 class="wow fadeInUp" data-wow-delay="0.2s" style="font-family:'Rubik', sans-serif; font-weight:600; font-size: 56px; letter-spacing:-1.5px; color: #111827; max-width: 900px; margin: 15px auto;">
              One Unified Growth Engine.
           </h1>
           <p class="fv-lead wow fadeInUp" data-wow-delay="0.3s" style="font-family: 'Rubik', sans-serif; font-size: 20px; color: #6b7280; max-width: 700px; margin: 20px auto 0;">
              We replaced the fragmented agency model with four interconnected departments engineered to scale your business.
           </p>
        </div>
   </section>

   <!-- PIPELINE EXPLANATION -->
   <section class="py-5" style="background-color: #ffffff; padding-top: 100px !important; padding-bottom: 100px !important;">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6 mb-5 mb-lg-0 wow fadeInLeft">
                    <span style="color: #fb383b; font-family: 'Rubik', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px; display: inline-block;">THE FLOW VELLO PIPELINE</span>
                    <h2 style="font-family:'Rubik', sans-serif; font-size: 48px; font-weight: 500; color: #111827; letter-spacing: -1.5px; margin-bottom: 24px; line-height: 1.1;">
                        Stop hiring disconnected teams.
                    </h2>
                    <p style="color: #6b7280; font-size: 18px; font-family:'Rubik', sans-serif; line-height: 1.6; margin-bottom: 20px;">
                        Most companies scale by hiring a design agency for their brand, a dev shop for their app, a marketing firm for their traffic, and a consultant for their operations. The result is bloated costs, broken communication, and systems that refuse to talk to each other.
                    </p>
                    <p style="color: #6b7280; font-size: 18px; font-family:'Rubik', sans-serif; line-height: 1.6;">
                        We built Flow Vello to be the single source of truth for your digital growth. A specialized pipeline where Creative, Development, Marketing, and Automation departments operate under one roof, sharing the same data, the same codebase, and the same aggressive revenue goals.
                    </p>
                </div>
                <div class="col-lg-5 offset-lg-1 wow fadeInRight">
                    <img src="img/minimal_workspace.webp" alt="Flow Vello Pipeline" class="img-fluid rounded" style="border: 1px solid #e5e7eb; box-shadow: 0 20px 40px rgba(0,0,0,0.08);">
                </div>
            </div>
        </div>
   </section>

   <!-- 4 PILLARS GRID -->
   <section class="py-5" style="background-color: #f9fafb; border-top: 1px solid #e5e7eb; border-bottom: 1px solid #e5e7eb; padding-top: 100px !important; padding-bottom: 100px !important;">
        <div class="container">
            <div class="text-center mb-5 pb-3">
                <h2 style="font-family:'Rubik', sans-serif; font-size: 42px; font-weight: 500; color: #111827; letter-spacing: -1.5px; margin: 0; line-height: 1.1;">
                    Four Specialized Departments.
                </h2>
                <p style="color: #6b7280; font-size: 18px; font-family:'Rubik', sans-serif; max-width: 600px; margin: 15px auto 0; line-height: 1.6;">
                    Operating sequentially to build, launch, and scale your infrastructure.
                </p>
            </div>
            
            <style>
                .feature-light-grid { display: grid; gap: 24px; grid-template-columns: 1fr; }
                @media (min-width: 768px) { .feature-light-grid { grid-template-columns: repeat(2, 1fr); } }
                .feature-light-card { background: #ffffff; padding: 40px; border-radius: 12px; border: 1px solid #e5e7eb; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); transition: box-shadow 0.2s ease, transform 0.2s ease; display: flex; flex-direction: column; height: 100%; }
                .feature-light-card:hover { box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); transform: translateY(-2px); }
                .fl-icon { font-size: 24px; color: #fb383b; margin-bottom: 20px; }
                .fl-title { font-family: 'Rubik', sans-serif; font-size: 24px; font-weight: 600; color: #111827; margin: 0 0 12px 0; letter-spacing: -0.5px; }
                .fl-desc { font-family: 'Rubik', sans-serif; color: #6b7280; font-size: 16px; line-height: 1.6; margin: 0 0 20px 0; flex-grow: 1; }
                .fl-link { font-family: 'Rubik', sans-serif; font-size: 14px; font-weight: 600; color: #111827; text-transform: uppercase; letter-spacing: 1px; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; transition: color 0.2s; }
                .fl-link:hover { color: #fb383b; text-decoration: none; }
            </style>

            <div class="feature-light-grid">
                <!-- CREATIVE -->
                <div class="feature-light-card wow fadeInUp" data-wow-delay="0.1s">
                    <div class="fl-icon"><i class="fal fa-palette"></i></div>
                    <h3 class="fl-title">01. Creative</h3>
                    <p class="fl-desc">We establish market dominance through elite UI/UX prototyping, cinematic video editing, and cohesive brand identity systems designed for high conversion.</p>
                    <a href="services.html" class="fl-link">View Creative Services <i class="fal fa-arrow-right"></i></a>
                </div>
                
                <!-- DEVELOPMENT -->
                <div class="feature-light-card wow fadeInUp" data-wow-delay="0.2s">
                    <div class="fl-icon"><i class="fal fa-code-branch"></i></div>
                    <h3 class="fl-title">02. Development</h3>
                    <p class="fl-desc">We build sub-second, enterprise-grade architecture spanning headless e-commerce, custom web applications, and seamless system integrations.</p>
                    <a href="services.html" class="fl-link">View Development Services <i class="fal fa-arrow-right"></i></a>
                </div>
                
                <!-- MARKETING -->
                <div class="feature-light-card wow fadeInUp" data-wow-delay="0.3s">
                    <div class="fl-icon"><i class="fal fa-bullseye-pointer"></i></div>
                    <h3 class="fl-title">03. Marketing</h3>
                    <p class="fl-desc">We drive aggressive revenue acquisition through omnichannel paid media, technical SEO, and data-driven outbound LinkedIn outreach.</p>
                    <a href="services.html" class="fl-link">View Marketing Services <i class="fal fa-arrow-right"></i></a>
                </div>
                
                <!-- AUTOMATION -->
                <div class="feature-light-card wow fadeInUp" data-wow-delay="0.4s">
                    <div class="fl-icon"><i class="fal fa-robot"></i></div>
                    <h3 class="fl-title">04. Automation</h3>
                    <p class="fl-desc">We scale your operations autonomously using proprietary AI agents, complex workflow automation, and real-time executive data dashboards.</p>
                    <a href="services.html" class="fl-link">View Automation Services <i class="fal fa-arrow-right"></i></a>
                </div>
            </div>
        </div>
   </section>

   <!-- OPERATIONAL STANDARDS (DARK) -->
   <section class="py-5" style="background-color: #0a0a0a; padding-top: 100px !important; padding-bottom: 100px !important;">
        <div class="container text-center">
            <span style="color: #fb383b; font-family: 'Rubik', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px; display: inline-block;">OUR STANDARDS</span>
            <h2 style="font-family:'Rubik', sans-serif; font-size: 42px; font-weight: 500; color: #ffffff; letter-spacing: -1.5px; margin-bottom: 60px; line-height: 1.1;">
                We don't hold your data hostage.
            </h2>
            
            <div class="row text-left">
                <div class="col-md-4 mb-4 mb-md-0 wow fadeInUp" data-wow-delay="0.1s">
                    <i class="fal fa-shield-check mb-4" style="font-size: 32px; color: #fb383b;"></i>
                    <h4 style="color: #ffffff; font-family: 'Rubik', sans-serif; font-size: 20px; font-weight: 500; margin-bottom: 15px;">Full IP Handover</h4>
                    <p style="color: #a1a1aa; font-family: 'Rubik', sans-serif; font-size: 16px; line-height: 1.6; margin: 0;">You own the code, the creative assets, and the administrative access to every system we build. No hidden retainer locks.</p>
                </div>
                <div class="col-md-4 mb-4 mb-md-0 wow fadeInUp" data-wow-delay="0.2s">
                    <i class="fal fa-tachometer-fast mb-4" style="font-size: 32px; color: #fb383b;"></i>
                    <h4 style="color: #ffffff; font-family: 'Rubik', sans-serif; font-size: 20px; font-weight: 500; margin-bottom: 15px;">Elite Performance</h4>
                    <p style="color: #a1a1aa; font-family: 'Rubik', sans-serif; font-size: 16px; line-height: 1.6; margin: 0;">We build without template bloat. Every system is engineered for sub-second load times and 90+ Lighthouse scores.</p>
                </div>
                <div class="col-md-4 wow fadeInUp" data-wow-delay="0.3s">
                    <i class="fal fa-user-lock mb-4" style="font-size: 32px; color: #fb383b;"></i>
                    <h4 style="color: #ffffff; font-family: 'Rubik', sans-serif; font-size: 20px; font-weight: 500; margin-bottom: 15px;">Enterprise Security</h4>
                    <p style="color: #a1a1aa; font-family: 'Rubik', sans-serif; font-size: 16px; line-height: 1.6; margin: 0;">Rigorous data protection, strict auth protocols, and secure cloud deployment standards baked into every line of code.</p>
                </div>
            </div>
        </div>
   </section>
'''

new_html = nav_content + '\n' + middle + '\n' + cta_and_footer

with open('c:/Users/my/Desktop/chatgpt/about.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("About page overhauled successfully.")
