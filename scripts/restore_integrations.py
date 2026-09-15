import re

file_path = 'c:/Users/my/Desktop/chatgpt/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

logo_cloud_html = """
    <!-- LOGO CLOUD (MODERN GRID) -->
    <section class="fv-logo-cloud-modern pt-5 pb-5" style="background-color: #ffffff;">
        <div class="container pt-4 pb-2">
           <h2 class="mb-5 text-center wow fadeInUp" style="font-family: 'Rubik', sans-serif; font-size: 52px; font-weight: 600; line-height: 1.15; letter-spacing: -1.5px; max-width: 850px; margin-left: auto; margin-right: auto; color: #000000;">
              Integrating with <strong style="color: #000000; font-weight: 600;">modern tech stacks</strong> for robust <strong style="color: #000000; font-weight: 600;">digital growth</strong>.
           </h2>
           
          <div class="logo-grid-container mx-auto wow fadeInUp" data-wow-delay="0.1s" style="max-width: 1000px; position: relative;">
               <div class="logo-grid">
                   <!-- Top Row -->
                  <div class="logo-grid-item bg-light border-right border-bottom relative-box">
                     <img src="https://cdn.worldvectorlogo.com/logos/salesforce-2.svg" alt="Salesforce">
                      <i class="fal fa-plus crosshair bottom-right d-none d-md-block"></i>
                   </div>
                  <div class="logo-grid-item bg-white border-right border-bottom relative-box">
                     <img src="https://upload.wikimedia.org/wikipedia/commons/0/0e/Shopify_logo_2018.svg" alt="Shopify">
                      <i class="fal fa-plus crosshair bottom-right d-none d-md-block"></i>
                   </div>
                  <div class="logo-grid-item bg-light border-right border-bottom relative-box">
                     <img src="https://upload.wikimedia.org/wikipedia/commons/3/33/Figma-logo.svg" alt="Figma">
                      <i class="fal fa-plus crosshair bottom-right d-none d-md-block"></i>
                   </div>
                  <div class="logo-grid-item bg-white border-bottom">
                      <img src="https://cdn.21st.dev/assets/mirror/2b/2bcdd4124223e3bf8e66bc08ce0ac32a6cc42ffe3584bbecfd377847176a188d.svg" alt="OpenAI">
                   </div>
    
                   <!-- Bottom Row -->
                  <div class="logo-grid-item bg-white border-right relative-box">
                     <img src="https://upload.wikimedia.org/wikipedia/commons/f/fd/Zapier_logo.svg" alt="Zapier">
                   </div>
                  <div class="logo-grid-item bg-light border-right relative-box">
                     <img src="https://cdn.worldvectorlogo.com/logos/hubspot.svg" alt="HubSpot">
                   </div>
                  <div class="logo-grid-item bg-white border-right relative-box">
                     <img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Stripe_Logo%2C_revised_2016.svg" alt="Stripe">
                   </div>
                  <div class="logo-grid-item bg-light">
                     <img src="https://cdn.worldvectorlogo.com/logos/aws-2.svg" alt="AWS">
                   </div>
                </div>
           </div>
        </div>
    </section>
"""

# The "foundation for enterprise scaling" section has class `bg-dark` or `techtox-dark-features` or id `features`
# Let's find it. From the previous `cat`, it has `class="shadcn-dark-cell"` inside it.
# Let's inject it right before `<section id="whyus"` or whatever section contains "The foundation for enterprise scaling"

content = re.sub(r'(<section[^>]*>\s*<div class="container">\s*<div class="row">\s*<div class="col-12 text-center">\s*<h6 class="text-uppercase[^>]*>WHY TECHTOX</h6>)', logo_cloud_html + r'\n\g<1>', content)
# If that didn't match, let's try finding the exact text "The foundation for enterprise scaling" and injecting before its parent section.

if logo_cloud_html not in content:
    idx = content.find('The foundation for enterprise scaling')
    if idx != -1:
        # Find the preceding <section> tag
        sec_idx = content.rfind('<section', 0, idx)
        if sec_idx != -1:
            content = content[:sec_idx] + logo_cloud_html + '\n' + content[sec_idx:]
            print("Injected via fallback text search.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Integrations section restored.")
