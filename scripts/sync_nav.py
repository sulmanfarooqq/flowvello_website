import re

# 1. First, copy the exact full <nav> from index.html (which is perfect)
with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

nav_match = re.search(r'(<nav id="navigration".*?</nav>)', index_html, flags=re.DOTALL)
full_nav = nav_match.group(1)

# Now, we need to inject this full_nav into all root files, and set the correct 'active' class.

files_and_active = {
    'c:/Users/my/Desktop/chatgpt/about.html': 'About',
    'c:/Users/my/Desktop/chatgpt/faq.html': 'FAQ',
    'c:/Users/my/Desktop/chatgpt/contact.html': 'Contact',
    'c:/Users/my/Desktop/chatgpt/services.html': 'Services',
    'c:/Users/my/Desktop/chatgpt/privacy.html': None,
    'c:/Users/my/Desktop/chatgpt/terms.html': None
}

for filepath, active_tab in files_and_active.items():
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # Replace the entire nav
        html = re.sub(r'<nav id="navigration".*?</nav>', full_nav, html, flags=re.DOTALL)
        
        # Remove active from Home
        html = html.replace('<li class="nav-item active"><a class="nav-link" href="index.html">Home</a></li>', '<li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>')
        
        # Add active to the correct tab
        if active_tab == 'About':
            html = html.replace('<li class="nav-item"><a class="nav-link" href="about.html">About</a></li>', '<li class="nav-item active"><a class="nav-link" href="about.html">About</a></li>')
        elif active_tab == 'FAQ':
            html = html.replace('<li class="nav-item"><a class="nav-link" href="faq.html">FAQ</a></li>', '<li class="nav-item active"><a class="nav-link" href="faq.html">FAQ</a></li>')
        elif active_tab == 'Contact':
            html = html.replace('<li class="nav-item"><a class="nav-link" href="contact.html">Contact</a></li>', '<li class="nav-item active"><a class="nav-link" href="contact.html">Contact</a></li>')
        elif active_tab == 'Services':
            # Services is a dropdown
            html = html.replace('<li class="nav-item dropdown">\n                   <a class="nav-link dropdown-toggle" data-toggle="collapse" href="#servicesDropdown"', '<li class="nav-item dropdown active">\n                   <a class="nav-link dropdown-toggle" data-toggle="collapse" href="#servicesDropdown"')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Fixed nav in {filepath}")
    except Exception as e:
        print(f"Error in {filepath}: {e}")

# Fix services.html hero
with open('c:/Users/my/Desktop/chatgpt/services.html', 'r', encoding='utf-8') as f:
    services_html = f.read()
    
# If services.html has the FAQ hero, replace it
bad_hero = r'<section class="fv-page-hero">\s*<div class="container text-center">\s*<span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s">FAQ</span>\s*<h1 class="wow fadeInUp" data-wow-delay="0.2s">Frequently Asked Questions.</h1>\s*<p class="fv-lead wow fadeInUp" data-wow-delay="0.3s">Find answers to common questions about our products and processes.</p>\s*</div>\s*</section>'

good_hero = '''<section class="fv-page-hero" style="background-image: linear-gradient(rgba(17, 24, 39, 0.85), rgba(17, 24, 39, 0.95)), url('https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1920&q=80'); background-size: cover; background-position: center; border-bottom: 1px solid #1f2937;">
  <div class="container text-center">
  <span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s">DIRECTORY</span>
  <h1 class="wow fadeInUp" data-wow-delay="0.2s">Master Services Directory.</h1>
  <p class="fv-lead wow fadeInUp" data-wow-delay="0.3s">Every technical, automated, and creative solution we provide.</p>
  </div>
  </section>'''

services_html = re.sub(bad_hero, good_hero, services_html)
with open('c:/Users/my/Desktop/chatgpt/services.html', 'w', encoding='utf-8') as f:
    f.write(services_html)

