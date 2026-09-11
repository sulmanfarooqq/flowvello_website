# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

# Fix the broken fv-why-grid section
# We have py-5">\s*<div class="dot-pattern-bg"> floating around.
# We need to prepend <section class="fv-why-grid  to it.

html = re.sub(r'(</section>\s*)py-5">', r'\1<section class="fv-why-grid py-5">', html)

with open('c:/Users/my/Desktop/chatgpt/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Fixed malformed HTML tag.")
