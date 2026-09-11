# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the specific section's background style
old_line = '<!-- 4 PILLARS GRID (REBUILT FEATURE 72) -->\n   <section class="py-5" style="background-color: #ffffff; padding-top: 100px !important; padding-bottom: 100px !important;">'
new_line = '<!-- 4 PILLARS GRID (REBUILT FEATURE 72) -->\n   <section class="py-5" style="background-color: #f8fafc; border-top: 1px solid #e5e7eb; border-bottom: 1px solid #e5e7eb; padding-top: 100px !important; padding-bottom: 100px !important;">'

if old_line in html:
    new_html = html.replace(old_line, new_line)
    with open('c:/Users/my/Desktop/chatgpt/about.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Background color updated to #f8fafc")
else:
    print("Could not find exact string to replace.")
