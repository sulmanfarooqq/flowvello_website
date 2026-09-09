import os
from bs4 import BeautifulSoup
import re

ROOT = r"c:\Users\my\Desktop\chatgpt"

# Extract shared components from index.html
with open(os.path.join(ROOT, "index.html"), "r", encoding="utf-8") as f:
    index_html = f.read()

soup = BeautifulSoup(index_html, "html.parser")

# Get Nav
nav = soup.find("nav", id="navigration")
nav_html = str(nav)

# Get CTA
cta = soup.find("section", id="contactArea")
cta_html = str(cta)

# Get Footer
footer = soup.find("footer", id="footerSection")
footer_html = str(footer)

# Get Head contents (minus title/meta description)
head = soup.find("head")
head_html = ""
for child in head.children:
    if child.name not in ["title", "meta"]:
        head_html += str(child)
    elif child.name == "meta" and child.get("name") not in ["description"]:
        head_html += str(child)

# Remove the page-specific css links if any snuck in, but index doesn't have them
def create_page(filename, title, description, body_content, is_active_link=""):
    # Fix the active nav item
    page_nav = nav_html
    page_nav = re.sub(r'nav-item active', r'nav-item', page_nav)
    if is_active_link:
        pattern = r'(<li class="nav-item">)(<a class="nav-link"[^>]*>' + is_active_link + r'</a>)'
        page_nav = re.sub(pattern, r'<li class="nav-item active">\2', page_nav)

    depth = filename.count('/')
    prefix = '../' * depth
    
    if depth > 0:
        # adjust hrefs and srcs
        page_nav = page_nav.replace('href="index.html"', f'href="{prefix}index.html"')
        page_nav = page_nav.replace('href="about.html"', f'href="{prefix}about.html"')
        page_nav = page_nav.replace('href="case-studies.html"', f'href="{prefix}case-studies.html"')
        page_nav = page_nav.replace('href="faq.html"', f'href="{prefix}faq.html"')
        page_nav = page_nav.replace('href="contact.html"', f'href="{prefix}contact.html"')
        page_nav = page_nav.replace('href="services/', f'href="{prefix}services/')
        page_nav = page_nav.replace('src="img/', f'src="{prefix}img/')
        
        page_cta = cta_html.replace('href="contact.html"', f'href="{prefix}contact.html"')
        page_cta = page_cta.replace('src="img/', f'src="{prefix}img/')
        
        page_footer = footer_html.replace('href="index.html"', f'href="{prefix}index.html"')
        page_footer = page_footer.replace('href="about.html"', f'href="{prefix}about.html"')
        page_footer = page_footer.replace('href="case-studies.html"', f'href="{prefix}case-studies.html"')
        page_footer = page_footer.replace('href="faq.html"', f'href="{prefix}faq.html"')
        page_footer = page_footer.replace('href="contact.html"', f'href="{prefix}contact.html"')
        page_footer = page_footer.replace('href="services/', f'href="{prefix}services/')
        page_footer = page_footer.replace('src="img/', f'src="{prefix}img/')
        
        page_head = head_html.replace('href="css/', f'href="{prefix}css/')
        page_head = page_head.replace('href="img/', f'href="{prefix}img/')
        
        # fix the CTA CTA background img specifically
        page_cta = page_cta.replace("img/cta_bg_2.webp", f"{prefix}img/cta_bg_2.webp")
    else:
        page_cta = cta_html
        page_footer = footer_html
        page_head = head_html
        
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{description}">
    <title>{title}</title>
    {page_head}
</head>
<body>
    {page_nav}
    
    {body_content}
    
    {page_cta}
    
    {page_footer}

    <a href="#" class="scroll-up"><i class="fal fa-chevron-up"></i></a>
    <script src="{prefix}js/jquery.min.js"></script>
    <script src="{prefix}js/bootstrap.min.js"></script>
    <script src="{prefix}js/popper.min.js"></script>
    <script src="{prefix}js/font-awesome-pro.js"></script>
    <script src="{prefix}js/wow.min.js"></script>
    <script src="{prefix}js/jquery.magnific-popup.min.js"></script>
    <script src="{prefix}js/owl.carousel.min.js"></script>
    <script src="{prefix}js/custom.js"></script>
</body>
</html>"""

    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Built {filename}")

if __name__ == '__main__':
    print("Builder ready.")
