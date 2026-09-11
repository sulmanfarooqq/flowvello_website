# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/about.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_section = '''   <!-- 4 PILLARS GRID (REBUILT FEATURE 72) -->
   <section class="py-5" style="background-color: #ffffff; padding-top: 100px !important; padding-bottom: 100px !important;">
        <div class="container" style="max-width: 1200px;">
            <div class="d-flex flex-column" style="gap: 60px;">
                <!-- Header Block -->
                <div style="max-width: 500px;">
                    <h2 style="font-family:'Rubik', sans-serif; font-size: 42px; font-weight: 600; color: #111827; letter-spacing: -1.5px; margin-bottom: 16px; line-height: 1.1;">
                        Four Specialized Departments.
                    </h2>
                    <p style="color: #6b7280; font-size: 18px; font-family:'Rubik', sans-serif; line-height: 1.6; margin-bottom: 30px;">
                        Operating sequentially to build, launch, and scale your infrastructure. We don't rely on fragmented contractors; every department works under one unified standard.
                    </p>
                    <a href="contact.html" class="fv-dual-btn" style="display: inline-flex;">
                        <span class="fv-btn-pill">BOOK A DEMO</span>
                        <div class="fv-btn-circle">
                            <i class="fal fa-arrow-right arrow-main"></i>
                            <i class="fal fa-arrow-right arrow-hover"></i>
                        </div>
                    </a>
                </div>
                
                <!-- Grid Block -->
                <style>
                    .f72-grid { display: grid; gap: 32px; grid-template-columns: 1fr; }
                    @media (min-width: 768px) { .f72-grid { grid-template-columns: repeat(2, 1fr); } }
                    .f72-card { display: flex; flex-direction: column; overflow: hidden; border-radius: 12px; border: 1px solid #e5e7eb; background: #ffffff; transition: box-shadow 0.2s ease, transform 0.2s ease; }
                    .f72-card:hover { box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); transform: translateY(-2px); }
                    .f72-img-container { width: 100%; aspect-ratio: 16/9; background: #f8fafc; border-bottom: 1px solid #e5e7eb; overflow: hidden; }
                    .f72-img-container img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease; }
                    .f72-card:hover .f72-img-container img { transform: scale(1.05); }
                    .f72-content { padding: 32px; flex-grow: 1; }
                    .f72-title { font-family: 'Rubik', sans-serif; font-size: 22px; font-weight: 600; color: #111827; margin: 0 0 12px 0; letter-spacing: -0.5px; }
                    .f72-desc { font-family: 'Rubik', sans-serif; color: #6b7280; font-size: 16px; line-height: 1.6; margin: 0; }
                </style>

                <div class="f72-grid">
                    <!-- CREATIVE -->
                    <a href="services.html" class="f72-card" style="text-decoration: none;">
                        <div class="f72-img-container">
                            <img src="https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=800&q=80" alt="Creative Department" loading="lazy">
                        </div>
                        <div class="f72-content">
                            <h3 class="f72-title">01. Creative</h3>
                            <p class="f72-desc">We establish market dominance through elite UI/UX prototyping, cinematic video editing, and cohesive brand identity systems designed for high conversion.</p>
                        </div>
                    </a>
                    
                    <!-- DEVELOPMENT -->
                    <a href="services.html" class="f72-card" style="text-decoration: none;">
                        <div class="f72-img-container">
                            <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=800&q=80" alt="Development Department" loading="lazy">
                        </div>
                        <div class="f72-content">
                            <h3 class="f72-title">02. Development</h3>
                            <p class="f72-desc">We build sub-second, enterprise-grade architecture spanning headless e-commerce, custom web applications, and seamless system integrations.</p>
                        </div>
                    </a>
                    
                    <!-- MARKETING -->
                    <a href="services.html" class="f72-card" style="text-decoration: none;">
                        <div class="f72-img-container">
                            <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80" alt="Marketing Department" loading="lazy">
                        </div>
                        <div class="f72-content">
                            <h3 class="f72-title">03. Marketing</h3>
                            <p class="f72-desc">We drive aggressive revenue acquisition through omnichannel paid media, technical SEO, and data-driven outbound LinkedIn outreach.</p>
                        </div>
                    </a>
                    
                    <!-- AUTOMATION -->
                    <a href="services.html" class="f72-card" style="text-decoration: none;">
                        <div class="f72-img-container">
                            <img src="https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80" alt="Automation Department" loading="lazy">
                        </div>
                        <div class="f72-content">
                            <h3 class="f72-title">04. Automation</h3>
                            <p class="f72-desc">We scale your operations autonomously using proprietary AI agents, complex workflow automation, and real-time executive data dashboards.</p>
                        </div>
                    </a>
                </div>
            </div>
        </div>
   </section>'''

# Regex to find the current 4 PILLARS GRID section
# We're looking for <!-- 4 PILLARS GRID --> to </section>
new_html = re.sub(r'(?s)<!-- 4 PILLARS GRID -->.*?</section>', new_section, html)

with open('c:/Users/my/Desktop/chatgpt/about.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated 4 PILLARS GRID section successfully.")
