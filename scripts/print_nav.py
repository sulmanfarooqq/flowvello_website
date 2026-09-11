import re
with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'(?s)(<ul class="mb-0 position-relative d-lg-flex align-items-center" id="main-nav-list">.*?</ul>)', html)
if match:
    print(match.group(1))
