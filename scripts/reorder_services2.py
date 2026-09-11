# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

with open('c:/Users/my/Desktop/chatgpt/services.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

presentation_section = soup.find('section', class_=lambda c: c and 'fv-services-presentation' in c)
dept_blocks = presentation_section.find_all('div', class_='w-full', recursive=False)

depts = {}
for block in dept_blocks:
    h2 = block.find('h2')
    name = h2.get_text(strip=True) if h2 else ""
    if "Marketing" in name:
        name = "Marketing"
    depts[name] = block

order = ["Creative", "Development", "Marketing", "Automation"]

for block in dept_blocks:
    block.extract()

phase_count = 1
for dept_name in order:
    block = depts[dept_name]
    
    pill = block.find(lambda tag: tag.name == 'div' and 'Phase 0' in tag.get_text())
    if pill:
        pill.string = f"Phase 0{phase_count}"
        
    presentation_section.append(block)
    phase_count += 1

with open('c:/Users/my/Desktop/chatgpt/services.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
    
print("Successfully reordered departments into logical pipeline!")
