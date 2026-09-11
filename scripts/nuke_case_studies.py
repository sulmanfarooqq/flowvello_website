# -*- coding: utf-8 -*-
import glob
import re
import os

files = glob.glob('c:/Users/my/Desktop/chatgpt/*.html') + glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html')

count = 0
for file_path in files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    # Remove from Nav (both relative and absolute paths if any exist)
    html = re.sub(r'<li class="nav-item">\s*<a class="nav-link" href="(\.\./)?case-studies\.html">Case Studies</a>\s*</li>', '', html)
    
    # Remove from Footer
    html = re.sub(r'<a href="(\.\./)?case-studies\.html">Case Studies</a>', '', html)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    count += 1

# Delete the actual file
target_file = 'c:/Users/my/Desktop/chatgpt/case-studies.html'
if os.path.exists(target_file):
    os.remove(target_file)
    print("Deleted case-studies.html")

print(f"Scrubbed Case Studies link from {count} files.")
