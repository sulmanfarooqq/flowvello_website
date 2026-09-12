import re

with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

nav_match = re.search(r'(?s)(<nav\b[^>]*id="navigration"[^>]*>.*?</nav>)', index_html)
if not nav_match:
    print("Could not find nav in index.html")
    exit()

full_nav = nav_match.group(1)

files_and_active = {
    'c:/Users/my/Desktop/chatgpt/about.html': 'About',
    'c:/Users/my/Desktop/chatgpt/faq.html': 'FAQ',
    'c:/Users/my/Desktop/chatgpt/contact.html': 'Contact',
    'c:/Users/my/Desktop/chatgpt/services.html': 'Services',
    'c:/Users/my/Desktop/chatgpt/privacy.html': None,
    'c:/Users/my/Desktop/chatgpt/terms.html': None
}

for filepath, active_tab in files_and_active.items():
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    html = re.sub(r'(?s)<nav\b[^>]*id="navigration"[^>]*>.*?</nav>', full_nav, html)
    
    html = html.replace('<li class="nav-item active"><a class="nav-link" href="index.html">Home</a></li>', '<li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>')
    
    if active_tab == 'About':
        html = html.replace('<li class="nav-item"><a class="nav-link" href="about.html">About</a></li>', '<li class="nav-item active"><a class="nav-link" href="about.html">About</a></li>')
    elif active_tab == 'FAQ':
        html = html.replace('<li class="nav-item"><a class="nav-link" href="faq.html">FAQ</a></li>', '<li class="nav-item active"><a class="nav-link" href="faq.html">FAQ</a></li>')
    elif active_tab == 'Contact':
        html = html.replace('<li class="nav-item"><a class="nav-link" href="contact.html">Contact</a></li>', '<li class="nav-item active"><a class="nav-link" href="contact.html">Contact</a></li>')
    elif active_tab == 'Services':
        html = html.replace('<li class="nav-item dropdown">\n                   <a class="nav-link dropdown-toggle" data-toggle="collapse" href="#servicesDropdown"', '<li class="nav-item dropdown active">\n                   <a class="nav-link dropdown-toggle" data-toggle="collapse" href="#servicesDropdown"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Fixed nav in {filepath}")

