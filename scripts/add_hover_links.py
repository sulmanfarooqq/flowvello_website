import re

file_path = 'c:/Users/my/Desktop/chatgpt/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# CSS to inject before the carousel
css_injection = """
<style>
.service-slide-card { text-decoration: none !important; display: block; cursor: pointer; }
.service-hover-link {
    margin-top: 20px;
    font-size: 12px;
    font-weight: 600;
    color: #FF2E3E;
    text-transform: uppercase;
    letter-spacing: 1px;
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
}
.service-hover-link i { margin-left: 8px; transition: transform 0.3s ease; }
.service-slide-card:hover .service-hover-link { opacity: 1; transform: translateY(0); }
.service-slide-card:hover .service-hover-link i { transform: translateX(5px); }
</style>
"""

# Only inject CSS if not already there
if '.service-hover-link' not in content:
    content = content.replace('<div id="servicesCarousel"', css_injection + '\n<div id="servicesCarousel"')

# Replacement for Development
content = re.sub(
    r'<div class="service-slide-card card-grad-1">(.*?)<p>Scalable custom software, web apps, and digital platforms.</p>\s*</div>\s*</div>\s*</div>',
    r'<a href="services.html#development" class="service-slide-card card-grad-1">\1<p>Scalable custom software, web apps, and digital platforms.</p><div class="service-hover-link"><span>View all services</span> <i class="fal fa-arrow-right"></i></div></div></div></a>',
    content,
    flags=re.DOTALL
)

# Replacement for Creative
content = re.sub(
    r'<div class="service-slide-card card-grad-2">(.*?)<p>High-impact visual identity, branding, and UI/UX design.</p>\s*</div>\s*</div>\s*</div>',
    r'<a href="services.html#creative" class="service-slide-card card-grad-2">\1<p>High-impact visual identity, branding, and UI/UX design.</p><div class="service-hover-link"><span>View all services</span> <i class="fal fa-arrow-right"></i></div></div></div></a>',
    content,
    flags=re.DOTALL
)

# Replacement for Marketing
content = re.sub(
    r'<div class="service-slide-card card-grad-3">(.*?)<p>Data-driven traffic, B2B lead generation, and omnichannel growth.</p>\s*</div>\s*</div>\s*</div>',
    r'<a href="services.html#marketing" class="service-slide-card card-grad-3">\1<p>Data-driven traffic, B2B lead generation, and omnichannel growth.</p><div class="service-hover-link"><span>View all services</span> <i class="fal fa-arrow-right"></i></div></div></div></a>',
    content,
    flags=re.DOTALL
)

# Replacement for Automation
content = re.sub(
    r'<div class="service-slide-card card-grad-4">(.*?)<p>Autonomous AI agents and seamless API workflow integrations.</p>\s*</div>\s*</div>\s*</div>',
    r'<a href="services.html#automation" class="service-slide-card card-grad-4">\1<p>Autonomous AI agents and seamless API workflow integrations.</p><div class="service-hover-link"><span>View all services</span> <i class="fal fa-arrow-right"></i></div></div></div></a>',
    content,
    flags=re.DOTALL
)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Hover states and links added.")
