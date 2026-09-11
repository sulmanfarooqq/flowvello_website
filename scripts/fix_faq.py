import re

with open('c:/Users/my/Desktop/chatgpt/faq.html', 'r', encoding='utf-8', errors='replace') as f:
    faq = f.read()

# I completely broke the FAQ structure earlier.
# The correct structure uses an accordion:
# <div class="fv-faq-item">
#    <div class="fv-faq-header">
#       <h3>Question</h3>
#       <i class="fal fa-angle-down"></i>
#    </div>
#    <div class="fv-faq-content">
#       <p>Answer</p>
#    </div>
# </div>

new_faqs = '''
         <!-- CATEGORY: General & Cross-Department -->
         <div class="mx-auto mb-3 wow fadeInUp" style="max-width: 800px;">
            <div class="fv-faq-item">
               <div class="fv-faq-header">
                  <h3>What does a "full-service digital agency" mean for my business?</h3>
                  <i class="fal fa-angle-down"></i>
               </div>
               <div class="fv-faq-content">
                  <p>It means you no longer have to hire a separate dev shop, design agency, and marketing firm. We handle your complete digital lifecycle - from building your custom web app to automating your operations, designing your brand, and scaling your traffic through paid marketing.</p>
               </div>
            </div>
         </div>
         
         <!-- CATEGORY: Development -->
         <div class="mx-auto mb-3 wow fadeInUp" style="max-width: 800px;">
            <div class="fv-faq-item">
               <div class="fv-faq-header">
                  <h3>What tech stacks do you use for web development?</h3>
                  <i class="fal fa-angle-down"></i>
               </div>
               <div class="fv-faq-content">
                  <p>We build lightweight, scalable, and highly optimized applications. Depending on the scope, we utilize modern frameworks for custom apps, robust headless CMS setups, or enterprise platforms like Shopify and WordPress.</p>
               </div>
            </div>
         </div>

         <!-- CATEGORY: Automation -->
         <div class="mx-auto mb-3 wow fadeInUp" style="max-width: 800px;">
            <div class="fv-faq-item">
               <div class="fv-faq-header">
                  <h3>Will AI agents fully replace my human support team?</h3>
                  <i class="fal fa-angle-down"></i>
               </div>
               <div class="fv-faq-content">
                  <p>No. Our AI agents are designed to handle 80% of routine inquiries, data entry, and workflow routing. We architect explicit escalation paths so your human team only handles high-value, complex interactions.</p>
               </div>
            </div>
         </div>

         <!-- CATEGORY: Creative -->
         <div class="mx-auto mb-3 wow fadeInUp" style="max-width: 800px;">
            <div class="fv-faq-item">
               <div class="fv-faq-header">
                  <h3>Do you handle end-to-end UI/UX design before development?</h3>
                  <i class="fal fa-angle-down"></i>
               </div>
               <div class="fv-faq-content">
                  <p>Absolutely. Our Creative department prototypes every screen, user flow, and interaction state in Figma before a single line of code is written, ensuring you approve the exact aesthetic and UX beforehand.</p>
               </div>
            </div>
         </div>
         
         <!-- CATEGORY: Marketing -->
         <div class="mx-auto mb-3 wow fadeInUp" style="max-width: 800px;">
            <div class="fv-faq-item">
               <div class="fv-faq-header">
                  <h3>Do your marketing retainers include ad spend?</h3>
                  <i class="fal fa-angle-down"></i>
               </div>
               <div class="fv-faq-content">
                  <p>No, ad spend is always billed directly to your corporate accounts to ensure full transparency. Our retainers cover the strategy, campaign management, A/B testing, and creative asset production.</p>
               </div>
            </div>
         </div>
'''

# Find everything between "Can't find what you're looking for?" and the CLOSING CTA.
# Let's target the exact block we injected earlier.
faq = re.sub(r'(?s)<!-- CATEGORY: General & Cross-Department -->.*?<!-- CLOSING CTA \(SPLIT\)', new_faqs + '\n   </section>\n\n   <!-- CLOSING CTA (SPLIT)', faq)

with open('c:/Users/my/Desktop/chatgpt/faq.html', 'w', encoding='utf-8') as f:
    f.write(faq)

print("FAQ accordion structure fixed.")
