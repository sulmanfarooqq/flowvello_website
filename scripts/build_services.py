# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup

with open('c:/Users/my/Desktop/chatgpt/services.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the massive section
section = soup.find('section', class_=lambda c: c and 'fv-services-presentation' in c)

if not section:
    print("Could not find section")
    exit()

departments = section.find_all('div', class_='mb-5 pb-5')
if not departments: # fallback if classes changed
    departments = section.find_all('div', class_='mb-5')

new_section_html = '''
<!-- MASTER SERVICES DIRECTORY (SHADCN GRID UI) -->
<section class="fv-services-presentation" style="background-color: #ffffff; padding-bottom: 80px;">
    
    <style>
       .shadcn-service-grid { display: grid; gap: 40px; grid-template-columns: 1fr; }
       @media (min-width: 768px) { .shadcn-service-grid { grid-template-columns: repeat(2, 1fr); } }
       @media (min-width: 1024px) { .shadcn-service-grid { grid-template-columns: repeat(3, 1fr); gap: 48px 32px; } }
       .shadcn-service-card { display: flex; flex-direction: column; gap: 16px; text-decoration: none !important; transition: transform 0.2s ease; cursor: pointer; }
       .shadcn-img-block { background-color: #f8fafc; border-radius: 12px; aspect-ratio: 16/9; display: flex; align-items: center; justify-content: center; font-size: 64px; color: #cbd5e1; transition: background-color 0.3s ease, color 0.3s ease; border: 1px solid #f1f5f9;}
       .shadcn-service-card:hover .shadcn-img-block { background-color: #f1f5f9; color: #94a3b8; }
       .shadcn-card-title { font-family: 'Rubik', sans-serif; font-size: 22px; font-weight: 500; color: #111827; margin: 0; letter-spacing: -0.5px; transition: color 0.2s ease; }
       .shadcn-service-card:hover .shadcn-card-title { color: #fb383b; }
       .shadcn-card-desc { font-family: 'Rubik', sans-serif; color: #6b7280; font-size: 16px; margin: 0; line-height: 1.6; }
    </style>
'''

dept_count = 1

for dept in departments:
    header = dept.find('h2')
    if not header:
        continue
    
    # Clean up the name (e.g. "Development Department")
    dept_name = header.get_text(strip=True).replace("Department", "").replace("Development", "").strip()
    if dept_name == "": dept_name = "Creative" # Handle edge case for Creative Development
    if dept_name == "Sales & Marketing": dept_name = "Marketing"
    if "Development" in header.get_text():
        if "Creative" not in header.get_text():
            dept_name = "Development"
    
    desc = dept.find('p')
    desc_text = desc.get_text(strip=True) if desc else ""

    new_section_html += f'''
    <div class="w-full py-5 lg:py-5" style="border-bottom: 1px solid #f3f4f6; padding-top: 80px !important; padding-bottom: 80px !important;">
      <div class="container mx-auto">
        
        <!-- Dept Header -->
        <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 12px; margin-bottom: 50px !important;">
            <div style="display: inline-flex; align-items: center; border-radius: 9999px; background-color: #111827; color: #ffffff; padding: 6px 16px; font-size: 13px; font-weight: 600; font-family: 'Rubik', sans-serif; letter-spacing: 1px; text-transform: uppercase;">
              Phase 0{dept_count}
            </div>
            <h2 style="font-family:'Rubik', sans-serif; font-size: 48px; font-weight: 500; color: #111827; letter-spacing: -1.5px; margin: 0; line-height: 1.1;">
              {dept_name}
            </h2>
            <p style="color: #6b7280; font-size: 18px; font-family:'Rubik', sans-serif; margin: 0; max-width: 600px; line-height: 1.6;">
              {desc_text}
            </p>
        </div>
        
        <div class="shadcn-service-grid">
'''
    
    # Find all services in this dept
    links = dept.find_all('a', class_='d-block')
    delay = 0.1
    for link in links:
        href = link.get('href')
        title_el = link.find('h3')
        title = title_el.get_text(strip=True) if title_el else ""
        title = title.title() # Capitalize nicely instead of ALL CAPS
        
        # Get description
        p_tags = link.find_all('p')
        service_desc = p_tags[0].get_text(strip=True) if p_tags else ""
        
        # Get icon
        icon_el = link.find('i')
        icon_class = "fal fa-browser"
        if icon_el:
            classes = icon_el.get('class', [])
            if "card-watermark" in classes:
                classes.remove("card-watermark")
            icon_class = " ".join(classes)
            if not icon_class:
                 icon_class = "fal fa-browser"
            
        new_section_html += f'''
           <!-- Card -->
           <a href="{href}" class="shadcn-service-card wow fadeInUp" data-wow-delay="{delay}s">
              <div class="shadcn-img-block"><i class="{icon_class}"></i></div>
              <div class="d-flex flex-column" style="gap: 8px;">
                  <h3 class="shadcn-card-title">{title}</h3>
                  <p class="shadcn-card-desc">{service_desc}</p>
              </div>
           </a>
'''
        delay += 0.1

    new_section_html += '''
        </div>
      </div>
    </div>
'''
    dept_count += 1

new_section_html += '</section>'

# Replace the old section using regex
import re
new_html = re.sub(r'(?s)<section class="fv-services-presentation[^>]*>.*?</section>', new_section_html, html, count=1)

with open('c:/Users/my/Desktop/chatgpt/services.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Successfully replaced services grid with Shadcn UI!")

