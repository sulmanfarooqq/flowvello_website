# -*- coding: utf-8 -*-
import re
with open('c:/Users/my/Desktop/chatgpt/services.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'(?s)(<li class="nav-item dropdown">.*?Services.*?</li>)', html)
if match:
    print("Found services li in services.html. Length:", len(match.group(1)))
    print("Ends with:", repr(match.group(1)[-50:]))
else:
    print("Not found at all")
