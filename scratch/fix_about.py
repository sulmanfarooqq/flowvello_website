import re
import os

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract <style>...</style>
style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
if style_match:
    style_content = style_match.group(1).strip()
    
    # Write to about.css
    mode = 'a' if os.path.exists('css/about.css') else 'w'
    with open('css/about.css', mode, encoding='utf-8') as f:
        f.write('\n\n/* Extracted from about.html */\n\n' + style_content)
        
    # Remove style block from html
    html = html.replace(style_match.group(0), '')

# Replace custom.css with global.css and about.css
if 'css/custom.css' in html:
    html = html.replace('<link rel="stylesheet" href="css/custom.css">', 
                        '<link rel="stylesheet" href="css/global.css">\n   <link rel="stylesheet" href="css/about.css">')
else:
    # If custom.css is not there, just ensure global and about are there
    pass

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("about.html fixed successfully.")
