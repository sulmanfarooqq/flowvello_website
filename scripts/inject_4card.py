import re

file_path = 'c:/Users/my/Desktop/chatgpt/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the section containing the services
# Look for a section that has "Integrating with <strong" or "shadcn-grid"
# Let's write the new HTML
new_html = """
    <!-- TECHTOX MODERN SERVICES (4 CARD GRID) -->
    <section class="techtox-services-modern pt-5 pb-5" style="background-color: #f8f9fa;">
        <div class="container pt-4 pb-2">
           <div class="d-flex justify-content-between align-items-end mb-5 wow fadeInUp">
               <h2 style="font-family: 'Rubik', sans-serif; font-size: 52px; font-weight: 600; line-height: 1.15; letter-spacing: -1.5px; color: #000000; margin: 0;">
                  Our services
               </h2>
               <a href="services.html" class="d-none d-md-inline-flex align-items-center" style="color: #000000; font-weight: 600; text-decoration: none; font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px;">
                  DISCOVER OUR FULL CAPABILITIES <i class="fal fa-arrow-right ml-2"></i>
               </a>
           </div>
           
           <style>
               .techtox-cards-wrapper {
                   display: grid;
                   grid-template-columns: repeat(4, 1fr);
                   gap: 24px;
               }
               .techtox-card {
                   background-color: #ffffff;
                   border-radius: 16px;
                   overflow: hidden;
                   display: flex;
                   flex-direction: column;
                   min-height: 480px;
                   box-shadow: 0 4px 20px rgba(0,0,0,0.03);
                   transition: transform 0.3s ease, box-shadow 0.3s ease;
                   position: relative;
               }
               .techtox-card:hover {
                   transform: translateY(-5px);
                   box-shadow: 0 10px 30px rgba(0,0,0,0.08);
               }
               .techtox-card-content {
                   padding: 40px 30px;
                   z-index: 2;
                   flex-grow: 1;
               }
               .techtox-card h3 {
                   font-family: 'Rubik', sans-serif;
                   font-size: 32px;
                   font-weight: 600;
                   color: #000000;
                   margin-bottom: 20px;
                   line-height: 1.2;
                   letter-spacing: -0.5px;
               }
               .techtox-card p {
                   color: #4b5563;
                   font-size: 15px;
                   line-height: 1.6;
                   margin-bottom: 30px;
               }
               .techtox-card-link {
                   font-size: 13px;
                   font-weight: 600;
                   color: #000000;
                   text-transform: uppercase;
                   letter-spacing: 0.5px;
                   text-decoration: none;
                   display: inline-flex;
                   align-items: center;
               }
               .techtox-card-link i {
                   margin-left: 8px;
                   transition: transform 0.2s ease;
               }
               .techtox-card:hover .techtox-card-link i {
                   transform: translateX(4px);
               }
               .techtox-card-bg {
                   position: absolute;
                   bottom: 0;
                   left: 0;
                   width: 100%;
                   height: 200px;
                   background: linear-gradient(180deg, rgba(255,46,62,0) 0%, rgba(255,46,62,0.15) 100%);
                   z-index: 1;
                   border-radius: 0 0 16px 16px;
               }
               /* Abstract SVG background for each card */
               .card-bg-1 { background: url('data:image/svg+xml;utf8,<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><path fill="%23FF2E3E" fill-opacity="0.1" d="M0,50 Q25,25 50,50 T100,50 L100,100 L0,100 Z"/></svg>') no-repeat bottom center; background-size: cover; }
               .card-bg-2 { background: url('data:image/svg+xml;utf8,<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><path fill="%23FF2E3E" fill-opacity="0.1" d="M0,70 Q30,40 60,70 T100,60 L100,100 L0,100 Z"/></svg>') no-repeat bottom center; background-size: cover; }
               .card-bg-3 { background: url('data:image/svg+xml;utf8,<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><path fill="%23FF2E3E" fill-opacity="0.1" d="M0,60 Q20,80 50,60 T100,50 L100,100 L0,100 Z"/></svg>') no-repeat bottom center; background-size: cover; }
               .card-bg-4 { background: url('data:image/svg+xml;utf8,<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><path fill="%23FF2E3E" fill-opacity="0.1" d="M0,40 Q40,80 70,40 T100,50 L100,100 L0,100 Z"/></svg>') no-repeat bottom center; background-size: cover; }
               
               @media (max-width: 1199px) {
                   .techtox-cards-wrapper { grid-template-columns: repeat(2, 1fr); }
               }
               @media (max-width: 767px) {
                   .techtox-cards-wrapper { grid-template-columns: 1fr; }
                   .techtox-services-modern h2 { font-size: 40px !important; }
               }
           </style>

           <div class="techtox-cards-wrapper wow fadeInUp" data-wow-delay="0.2s">
               
               <!-- Card 1 -->
               <div class="techtox-card">
                   <div class="techtox-card-content">
                       <h3>Development<br>& Foundation</h3>
                       <p>We architect scalable custom software, high-performance web applications, and robust e-commerce platforms. This is the indestructible bedrock of your digital business.</p>
                       <a href="services.html" class="techtox-card-link">LEARN MORE <i class="fal fa-arrow-right"></i></a>
                   </div>
                   <div class="techtox-card-bg card-bg-1"></div>
               </div>

               <!-- Card 2 -->
               <div class="techtox-card">
                   <div class="techtox-card-content">
                       <h3>Creative &<br>Brand Identity</h3>
                       <p>Elite UI/UX prototyping, digital branding, and high-impact visual design. Establish absolute market authority with interfaces that convert instantly.</p>
                       <a href="services.html" class="techtox-card-link">LEARN MORE <i class="fal fa-arrow-right"></i></a>
                   </div>
                   <div class="techtox-card-bg card-bg-2"></div>
               </div>

               <!-- Card 3 -->
               <div class="techtox-card">
                   <div class="techtox-card-content">
                       <h3>Marketing<br>& Scaling</h3>
                       <p>Relentless omnichannel growth marketing, targeted B2B LinkedIn pipeline scaling, and SEO strategies to drive highly qualified enterprise leads.</p>
                       <a href="services.html" class="techtox-card-link">LEARN MORE <i class="fal fa-arrow-right"></i></a>
                   </div>
                   <div class="techtox-card-bg card-bg-3"></div>
               </div>

               <!-- Card 4 -->
               <div class="techtox-card">
                   <div class="techtox-card-content">
                       <h3>Autonomous<br>Operations</h3>
                       <p>Layer autonomous AI agents, API integrations, and smart CRM workflows over your business to eliminate manual labor and accelerate data processing.</p>
                       <a href="services.html" class="techtox-card-link">LEARN MORE <i class="fal fa-arrow-right"></i></a>
                   </div>
                   <div class="techtox-card-bg card-bg-4"></div>
               </div>

           </div>
           
           <div class="mt-4 text-center d-md-none wow fadeInUp">
               <a href="services.html" class="techtox-card-link" style="font-size: 16px;">
                  DISCOVER OUR FULL CAPABILITIES <i class="fal fa-arrow-right ml-2"></i>
               </a>
           </div>

        </div>
    </section>
"""

# Replace the old section
# We will find `<section class="fv-logo-cloud-modern` and replace everything until the next `</section>`
# Wait, the previous block was `shadcn-grid` which was inside `fv-logo-cloud-modern`.
# Let's just find the `fv-logo-cloud-modern` section and replace the whole thing.

# regex to match `<section class="fv-logo-cloud-modern ... </section>`
import re
new_content = re.sub(r'<section class="fv-logo-cloud-modern.*?</section>', new_html, content, flags=re.DOTALL)

if new_content == content:
    print("Could not find the section to replace.")
else:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully injected the new 4-card services section.")
