import re

with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the end of the services carousel section
# It looks like: <section class="fv-services-presentation py-5" id="services"> ... </section>
match = re.search(r'(?s)(<section class="fv-services-presentation py-5" id="services">.*?</section>)', content)

if match:
    services_html = match.group(1)
    
    # We want to inject a CTA button right before the closing </section>
    # Actually, the carousel itself is inside a container. We should append a centered button row at the bottom of the section.
    
    cta_button_html = '''
    <div class="container mt-5 text-center wow fadeInUp" data-wow-delay="0.3s">
        <a href="services.html" class="fv-dual-btn mx-auto">
            <span class="fv-btn-pill">EXPLORE ALL 20 SERVICES</span>
            <div class="fv-btn-circle">
                <i class="fal fa-arrow-right arrow-main"></i>
                <i class="fal fa-arrow-right arrow-hover"></i>
            </div>
        </a>
    </div>
'''
    
    # Insert right before the last closing div/section of the services block.
    # We can just replace the last '</section>' of that block.
    new_services_html = services_html.rsplit('</section>', 1)[0] + cta_button_html + '</section>'
    
    content = content.replace(services_html, new_services_html)
    
    with open('c:/Users/my/Desktop/chatgpt/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added Explore All Services button to index.html")
else:
    print("Could not find services section.")
