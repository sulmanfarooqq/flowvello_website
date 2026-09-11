# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

with open('c:/Users/my/Desktop/chatgpt/services.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the main container holding the departments
presentation_section = soup.find('section', class_=lambda c: c and 'fv-services-presentation' in c)
if not presentation_section:
    print("Could not find fv-services-presentation")
    exit()

# Find all department blocks
dept_blocks = presentation_section.find_all('div', class_='w-full', recursive=False)

if len(dept_blocks) != 4:
    print(f"Expected 4 departments, found {len(dept_blocks)}")
    exit()

# Map them by name
depts = {}
for block in dept_blocks:
    h2 = block.find('h2')
    name = h2.get_text(strip=True) if h2 else ""
    depts[name] = block

# Desired Order
order = ["Creative", "Development", "Marketing", "Automation"]

# Ensure we have them all
missing = [o for o in order if o not in depts]
if missing:
    print(f"Missing departments: {missing}")
    print(f"Found: {list(depts.keys())}")
    exit()

# Detach all blocks from the tree
for block in dept_blocks:
    block.extract()

# Re-append in correct order and update Phase labels
phase_count = 1
for dept_name in order:
    block = depts[dept_name]
    
    # Find the Phase label div
    # It has text "Phase 0X"
    pill = block.find(lambda tag: tag.name == 'div' and 'Phase 0' in tag.get_text())
    if pill:
        pill.string = f"Phase 0{phase_count}"
        
    presentation_section.append(block)
    phase_count += 1

with open('c:/Users/my/Desktop/chatgpt/services.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
    
print("Successfully reordered departments into logical pipeline!")
