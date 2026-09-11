import glob
import re

files = glob.glob('c:/Users/my/Desktop/chatgpt/industries/*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove 'active' from the Services li
    html = re.sub(
        r'<li class="nav-item dropdown active">\s*<a class="nav-link dropdown-toggle" data-toggle="collapse" href="#servicesDropdown"',
        r'<li class="nav-item dropdown">\n                   <a class="nav-link dropdown-toggle" data-toggle="collapse" href="#servicesDropdown"',
        html
    )
    
    # Add 'active' to the Industries li
    html = re.sub(
        r'<li class="nav-item dropdown">\s*<a class="nav-link dropdown-toggle" data-toggle="collapse" href="#industriesDropdown"',
        r'<li class="nav-item dropdown active">\n                   <a class="nav-link dropdown-toggle" data-toggle="collapse" href="#industriesDropdown"',
        html
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Active states fixed on industry pages.")
