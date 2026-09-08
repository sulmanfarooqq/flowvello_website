import os

# 1. We will read the newly split files
with open('css/global.css.new', 'r', encoding='utf-8') as f:
    global_css = f.read()
    
with open('css/home.css.new', 'r', encoding='utf-8') as f:
    home_css = f.read()

with open('css/services-components.css.new', 'r', encoding='utf-8') as f:
    services_css = f.read()

with open('css/contact-components.css.new', 'r', encoding='utf-8') as f:
    contact_css = f.read()

with open('css/about-components.css.new', 'r', encoding='utf-8') as f:
    about_css = f.read()

with open('css/portfolio-components.css.new', 'r', encoding='utf-8') as f:
    portfolio_css = f.read()

with open('css/pricing-components.css.new', 'r', encoding='utf-8') as f:
    pricing_css = f.read()

# 2. Append to existing or create new
def append_or_create(filename, content):
    if not content.strip():
        return
    mode = 'a' if os.path.exists(filename) else 'w'
    with open(filename, mode, encoding='utf-8') as f:
        f.write('\n\n/* Extracted from global.css */\n\n' + content)

# Overwrite global.css with the slimmed down version
with open('css/global.css', 'w', encoding='utf-8') as f:
    f.write(global_css)

# Append homepage components to index.css
append_or_create('css/index.css', home_css)

# Append services components to service.css
append_or_create('css/service.css', services_css)

# Append contact components to contact.css
append_or_create('css/contact.css', contact_css)

# Create about.css, portfolio.css, pricing.css
append_or_create('css/about.css', about_css)
append_or_create('css/portfolio.css', portfolio_css)
append_or_create('css/pricing.css', pricing_css)

print("Successfully restructured CSS files.")
