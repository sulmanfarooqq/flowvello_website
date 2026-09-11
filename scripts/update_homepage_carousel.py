import re

with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

carousel_match = re.search(r'(?s)(<div id="servicesCarousel" class="owl-carousel services-carousel owl-theme">)(.*?)(</div>\s*</div>\s*<div class="container mt-5 text-center wow fadeInUp")', content)

if carousel_match:
    prefix = carousel_match.group(1)
    suffix = carousel_match.group(3)
    
    new_items = '''
              <!-- Development Dept -->
              <div class="service-slide-card card-grad-1">
                 <i class="fal fa-browser card-watermark"></i>
                 <div class="card-content">
                    <span class="service-number">( 01 )</span>
                    <div class="service-icon"><i class="fal fa-browser"></i></div>
                    <div class="service-text">
                       <h3>WEB APPLICATIONS</h3>
                       <p>Custom scalable web applications engineered for performance.</p>
                    </div>
                 </div>
              </div>

              <div class="service-slide-card card-grad-2">
                 <i class="fab fa-wordpress card-watermark"></i>
                 <div class="card-content">
                    <span class="service-number">( 02 )</span>
                    <div class="service-icon"><i class="fab fa-wordpress"></i></div>
                    <div class="service-text">
                       <h3>WORDPRESS SOLUTIONS</h3>
                       <p>Custom themes, plugins, and full CMS buildouts.</p>
                    </div>
                 </div>
              </div>

              <div class="service-slide-card card-grad-3">
                 <i class="fab fa-shopify card-watermark"></i>
                 <div class="card-content">
                    <span class="service-number">( 03 )</span>
                    <div class="service-icon"><i class="fab fa-shopify"></i></div>
                    <div class="service-text">
                       <h3>SHOPIFY STORES</h3>
                       <p>High-converting E-commerce store design and optimization.</p>
                    </div>
                 </div>
              </div>

              <!-- Automation Dept -->
              <div class="service-slide-card card-grad-4">
                 <i class="fal fa-robot card-watermark"></i>
                 <div class="card-content">
                    <span class="service-number">( 04 )</span>
                    <div class="service-icon"><i class="fal fa-robot"></i></div>
                    <div class="service-text">
                       <h3>AI AGENTS</h3>
                       <p>Autonomous task execution and customer workflow agents.</p>
                    </div>
                 </div>
              </div>

              <div class="service-slide-card card-grad-5">
                 <i class="fal fa-chart-pie card-watermark"></i>
                 <div class="card-content">
                    <span class="service-number">( 05 )</span>
                    <div class="service-icon"><i class="fal fa-chart-pie"></i></div>
                    <div class="service-text">
                       <h3>CUSTOM DASHBOARDS</h3>
                       <p>Real-time operational data visualization and reporting.</p>
                    </div>
                 </div>
              </div>

              <div class="service-slide-card card-grad-6">
                 <i class="fal fa-funnel-dollar card-watermark"></i>
                 <div class="card-content">
                    <span class="service-number">( 06 )</span>
                    <div class="service-icon"><i class="fal fa-funnel-dollar"></i></div>
                    <div class="service-text">
                       <h3>GOHIGHLEVEL (GHL)</h3>
                       <p>Complete CRM automation and sales funnel setup.</p>
                    </div>
                 </div>
              </div>

              <!-- Creative Dept -->
              <div class="service-slide-card card-grad-1">
                 <i class="fal fa-mobile-alt card-watermark"></i>
                 <div class="card-content">
                    <span class="service-number">( 07 )</span>
                    <div class="service-icon"><i class="fal fa-mobile-alt"></i></div>
                    <div class="service-text">
                       <h3>UI/UX DESIGN</h3>
                       <p>Modern web and mobile user interface prototyping.</p>
                    </div>
                 </div>
              </div>

              <div class="service-slide-card card-grad-2">
                 <i class="fal fa-pen-nib card-watermark"></i>
                 <div class="card-content">
                    <span class="service-number">( 08 )</span>
                    <div class="service-icon"><i class="fal fa-pen-nib"></i></div>
                    <div class="service-text">
                       <h3>GRAPHIC DESIGN</h3>
                       <p>Brand identity, social assets, and premium collateral.</p>
                    </div>
                 </div>
              </div>

              <div class="service-slide-card card-grad-3">
                 <i class="fal fa-video card-watermark"></i>
                 <div class="card-content">
                    <span class="service-number">( 09 )</span>
                    <div class="service-icon"><i class="fal fa-video"></i></div>
                    <div class="service-text">
                       <h3>VIDEO EDITING</h3>
                       <p>High-impact promotional and social media video production.</p>
                    </div>
                 </div>
              </div>

              <!-- Sales Dept -->
              <div class="service-slide-card card-grad-4">
                 <i class="fal fa-bullhorn card-watermark"></i>
                 <div class="card-content">
                    <span class="service-number">( 10 )</span>
                    <div class="service-icon"><i class="fal fa-bullhorn"></i></div>
                    <div class="service-text">
                       <h3>DIGITAL MARKETING</h3>
                       <p>Omnichannel PPC, SEO, and paid growth campaigns.</p>
                    </div>
                 </div>
              </div>

              <div class="service-slide-card card-grad-5">
                 <i class="fal fa-envelope-open-text card-watermark"></i>
                 <div class="card-content">
                    <span class="service-number">( 11 )</span>
                    <div class="service-icon"><i class="fal fa-envelope-open-text"></i></div>
                    <div class="service-text">
                       <h3>EMAIL MARKETING</h3>
                       <p>Targeted drip campaigns and lead nurturing sequences.</p>
                    </div>
                 </div>
              </div>

              <div class="service-slide-card card-grad-6">
                 <i class="fab fa-linkedin-in card-watermark"></i>
                 <div class="card-content">
                    <span class="service-number">( 12 )</span>
                    <div class="service-icon"><i class="fab fa-linkedin-in"></i></div>
                    <div class="service-text">
                       <h3>LINKEDIN GROWTH</h3>
                       <p>B2B lead generation and executive personal branding.</p>
                    </div>
                 </div>
              </div>
'''
    new_content = content[:carousel_match.start(2)] + '\n' + new_items + '\n            ' + content[carousel_match.start(3):]
    
    with open('c:/Users/my/Desktop/chatgpt/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully replaced homepage carousel with 12 diverse services.")
else:
    print("Could not find carousel.")
