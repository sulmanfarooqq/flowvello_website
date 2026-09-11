# -*- coding: utf-8 -*-
import re
import glob

# 1. Extract CTA from index.html
with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

cta_match = re.search(r'(?s)(<!-- CLOSING CTA \(SPLIT\) -->.*?</section>)', index_html)
if not cta_match:
    print("Could not find CTA section in index.html")
    exit()

cta_html = cta_match.group(1)

# 2. Update relative paths for the services/ directory
cta_html = cta_html.replace('src="img/', 'src="../img/')
cta_html = cta_html.replace('href="contact.html"', 'href="../contact.html"')

# 3. Replace in all services/*.html files
files = glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html')
count = 0

for file_path in files:
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        html = f.read()
    
    # We want to replace the DIRECT BOOKING LINK section
    # Regex logic: find <!-- DIRECT BOOKING LINK --> and replace everything up to <!-- FOOTER -->
    new_html = re.sub(r'(?s)<!-- DIRECT BOOKING LINK -->.*?(?=<!-- FOOTER -->|<footer)', cta_html + '\n\n', html, count=1)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    count += 1

print(f"Injected CTA into {count} service pages.")
