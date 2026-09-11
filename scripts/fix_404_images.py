# -*- coding: utf-8 -*-
with open('c:/Users/my/Desktop/chatgpt/services.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the 404s
html = html.replace('https://images.unsplash.com/photo-1432888117426-1d6ac08ae005', 'https://images.unsplash.com/photo-1533750516457-a7f992034fec')
html = html.replace('https://images.unsplash.com/photo-1563986768494-4dee2763ff0f', 'https://images.unsplash.com/photo-1557804506-669a67965ba0')

with open('c:/Users/my/Desktop/chatgpt/services.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Fixed the 404 images.")
