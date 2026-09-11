# -*- coding: utf-8 -*-
import re

# 1. FIX ABOUT.HTML
with open('c:/Users/my/Desktop/chatgpt/about.html', 'r', encoding='utf-8') as f:
    about = f.read()

about = about.replace('We build the systems that make businesses run better.', 'We are the growth partner that combines engineering, creative design, and data-driven marketing.')
about = about.replace('Solve the operational problem first.', 'Solve the business bottleneck first.')
about = about.replace('AUTOMATION FOR REAL BUSINESS OPERATIONS<span style="color:#fb383b;">.</span>', 'FULL-STACK DIGITAL GROWTH<span style="color:#fb383b;">.</span>')
about = about.replace('From operational bottlenecks to working systems.', 'From digital bottlenecks to scalable growth systems.')

about = re.sub(r'(?s)<section class="fv-industries-grid.*?</section>', '', about)
about = re.sub(r'(?s)<section class="fv-capabilities-section.*?</section>', '', about)

with open('c:/Users/my/Desktop/chatgpt/about.html', 'w', encoding='utf-8') as f:
    f.write(about)

# 2. FIX CASE-STUDIES.HTML
with open('c:/Users/my/Desktop/chatgpt/case-studies.html', 'r', encoding='utf-8') as f:
    cs = f.read()

cs = cs.replace('Engineered for operational impact.', 'Engineered for growth, scale, and digital impact.')

with open('c:/Users/my/Desktop/chatgpt/case-studies.html', 'w', encoding='utf-8') as f:
    f.write(cs)

# 3. FIX FAQ.HTML
with open('c:/Users/my/Desktop/chatgpt/faq.html', 'r', encoding='utf-8') as f:
    faq = f.read()

new_faqs = '''
         <!-- CATEGORY: General & Cross-Department -->
         <div class="mx-auto mb-3 wow fadeInUp" style="max-width: 800px;">
            <div class="fv-faq-item">
               <h3>What does a "full-service digital agency" mean for my business?</h3>
               <p>It means you no longer have to hire a separate dev shop, design agency, and marketing firm. We handle your complete digital lifecycle - from building your custom web app to automating your operations, designing your brand, and scaling your traffic through paid marketing.</p>
            </div>
         </div>
         
         <!-- CATEGORY: Development -->
         <div class="mx-auto mb-3 wow fadeInUp" style="max-width: 800px;">
            <div class="fv-faq-item">
               <h3>What tech stacks do you use for web development?</h3>
               <p>We build lightweight, scalable, and highly optimized applications. Depending on the scope, we utilize modern frameworks for custom apps, robust headless CMS setups, or enterprise platforms like Shopify and WordPress.</p>
            </div>
         </div>

         <!-- CATEGORY: Automation -->
         <div class="mx-auto mb-3 wow fadeInUp" style="max-width: 800px;">
            <div class="fv-faq-item">
               <h3>Will AI agents fully replace my human support team?</h3>
               <p>No. Our AI agents are designed to handle 80% of routine inquiries, data entry, and workflow routing. We architect explicit escalation paths so your human team only handles high-value, complex interactions.</p>
            </div>
         </div>

         <!-- CATEGORY: Creative -->
         <div class="mx-auto mb-3 wow fadeInUp" style="max-width: 800px;">
            <div class="fv-faq-item">
               <h3>Do you handle end-to-end UI/UX design before development?</h3>
               <p>Absolutely. Our Creative department prototypes every screen, user flow, and interaction state in Figma before a single line of code is written, ensuring you approve the exact aesthetic and UX beforehand.</p>
            </div>
         </div>
         
         <!-- CATEGORY: Marketing -->
         <div class="mx-auto mb-3 wow fadeInUp" style="max-width: 800px;">
            <div class="fv-faq-item">
               <h3>Do your marketing retainers include ad spend?</h3>
               <p>No, ad spend is always billed directly to your corporate accounts to ensure full transparency. Our retainers cover the strategy, campaign management, A/B testing, and creative asset production.</p>
            </div>
         </div>
'''

faq = re.sub(r'(?s)<!-- CATEGORY: General -->.*?<!-- CLOSING CTA \(SPLIT\)', new_faqs + '\n   </section>\n\n   <!-- CLOSING CTA (SPLIT)', faq)

with open('c:/Users/my/Desktop/chatgpt/faq.html', 'w', encoding='utf-8') as f:
    f.write(faq)

# 4. FIX CONTACT.HTML
with open('c:/Users/my/Desktop/chatgpt/contact.html', 'r', encoding='utf-8') as f:
    contact = f.read()

form_dropdown = '''
                           <div class="col-md-12 mb-3">
                              <select class="form-control" name="department" required style="height: 55px; border-radius: 8px; border: 1px solid #e5e7eb; background: #f9fafb; font-family: 'Rubik', sans-serif;">
                                 <option value="" disabled selected>What do you need help with?</option>
                                 <option value="Development">Web & App Development</option>
                                 <option value="Automation">AI & Workflow Automation</option>
                                 <option value="Creative">Creative, UI/UX & Design</option>
                                 <option value="Marketing">Digital Marketing & Growth</option>
                                 <option value="Multiple">Full-Stack Retainer (Multiple)</option>
                              </select>
                           </div>
'''

contact = re.sub(r'(<input type="email".*?</div>)', r'\1\n' + form_dropdown, contact)

with open('c:/Users/my/Desktop/chatgpt/contact.html', 'w', encoding='utf-8') as f:
    f.write(contact)

print("Deep rewrite completed.")
