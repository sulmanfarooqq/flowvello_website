import re
with open('c:/Users/my/Desktop/chatgpt/services.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace mega menu in services.html
search_pattern = r'(<div class="dropdown-menus collapse mega-menu-container" id="servicesDropdown">.*?</div>\s*</div>\s*</div>\s*</div>)'

# Get the new_nav from one of the other files
with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()
    
nav_match = re.search(r'(<style>\n.nested-services-menu.*?</style>\s*<div id="servicesDropdown" class="dropdown-menus collapse".*?</div>)', index_html, flags=re.DOTALL)
if nav_match:
    new_nav = nav_match.group(1)
    # Ensure correct href prefix for root files
    html = re.sub(search_pattern, new_nav, html, flags=re.DOTALL)
    with open('c:/Users/my/Desktop/chatgpt/services.html', 'w', encoding='utf-8') as f:
        f.write(html)
