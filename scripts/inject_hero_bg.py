# -*- coding: utf-8 -*-
import glob
import re

image_map = {
    "Web Applications": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1920&q=80",
    "Web-Based Games": "https://images.unsplash.com/photo-1552820728-8b83bb6b773f?auto=format&fit=crop&w=1920&q=80",
    "Wordpress Solutions": "https://images.unsplash.com/photo-1616469829581-73993eb86b02?auto=format&fit=crop&w=1920&q=80",
    "Shopify Stores": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=1920&q=80",
    "Desktop Apps": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1920&q=80",
    "Desktop Applications": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1920&q=80",
    "Ai Agents": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1920&q=80",
    "Custom Dashboards": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1920&q=80",
    "Calling Agents": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=1920&q=80",
    "Api Integrations": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1920&q=80",
    "Api & Integration": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1920&q=80",
    "Api & System Integration": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1920&q=80",
    "Gohighlevel (Ghl)": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1920&q=80",
    "Ui/Ux Design": "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=1920&q=80",
    "Graphic Design": "https://images.unsplash.com/photo-1626785774573-4b799315345d?auto=format&fit=crop&w=1920&q=80",
    "Video Editing": "https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?auto=format&fit=crop&w=1920&q=80",
    "Social Media Design": "https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&w=1920&q=80",
    "3D & Vfx": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1920&q=80",
    "Linkedin Growth": "https://images.unsplash.com/photo-1611944212129-29977ae1398c?auto=format&fit=crop&w=1920&q=80",
    "Digital Marketing": "https://images.unsplash.com/photo-1533750516457-a7f992034fec?auto=format&fit=crop&w=1920&q=80",
    "Email Marketing": "https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=1920&q=80",
    "Platform Management": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1920&q=80",
    "Freelancing Platform Management": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1920&q=80",
    "Wix Development": "https://images.unsplash.com/photo-1547658719-da2b51169166?auto=format&fit=crop&w=1920&q=80",
    "Wix.Com Development": "https://images.unsplash.com/photo-1547658719-da2b51169166?auto=format&fit=crop&w=1920&q=80"
}

default_img = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1920&q=80"

files = glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html')
count = 0

for file_path in files:
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        html = f.read()
        
    # Find the h1
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html)
    if not h1_match: continue
    
    title = h1_match.group(1).strip().title()
    
    img_url = image_map.get(title, default_img)
    
    # We want to replace <section class="fv-page-hero"> with the styled version.
    # It might already be styled if this script is run twice, so match v-page-hero regardless of existing styles.
    
    new_hero_tag = f'''<section class="fv-page-hero" style="background-image: linear-gradient(rgba(17, 24, 39, 0.85), rgba(17, 24, 39, 0.95)), url('{img_url}'); background-size: cover; background-position: center; border-bottom: 1px solid #1f2937;">'''
    
    html = re.sub(r'<section class="fv-page-hero"[^>]*>', new_hero_tag, html)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    count += 1

print(f"Injected hero backgrounds into {count} service pages.")
