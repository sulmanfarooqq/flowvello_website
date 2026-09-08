import os
import glob
import re

def restore_css_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    prefix = '../' if '/' in file_path or '\\' in file_path else ''
    
    # Remove all the chunked links
    html = re.sub(rf'<link rel="stylesheet" href="{prefix}css/global\.css">\n?', '', html)
    html = re.sub(rf'<link rel="stylesheet" href="{prefix}css/index\.css">\n?', '', html)
    html = re.sub(rf'<link rel="stylesheet" href="{prefix}css/about\.css">\n?', '', html)
    html = re.sub(rf'<link rel="stylesheet" href="{prefix}css/contact\.css">\n?', '', html)
    html = re.sub(rf'<link rel="stylesheet" href="{prefix}css/service\.css">\n?', '', html)
    html = re.sub(rf'<link rel="stylesheet" href="{prefix}css/detail-pages\.css">\n?', '', html)
    
    # Inject custom.css before chatbot.css
    if f'css/custom.css' not in html:
        html = html.replace(f'<link rel="stylesheet" href="{prefix}css/chatbot.css">', 
                            f'<link rel="stylesheet" href="{prefix}css/custom.css">\n   <link rel="stylesheet" href="{prefix}css/chatbot.css">')
                                
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

for f in glob.glob('*.html') + glob.glob('services/*.html'):
    restore_css_links(f)

print("Restored custom.css in all HTML files.")
