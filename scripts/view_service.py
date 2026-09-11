with open('c:/Users/my/Desktop/chatgpt/services/web-applications.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
match = re.search(r'(?s)<!-- NAVIGATION -->.*?(<section class="fv-page-hero">.*)', html)
if match:
    print(match.group(1))
