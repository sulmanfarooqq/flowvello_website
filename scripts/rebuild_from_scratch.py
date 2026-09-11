# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re

# 1. Parse original data
with open('c:/Users/my/Desktop/chatgpt/scripts/services_backup.html', 'r', encoding='utf-8', errors='replace') as f:
    backup_html = f.read()

soup_backup = BeautifulSoup(backup_html, 'html.parser')
section_backup = soup_backup.find('section', class_=lambda c: c and 'fv-services-presentation' in c)

# Extract original departments
raw_departments = section_backup.find_all('div', class_='mb-5 pb-5')

dept_data = {}

for dept in raw_departments:
    header = dept.find('h2')
    if not header: continue
    dept_name = header.get_text(strip=True).replace("Department", "").replace("Development", "").strip()
    if dept_name == "": dept_name = "Creative"
    if dept_name == "Sales & Marketing": dept_name = "Marketing"
    if "Development" in header.get_text() and "Creative" not in header.get_text():
        dept_name = "Development"
        
    desc = dept.find('p')
    desc_text = desc.get_text(strip=True) if desc else ""
    
    services = []
    links = dept.find_all('a', class_='d-block')
    for link in links:
        href = link.get('href')
        title_el = link.find('h3')
        title = title_el.get_text(strip=True).title() if title_el else ""
        
        p_tags = link.find_all('p')
        service_desc = p_tags[0].get_text(strip=True) if p_tags else ""
        
        services.append({
            'href': href,
            'title': title,
            'desc': service_desc
        })
        
    dept_data[dept_name] = {
        'desc': desc_text,
        'services': services
    }

image_map = {
    "Web Applications": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80",
    "Web-Based Games": "https://images.unsplash.com/photo-1552820728-8b83bb6b773f?auto=format&fit=crop&w=800&q=80",
    "Wordpress Solutions": "https://images.unsplash.com/photo-1616469829581-73993eb86b02?auto=format&fit=crop&w=800&q=80",
    "Shopify Stores": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=800&q=80",
    "Desktop Apps": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=800&q=80",
    "Desktop Applications": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=800&q=80",
    "Ai Agents": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=800&q=80",
    "Custom Dashboards": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
    "Calling Agents": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80",
    "Api Integrations": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=80",
    "Api & Integration": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=80",
    "Gohighlevel (Ghl)": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
    "Ui/Ux Design": "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=800&q=80",
    "Graphic Design": "https://images.unsplash.com/photo-1626785774573-4b799315345d?auto=format&fit=crop&w=800&q=80",
    "Video Editing": "https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?auto=format&fit=crop&w=800&q=80",
    "Social Media Design": "https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&w=800&q=80",
    "3D & Vfx": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80",
    "Linkedin Growth": "https://images.unsplash.com/photo-1611944212129-29977ae1398c?auto=format&fit=crop&w=800&q=80",
    "Digital Marketing": "https://images.unsplash.com/photo-1533750516457-a7f992034fec?auto=format&fit=crop&w=800&q=80",
    "Email Marketing": "https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=800&q=80",
    "Platform Management": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=800&q=80",
    "Wix Development": "https://images.unsplash.com/photo-1547658719-da2b51169166?auto=format&fit=crop&w=800&q=80"
}

# 2. Build the NEW DOM string
new_section_html = '''
<!-- MASTER SERVICES DIRECTORY (SHADCN GRID UI) -->
<section class="fv-services-presentation" style="background-color: #ffffff; padding-bottom: 80px;">
    
    <style>
       .shadcn-service-grid { display: grid; gap: 40px; grid-template-columns: 1fr; }
       @media (min-width: 768px) { .shadcn-service-grid { grid-template-columns: repeat(2, 1fr); } }
       @media (min-width: 1024px) { .shadcn-service-grid { grid-template-columns: repeat(3, 1fr); gap: 48px 32px; } }
       .shadcn-service-card { display: flex; flex-direction: column; gap: 16px; text-decoration: none !important; transition: transform 0.2s ease; cursor: pointer; }
       .shadcn-img-block { background-color: #f8fafc; border-radius: 12px; aspect-ratio: 16/9; display: flex; align-items: center; justify-content: center; font-size: 64px; color: #cbd5e1; transition: background-color 0.3s ease, color 0.3s ease; border: 1px solid #f1f5f9; overflow: hidden; }
       .shadcn-service-card:hover .shadcn-img-block { background-color: #f1f5f9; color: #94a3b8; }
       .shadcn-card-title { font-family: 'Rubik', sans-serif; font-size: 22px; font-weight: 500; color: #111827; margin: 0; letter-spacing: -0.5px; transition: color 0.2s ease; }
       .shadcn-service-card:hover .shadcn-card-title { color: #fb383b; }
       .shadcn-card-desc { font-family: 'Rubik', sans-serif; color: #6b7280; font-size: 16px; margin: 0; line-height: 1.6; }
    </style>
'''

order = ["Creative", "Development", "Marketing", "Automation"]
phase_count = 1

for dept_name in order:
    if dept_name not in dept_data: continue
    
    desc_text = dept_data[dept_name]['desc']
    
    new_section_html += f'''
    <div class="w-full py-5 lg:py-5" style="border-bottom: 1px solid #f3f4f6; padding-top: 80px !important; padding-bottom: 80px !important;">
      <div class="container mx-auto">
        <!-- Dept Header -->
        <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 12px; margin-bottom: 50px !important;">
            <div style="display: inline-flex; align-items: center; border-radius: 9999px; background-color: #111827; color: #ffffff; padding: 6px 16px; font-size: 13px; font-weight: 600; font-family: 'Rubik', sans-serif; letter-spacing: 1px; text-transform: uppercase;">
              Phase 0{phase_count}
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
    
    delay = 0.1
    for service in dept_data[dept_name]['services']:
        title = service['title']
        img_url = image_map.get(title, "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80")
        
        new_section_html += f'''
           <!-- Card -->
           <a href="{service['href']}" class="shadcn-service-card wow fadeInUp" data-wow-delay="{delay}s">
              <img class="shadcn-img-block" src="{img_url}" alt="{title}" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px;">
                  <h3 class="shadcn-card-title">{title}</h3>
                  <p class="shadcn-card-desc">{service['desc']}</p>
              </div>
           </a>
'''
        delay += 0.1
        
    new_section_html += '''
        </div>
      </div>
    </div>
'''
    phase_count += 1

new_section_html += '</section>'

# 3. Replace the broken section in the LIVE file
with open('c:/Users/my/Desktop/chatgpt/services.html', 'r', encoding='utf-8', errors='replace') as f:
    live_html = f.read()

live_html = re.sub(r'(?s)<section class="fv-services-presentation[^>]*>.*?</section>', new_section_html, live_html, count=1)

with open('c:/Users/my/Desktop/chatgpt/services.html', 'w', encoding='utf-8') as f:
    f.write(live_html)

print("Recovered from Git backup and rebuilt flawlessly!")
