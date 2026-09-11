# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

image_map = {
    "Wix Development": "https://images.unsplash.com/photo-1547658719-da2b51169166?auto=format&fit=crop&w=800&q=80",
    "Desktop Applications": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=800&q=80",
    "Api & Integration": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=80"
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

print(f"Replaced remaining {count} placeholder blocks with real Unsplash images!")
