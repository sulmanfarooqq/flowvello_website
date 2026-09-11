# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

image_map = {
    # Development
    "Web Applications": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80",
    "Web-Based Games": "https://images.unsplash.com/photo-1552820728-8b83bb6b773f?auto=format&fit=crop&w=800&q=80",
    "Wordpress Solutions": "https://images.unsplash.com/photo-1616469829581-73993eb86b02?auto=format&fit=crop&w=800&q=80",
    "Shopify Stores": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=800&q=80",
    "Desktop Apps": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=800&q=80",
    
    # Automation
    "Ai Agents": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=800&q=80",
    "Custom Dashboards": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
    "Calling Agents": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80",
    "Api Integrations": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=80",
    "Gohighlevel (Ghl)": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
    
    # Creative
    "Ui/Ux Design": "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=800&q=80",
    "Graphic Design": "https://images.unsplash.com/photo-1626785774573-4b799315345d?auto=format&fit=crop&w=800&q=80",
    "Video Editing": "https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?auto=format&fit=crop&w=800&q=80",
    "Social Media Design": "https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&w=800&q=80",
    "3D & Vfx": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80",
    
    # Marketing
    "Linkedin Growth": "https://images.unsplash.com/photo-1611944212129-29977ae1398c?auto=format&fit=crop&w=800&q=80",
    "Digital Marketing": "https://images.unsplash.com/photo-1432888117426-1d6ac08ae005?auto=format&fit=crop&w=800&q=80",
    "Email Marketing": "https://images.unsplash.com/photo-1563986768494-4dee2763ff0f?auto=format&fit=crop&w=800&q=80",
    "Platform Management": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=800&q=80",
}

with open('c:/Users/my/Desktop/chatgpt/services.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

cards = soup.find_all('a', class_='shadcn-service-card')
count = 0

for card in cards:
    title_el = card.find('h3', class_='shadcn-card-title')
    if not title_el:
        continue
    title = title_el.get_text(strip=True)
    
    if title in image_map:
        img_url = image_map[title]
        # Replace the <div class="shadcn-img-block">...</div> with <img class="shadcn-img-block" src="...">
        img_block = card.find('div', class_='shadcn-img-block')
        if img_block:
            new_img = soup.new_tag('img', src=img_url, alt=title, loading="lazy", style="object-fit: cover; width: 100%; display: block;")
            new_img['class'] = img_block.get('class')
            img_block.replace_with(new_img)
            count += 1
            
# Write back
with open('c:/Users/my/Desktop/chatgpt/services.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(f"Replaced {count} placeholder blocks with real Unsplash images!")
