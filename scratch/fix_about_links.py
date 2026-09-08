import re

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'css/about.css' not in html:
    html = html.replace('<link rel="stylesheet" href="css/custom.css">', 
                        '<link rel="stylesheet" href="css/custom.css">\n   <link rel="stylesheet" href="css/about.css">')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("about.css linked in about.html")
