import re

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

cta_pattern = r'<section class="fv-about-cta">.*?</section>'
new_cta = """<!-- CLOSING CTA (SPLIT) -->
   <section class="fv-cta-split py-5" id="contactArea" style="position: relative; overflow: hidden;">
      <img src="img/cta_bg_2.webp" alt="Abstract Background" loading="lazy" class="wow fadeIn" data-wow-duration="1.5s" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0;">
      <div style="position:absolute; inset:0; background: linear-gradient(90deg, rgba(17,24,39,0.95) 0%, rgba(17,24,39,0.7) 100%); z-index:0;"></div>
      
      <div class="container" style="position:relative; z-index:1; padding-top: 100px; padding-bottom: 100px;">
         <div class="row align-items-center">
            
            <div class="col-lg-6 mb-5 mb-lg-0 pr-lg-5 wow fadeInLeft" data-wow-delay="0.1s">
               <h2 class="fw-bold mb-4" style="color: #ffffff; font-family: 'Rubik', sans-serif; font-size: 56px; line-height: 1.1; letter-spacing: -1px;">
                  Ready to work with Flow Vello?
               </h2>
               <p style="color: #d1d5db; font-family: 'Rubik', sans-serif; font-size: 18px; line-height: 1.6; max-width: 500px; margin-bottom: 40px;">
                  Book a free consultation and let us show you where automation, AI or custom software can create the biggest operational improvement for your business.
               </p>
               <a href="contact.html" class="fv-dual-btn">
                  <span class="fv-btn-pill">BOOK A FREE CONSULTATION</span>
                  <div class="fv-btn-circle">
                     <i class="fal fa-arrow-right arrow-main"></i>
                     <i class="fal fa-arrow-right arrow-hover"></i>
                  </div>
               </a>
            </div>

            <div class="col-lg-5 offset-lg-1 wow fadeInRight" data-wow-delay="0.2s">
               <ul class="cta-check-list list-unstyled m-0">
                  <li class="d-flex align-items-center mb-4 pb-2">
                     <i class="fal fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Rubik', sans-serif; font-size: 20px; font-weight: 500;">Custom AI Agents</span>
                  </li>
                  <li class="d-flex align-items-center mb-4 pb-2">
                     <i class="fal fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Rubik', sans-serif; font-size: 20px; font-weight: 500;">Business-first Architecture</span>
                  </li>
                  <li class="d-flex align-items-center mb-4 pb-2">
                     <i class="fal fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Rubik', sans-serif; font-size: 20px; font-weight: 500;">Seamless Integrations</span>
                  </li>
                  <li class="d-flex align-items-center">
                     <i class="fal fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Rubik', sans-serif; font-size: 20px; font-weight: 500;">Measurable ROI</span>
                  </li>
               </ul>
            </div>
            
         </div>
      </div>
   </section>"""

html = re.sub(cta_pattern, new_cta, html, flags=re.DOTALL)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("about CTA replaced.")
