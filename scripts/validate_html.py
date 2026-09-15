import re
with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

div_open = html.count('<div')
div_close = html.count('</div')
section_open = html.count('<section')
section_close = html.count('</section')

print(f"Divs: {div_open} open, {div_close} closed. Diff: {div_open - div_close}")
print(f"Sections: {section_open} open, {section_close} closed. Diff: {section_open - section_close}")
