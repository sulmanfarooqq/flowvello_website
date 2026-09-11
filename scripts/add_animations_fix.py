# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add wow to header
html = html.replace('<div style="max-width: 500px;">', '<div style="max-width: 500px;" class="wow fadeInUp" data-wow-delay="0.1s">')

# Add wow to cards
html = re.sub(r'<a href="services\.html" class="f72-card" style="text-decoration: none;">\s*<div class="f72-img-container">\s*<img src="https://images\.unsplash\.com/photo-1561070791', r'<a href="services.html" class="f72-card wow fadeInUp" data-wow-delay="0.2s" style="text-decoration: none;">\n                        <div class="f72-img-container">\n                            <img src="https://images.unsplash.com/photo-1561070791', html)

html = re.sub(r'<a href="services\.html" class="f72-card" style="text-decoration: none;">\s*<div class="f72-img-container">\s*<img src="https://images\.unsplash\.com/photo-1555066931', r'<a href="services.html" class="f72-card wow fadeInUp" data-wow-delay="0.3s" style="text-decoration: none;">\n                        <div class="f72-img-container">\n                            <img src="https://images.unsplash.com/photo-1555066931', html)

html = re.sub(r'<a href="services\.html" class="f72-card" style="text-decoration: none;">\s*<div class="f72-img-container">\s*<img src="https://images\.unsplash\.com/photo-1460925895', r'<a href="services.html" class="f72-card wow fadeInUp" data-wow-delay="0.4s" style="text-decoration: none;">\n                        <div class="f72-img-container">\n                            <img src="https://images.unsplash.com/photo-1460925895', html)

html = re.sub(r'<a href="services\.html" class="f72-card" style="text-decoration: none;">\s*<div class="f72-img-container">\s*<img src="https://images\.unsplash\.com/photo-1519389950', r'<a href="services.html" class="f72-card wow fadeInUp" data-wow-delay="0.5s" style="text-decoration: none;">\n                        <div class="f72-img-container">\n                            <img src="https://images.unsplash.com/photo-1519389950', html)

with open('c:/Users/my/Desktop/chatgpt/about.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Animations added successfully.")
