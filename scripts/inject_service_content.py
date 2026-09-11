# -*- coding: utf-8 -*-
import os
import glob
import re
import json

try:
    with open('c:/Users/my/Desktop/chatgpt/scripts/data.json', 'r', encoding='utf-8') as f:
        custom_data = json.load(f)
except:
    custom_data = {}

def get_service_data(title):
    if title in custom_data:
        return custom_data[title]
    
    # Generic highly-professional fallback customized by title
    return {
        "images": [
            "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80"
        ],
        "features": [
            {"icon": "layer-group", "title": "Custom Architecture", "desc": f"Tailored {title} frameworks built precisely for your operational bottlenecks without generic template bloat."},
            {"icon": "code-branch", "title": "API Synchronization", "desc": f"Seamlessly wired into your existing CRM, database, and marketing stack for fluid {title} data transfer."},
            {"icon": "shield-check", "title": "Enterprise Security", "desc": "Rigorous data protection, strict auth protocols, and secure cloud deployment standards."},
            {"icon": "bolt", "title": "Speed Optimization", "desc": "Stripped of unnecessary code to ensure sub-second response times and elite performance."},
            {"icon": "users-cog", "title": "Human Fallback", "desc": "Intelligent escalation paths designed to hand off processes to your team before failure."},
            {"icon": "box-open", "title": "Full Handover", "desc": "You own the system. Complete documentation, codebase handover, and administrative access."}
        ]
    }

template = '''
<!-- SHADCN PORTFOLIO GALLERY -->
<section class="py-5" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
    <div class="container">
        <div class="mb-5 d-flex flex-column align-items-start" style="gap: 12px;">
            <div style="display: inline-flex; align-items: center; border-radius: 9999px; background-color: #111827; color: #ffffff; padding: 6px 16px; font-size: 13px; font-weight: 600; font-family: 'Rubik', sans-serif; letter-spacing: 1px; text-transform: uppercase;">
                Deliverables
            </div>
            <h2 style="font-family:'Rubik', sans-serif; font-size: 42px; font-weight: 500; color: #111827; letter-spacing: -1.5px; margin: 0; line-height: 1.1;">
                Project Showcase
            </h2>
            <p style="color: #6b7280; font-size: 18px; font-family:'Rubik', sans-serif; margin: 0; max-width: 600px; line-height: 1.6;">
                Visual representations of our enterprise deliverables and real-world project deployments for this service.
            </p>
        </div>
        
        <div style="display: grid; gap: 32px; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
            <div style="border-radius: 12px; overflow: hidden; border: 1px solid #e5e7eb; background: #f8fafc; aspect-ratio: 16/9;">
                <img src="{IMG_1}" alt="Deliverable 1" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            </div>
            <div style="border-radius: 12px; overflow: hidden; border: 1px solid #e5e7eb; background: #f8fafc; aspect-ratio: 16/9;">
                <img src="{IMG_2}" alt="Deliverable 2" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            </div>
            <div style="border-radius: 12px; overflow: hidden; border: 1px solid #e5e7eb; background: #f8fafc; aspect-ratio: 16/9;">
                <img src="{IMG_3}" alt="Deliverable 3" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            </div>
        </div>
    </div>
</section>

<!-- SHADCN LIGHT BENTO GRID (FEATURES) -->
<section class="py-5" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important;">
    <div class="container" style="max-width: 1100px;">
        <div class="text-center mb-5 pb-2 mx-auto" style="max-width: 700px;">
            <span style="color: #fb383b; font-family: 'Rubik', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px; display: inline-block;">INCLUDED IN SCOPE</span>
            <h2 style="font-family:'Rubik', sans-serif; font-size: 42px; font-weight: 500; color: #111827; letter-spacing: -1px; margin-bottom: 20px; line-height: 1.15;">
                Features & Deliverables
            </h2>
            <p style="color: #6b7280; font-size: 16px; font-family:'Rubik', sans-serif; margin: 0; line-height: 1.6;">
                Everything engineered, tested, and deployed when you integrate {SERVICE_NAME} into your infrastructure.
            </p>
        </div>

        <style>
            .feature-light-grid { display: grid; gap: 24px; grid-template-columns: 1fr; }
            @media (min-width: 768px) { .feature-light-grid { grid-template-columns: repeat(2, 1fr); } }
            @media (min-width: 1024px) { .feature-light-grid { grid-template-columns: repeat(3, 1fr); } }
            .feature-light-card { background: #ffffff; padding: 40px; border-radius: 12px; border: 1px solid #e5e7eb; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); transition: box-shadow 0.2s ease, transform 0.2s ease; }
            .feature-light-card:hover { box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); transform: translateY(-2px); }
            .fl-icon { font-size: 24px; color: #fb383b; margin-bottom: 20px; }
            .fl-title { font-family: 'Rubik', sans-serif; font-size: 18px; font-weight: 600; color: #111827; margin: 0 0 12px 0; letter-spacing: -0.5px; }
            .fl-desc { font-family: 'Rubik', sans-serif; color: #6b7280; font-size: 15px; line-height: 1.6; margin: 0; }
        </style>

        <div class="feature-light-grid">
{CARDS_HTML}
        </div>
    </div>
</section>
'''

files = glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html')
count = 0

for file_path in files:
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        html = f.read()
        
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html)
    if not h1_match: continue
    
    title = h1_match.group(1).strip().title()
    
    # Extract existing CTA block before we replace the middle
    cta_match = re.search(r'(?s)(<!-- CLOSING CTA \(SPLIT\) -->.*?</section>)', html)
    if not cta_match: continue
    cta_html = cta_match.group(1)
    
    hero_match = re.search(r'(?s)(.*?</section>)', html)
    footer_match = re.search(r'(?s)(<!-- FOOTER -->.*)', html)
    
    if hero_match and footer_match:
        hero_content = hero_match.group(1)
        
        data = get_service_data(title)
        
        cards_html = ""
        for f in data['features']:
            cards_html += f'''            <div class="feature-light-card">
                <div class="fl-icon"><i class="fal fa-{f['icon']}"></i></div>
                <h3 class="fl-title">{f['title']}</h3>
                <p class="fl-desc">{f['desc']}</p>
            </div>\n'''
            
        middle = template.replace('{IMG_1}', data['images'][0])
        middle = middle.replace('{IMG_2}', data['images'][1])
        middle = middle.replace('{IMG_3}', data['images'][2])
        middle = middle.replace('{SERVICE_NAME}', title)
        middle = middle.replace('{CARDS_HTML}', cards_html)
        
        new_html = hero_content + '\n\n' + middle + '\n\n' + cta_html + '\n\n' + footer_match.group(1)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
            
        count += 1

print(f"Redesigned {count} pages with SEO content and fresh images!")
