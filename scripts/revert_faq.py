# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/faq.html', 'r', encoding='utf-8', errors='replace') as f:
    faq = f.read()

new_faqs = '''
         <!-- CATEGORY: Development -->
         <div class="mx-auto mb-3 wow fadeInUp" style="max-width: 800px;">
            <p style="font-family: 'Rubik', sans-serif; font-size: 12px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: #fb383b; margin-bottom: 4px;">Development</p>
         </div>
         <div class="mx-auto fv-faq-modern-accordion" style="max-width: 800px; margin-bottom: 56px;">
            <div class="fv-faq-item fv-faq-modern-item wow fadeInUp" data-wow-delay="0.05s">
               <div class="fv-faq-header fv-faq-modern-header">
                  <h3>What tech stacks do you use for web development?</h3>
                  <i class="fal fa-chevron-down"></i>
               </div>
               <div class="fv-faq-content fv-faq-modern-content">
                  <p>We build lightweight, scalable, and highly optimized applications. Depending on the scope, we utilize modern frameworks for custom web apps, robust headless CMS setups, or enterprise platforms like Shopify and WordPress.</p>
               </div>
            </div>
            <div class="fv-faq-item fv-faq-modern-item wow fadeInUp" data-wow-delay="0.1s">
               <div class="fv-faq-header fv-faq-modern-header">
                  <h3>How long does a typical application build take?</h3>
                  <i class="fal fa-chevron-down"></i>
               </div>
               <div class="fv-faq-content fv-faq-modern-content">
                  <p>Standard builds typically span 4-8 weeks from discovery to deployment. Complex custom portals or massive e-commerce migrations can take 3-4 months. We provide an exact timeline during the scoping phase.</p>
               </div>
            </div>
         </div>

         <!-- CATEGORY: Automation -->
         <div class="mx-auto mb-3 wow fadeInUp" style="max-width: 800px;">
            <p style="font-family: 'Rubik', sans-serif; font-size: 12px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: #fb383b; margin-bottom: 4px;">Automation</p>
         </div>
         <div class="mx-auto fv-faq-modern-accordion" style="max-width: 800px; margin-bottom: 56px;">
            <div class="fv-faq-item fv-faq-modern-item wow fadeInUp" data-wow-delay="0.05s">
               <div class="fv-faq-header fv-faq-modern-header">
                  <h3>Will AI agents fully replace my human team?</h3>
                  <i class="fal fa-chevron-down"></i>
               </div>
               <div class="fv-faq-content fv-faq-modern-content">
                  <p>No. Our AI agents are designed to handle 80% of routine inquiries, data entry, and workflow routing. We architect explicit escalation paths so your human team only handles high-value, complex interactions.</p>
               </div>
            </div>
            <div class="fv-faq-item fv-faq-modern-item wow fadeInUp" data-wow-delay="0.1s">
               <div class="fv-faq-header fv-faq-modern-header">
                  <h3>Is our company data secure with your integrations?</h3>
                  <i class="fal fa-chevron-down"></i>
               </div>
               <div class="fv-faq-content fv-faq-modern-content">
                  <p>Yes. We use enterprise-grade APIs where data is never used to train public models. We implement strict access controls and isolated vector databases to ensure full compliance and privacy.</p>
               </div>
            </div>
         </div>

         <!-- CATEGORY: Creative -->
         <div class="mx-auto mb-3 wow fadeInUp" style="max-width: 800px;">
            <p style="font-family: 'Rubik', sans-serif; font-size: 12px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: #fb383b; margin-bottom: 4px;">Creative</p>
         </div>
         <div class="mx-auto fv-faq-modern-accordion" style="max-width: 800px; margin-bottom: 56px;">
            <div class="fv-faq-item fv-faq-modern-item wow fadeInUp" data-wow-delay="0.05s">
               <div class="fv-faq-header fv-faq-modern-header">
                  <h3>Do you handle end-to-end UI/UX design before development?</h3>
                  <i class="fal fa-chevron-down"></i>
               </div>
               <div class="fv-faq-content fv-faq-modern-content">
                  <p>Absolutely. Our Creative department prototypes every screen, user flow, and interaction state in Figma before a single line of code is written, ensuring you approve the exact aesthetic and UX beforehand.</p>
               </div>
            </div>
            <div class="fv-faq-item fv-faq-modern-item wow fadeInUp" data-wow-delay="0.1s">
               <div class="fv-faq-header fv-faq-modern-header">
                  <h3>What is included in a branding package?</h3>
                  <i class="fal fa-chevron-down"></i>
               </div>
               <div class="fv-faq-content fv-faq-modern-content">
                  <p>Full brand identity systems, logo design, typography scales, color palettes, and component libraries. We ensure your brand looks professional, cohesive, and enterprise-ready across all digital touchpoints.</p>
               </div>
            </div>
         </div>

         <!-- CATEGORY: Sales & Marketing -->
         <div class="mx-auto mb-3 wow fadeInUp" style="max-width: 800px;">
            <p style="font-family: 'Rubik', sans-serif; font-size: 12px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: #fb383b; margin-bottom: 4px;">Sales & Marketing</p>
         </div>
         <div class="mx-auto fv-faq-modern-accordion" style="max-width: 800px; margin-bottom: 56px;">
            <div class="fv-faq-item fv-faq-modern-item wow fadeInUp" data-wow-delay="0.05s">
               <div class="fv-faq-header fv-faq-modern-header">
                  <h3>Do your marketing retainers include ad spend?</h3>
                  <i class="fal fa-chevron-down"></i>
               </div>
               <div class="fv-faq-content fv-faq-modern-content">
                  <p>No, ad spend is always billed directly to your corporate accounts to ensure full transparency. Our retainers exclusively cover strategy, campaign management, A/B testing, and creative asset production.</p>
               </div>
            </div>
            <div class="fv-faq-item fv-faq-modern-item wow fadeInUp" data-wow-delay="0.1s">
               <div class="fv-faq-header fv-faq-modern-header">
                  <h3>Can you scale our LinkedIn lead generation?</h3>
                  <i class="fal fa-chevron-down"></i>
               </div>
               <div class="fv-faq-content fv-faq-modern-content">
                  <p>Yes. We build robust B2B outreach campaigns, optimize executive profiles, and craft highly targeted messaging sequences that convert connections into qualified booked meetings.</p>
               </div>
            </div>
         </div>
'''

# We need to wipe whatever I injected last time and replace it with this.
# The area to replace is between:
# Can't find what you're looking for? <a href="contact.html"... Contact our team directly.</a>
#               </p>
#            </div>
#
# AND
#
#    </section>
#
#    <!-- CLOSING CTA (SPLIT) -->

match = re.search(r'(?s)(Contact our team directly\.</a>\s*</p>\s*</div>)(.*?)(</section>\s*<!-- CLOSING CTA \(SPLIT\))', faq)
if match:
    new_html = faq[:match.end(1)] + '\n' + new_faqs + '\n   ' + faq[match.start(3):]
    with open('c:/Users/my/Desktop/chatgpt/faq.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Fixed FAQ!")
else:
    print("Regex failed to find bounds.")
