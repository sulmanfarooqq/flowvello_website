import os
import re

source = 'c:/Users/my/Desktop/chatgpt/faq.html'
dest = 'c:/Users/my/Desktop/chatgpt/services.html'

with open(source, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace title
content = re.sub(r'<title>.*?</title>', '<title>All Services | Flow Vello</title>', content)

# Remove the specific FAQ content sections
# Find the hero text and replace it
content = re.sub(r'(?s)<div class="col-lg-8 mx-auto text-center">.*?</div>\s*</div>\s*</div>\s*</section>', '''
<div class="col-lg-8 mx-auto text-center">
    <h1 style="color: #111827; font-family: 'Rubik', sans-serif; font-size: 52px; font-weight: 600; letter-spacing: -1.5px; margin-bottom: 24px;">Our Complete <span style="color: #fb383b;">Service Catalog</span></h1>
    <p style="color: #4b5563; font-family: 'Rubik', sans-serif; font-size: 20px; line-height: 1.6; margin-bottom: 0;">Comprehensive solutions across Development, Automation, Creative, and Marketing to scale your business.</p>
</div></div></div></section>
''', content)

# Remove everything between the hero section and the CTA split / footer
# Hero ends with </section>. The next section is FAQ.
# Let's just rip out the FAQ section.
content = re.sub(r'(?s)<!-- FAQ SECTION -->.*?<!-- CLOSING CTA \(SPLIT\) -->', '''
<!-- MASTER SERVICES DIRECTORY -->
<section class="py-5" style="background: #f9fafb;">
    <div class="container py-5">
        
        <!-- Dept 1: Development -->
        <div class="mb-5">
            <h2 class="mb-4" style="font-family: 'Rubik', sans-serif; font-weight: 600; color: #111827; border-bottom: 2px solid #e5e7eb; padding-bottom: 10px;">Development Department</h2>
            <div class="row">
                <div class="col-md-4 mb-4"><a href="services/web-applications.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">Web Applications</h4><p class="text-muted mb-0">Custom scalable web applications.</p></a></div>
                <div class="col-md-4 mb-4"><a href="services/web-based-games.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">Web-Based Games</h4><p class="text-muted mb-0">Interactive browser gaming experiences.</p></a></div>
                <div class="col-md-4 mb-4"><a href="services/wordpress-solutions.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">WordPress Solutions</h4><p class="text-muted mb-0">Custom themes, plugins, and CMS.</p></a></div>
                <div class="col-md-4 mb-4"><a href="services/shopify-stores.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">Shopify Stores</h4><p class="text-muted mb-0">E-commerce store design and optimization.</p></a></div>
                <div class="col-md-4 mb-4"><a href="services/wix-development.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">Wix.com Development</h4><p class="text-muted mb-0">Fast, modern low-code web solutions.</p></a></div>
                <div class="col-md-4 mb-4"><a href="services/desktop-applications.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">Desktop Applications</h4><p class="text-muted mb-0">Cross-platform desktop software.</p></a></div>
            </div>
        </div>

        <!-- Dept 2: Automation -->
        <div class="mb-5">
            <h2 class="mb-4" style="font-family: 'Rubik', sans-serif; font-weight: 600; color: #111827; border-bottom: 2px solid #e5e7eb; padding-bottom: 10px;">Automation Department</h2>
            <div class="row">
                <div class="col-md-4 mb-4"><a href="services/ai-agents.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">AI Agents</h4><p class="text-muted mb-0">Autonomous task and customer workflow agents.</p></a></div>
                <div class="col-md-4 mb-4"><a href="services/custom-dashboards.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">Custom Dashboards</h4><p class="text-muted mb-0">Real-time operational data visualization.</p></a></div>
                <div class="col-md-4 mb-4"><a href="services/calling-agents.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">Calling Agents</h4><p class="text-muted mb-0">AI-powered voice outreach and inbound calling.</p></a></div>
                <div class="col-md-4 mb-4"><a href="services/api-system-integration.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">API & Integration</h4><p class="text-muted mb-0">Seamless multi-platform data syncing.</p></a></div>
                <div class="col-md-4 mb-4"><a href="services/gohighlevel.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">GoHighLevel (GHL)</h4><p class="text-muted mb-0">Complete CRM automation and funnel setup.</p></a></div>
            </div>
        </div>

        <!-- Dept 3: Creative -->
        <div class="mb-5">
            <h2 class="mb-4" style="font-family: 'Rubik', sans-serif; font-weight: 600; color: #111827; border-bottom: 2px solid #e5e7eb; padding-bottom: 10px;">Creative Development</h2>
            <div class="row">
                <div class="col-md-4 mb-4"><a href="services/graphic-design.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">Graphic Design</h4><p class="text-muted mb-0">Brand identity, social assets, and collateral.</p></a></div>
                <div class="col-md-4 mb-4"><a href="services/video-editing.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">Video Editing</h4><p class="text-muted mb-0">High-impact promotional and social media videos.</p></a></div>
                <div class="col-md-4 mb-4"><a href="services/social-media-design.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">Social Media Design</h4><p class="text-muted mb-0">Engaging feed graphics and ad creatives.</p></a></div>
                <div class="col-md-4 mb-4"><a href="services/3d-vfx.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">3D & VFX</h4><p class="text-muted mb-0">3D modeling, rendering, and visual effects.</p></a></div>
                <div class="col-md-4 mb-4"><a href="services/ui-ux-design.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">UI/UX Design</h4><p class="text-muted mb-0">Modern web and mobile interface prototyping.</p></a></div>
            </div>
        </div>

        <!-- Dept 4: Sales & Marketing -->
        <div class="mb-5">
            <h2 class="mb-4" style="font-family: 'Rubik', sans-serif; font-weight: 600; color: #111827; border-bottom: 2px solid #e5e7eb; padding-bottom: 10px;">Sales & Marketing</h2>
            <div class="row">
                <div class="col-md-4 mb-4"><a href="services/email-marketing.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">Email Marketing</h4><p class="text-muted mb-0">Targeted drip campaigns and lead nurturing.</p></a></div>
                <div class="col-md-4 mb-4"><a href="services/digital-marketing.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">Digital Marketing</h4><p class="text-muted mb-0">Omnichannel PPC, SEO, and paid growth.</p></a></div>
                <div class="col-md-4 mb-4"><a href="services/freelancing-platform-management.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">Platform Management</h4><p class="text-muted mb-0">Upwork & Fiverr agency optimization.</p></a></div>
                <div class="col-md-4 mb-4"><a href="services/linkedin-growth.html" class="d-block p-4 bg-white rounded shadow-sm text-decoration-none" style="border: 1px solid #e5e7eb; transition: 0.3s;"><h4 style="color: #fb383b; font-size: 20px; font-weight: 600;">LinkedIn Growth</h4><p class="text-muted mb-0">B2B lead generation and personal branding.</p></a></div>
            </div>
        </div>

    </div>
</section>
<!-- CLOSING CTA (SPLIT) -->''', content)

with open(dest, 'w', encoding='utf-8') as f:
    f.write(content)

print("Created services.html directory page.")
