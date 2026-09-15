import re

file_path = 'c:/Users/my/Desktop/chatgpt/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove techtox-services-modern completely
content = re.sub(r'<!-- TECHTOX MODERN SERVICES.*?</section>', '', content, flags=re.DOTALL | re.IGNORECASE)

# 2. Re-write the servicesCarousel contents
new_carousel_items = """
              <!-- Department 1: Development -->
              <div class="service-slide-card card-grad-1">
                 <i class="fal fa-browser card-watermark"></i>
                 <div class="card-content">
                    <span class="service-number">( 01 )</span>
                    <div class="service-icon"><i class="fal fa-browser"></i></div>
                    <div class="service-text">
                       <h3>DEVELOPMENT</h3>
                       <p>Scalable custom software, web apps, and digital platforms.</p>
                    </div>
                 </div>
              </div>

              <!-- Department 2: Creative -->
              <div class="service-slide-card card-grad-2">
                 <i class="fal fa-pen-nib card-watermark"></i>
                 <div class="card-content">
                    <span class="service-number">( 02 )</span>
                    <div class="service-icon"><i class="fal fa-pen-nib"></i></div>
                    <div class="service-text">
                       <h3>CREATIVE</h3>
                       <p>High-impact visual identity, branding, and UI/UX design.</p>
                    </div>
                 </div>
              </div>

              <!-- Department 3: Marketing -->
              <div class="service-slide-card card-grad-3">
                 <i class="fal fa-bullhorn card-watermark"></i>
                 <div class="card-content">
                    <span class="service-number">( 03 )</span>
                    <div class="service-icon"><i class="fal fa-bullhorn"></i></div>
                    <div class="service-text">
                       <h3>MARKETING</h3>
                       <p>Data-driven traffic, B2B lead generation, and omnichannel growth.</p>
                    </div>
                 </div>
              </div>

              <!-- Department 4: Automation -->
              <div class="service-slide-card card-grad-4">
                 <i class="fal fa-robot card-watermark"></i>
                 <div class="card-content">
                    <span class="service-number">( 04 )</span>
                    <div class="service-icon"><i class="fal fa-robot"></i></div>
                    <div class="service-text">
                       <h3>AUTOMATION</h3>
                       <p>Autonomous AI agents and seamless API workflow integrations.</p>
                    </div>
                 </div>
              </div>
"""

# Find the carousel and replace its contents
content = re.sub(
    r'(<div id="servicesCarousel"[^>]*>).*?(</div>\s*</div>\s*</div>\s*</section>)', 
    r'\g<1>' + new_carousel_items + r'\g<2>', 
    content, 
    flags=re.DOTALL
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Carousel updated successfully.")
