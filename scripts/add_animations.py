# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add wow to the header block
html = html.replace('<div style="max-width: 500px;">\n                    <h2 style="font-family:\\'Rubik\\'', '<div style="max-width: 500px;" class="wow fadeInUp" data-wow-delay="0.1s">\n                    <h2 style="font-family:\\'Rubik\\'')

# 2. Add wow to the cards
html = html.replace('alt="Creative Department" loading="lazy">\n                        </div>', 'alt="Creative Department" loading="lazy">\n                        </div>').replace('<a href="services.html" class="f72-card" style="text-decoration: none;">\n                        <div class="f72-img-container">\n                            <img src="https://images.unsplash.com/photo-1561070791-2526d30994b5', '<a href="services.html" class="f72-card wow fadeInUp" data-wow-delay="0.2s" style="text-decoration: none;">\n                        <div class="f72-img-container">\n                            <img src="https://images.unsplash.com/photo-1561070791-2526d30994b5')

html = html.replace('<a href="services.html" class="f72-card" style="text-decoration: none;">\n                        <div class="f72-img-container">\n                            <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c', '<a href="services.html" class="f72-card wow fadeInUp" data-wow-delay="0.3s" style="text-decoration: none;">\n                        <div class="f72-img-container">\n                            <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c')

html = html.replace('<a href="services.html" class="f72-card" style="text-decoration: none;">\n                        <div class="f72-img-container">\n                            <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f', '<a href="services.html" class="f72-card wow fadeInUp" data-wow-delay="0.4s" style="text-decoration: none;">\n                        <div class="f72-img-container">\n                            <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f')

html = html.replace('<a href="services.html" class="f72-card" style="text-decoration: none;">\n                        <div class="f72-img-container">\n                            <img src="https://images.unsplash.com/photo-1519389950473-47ba0277781c', '<a href="services.html" class="f72-card wow fadeInUp" data-wow-delay="0.5s" style="text-decoration: none;">\n                        <div class="f72-img-container">\n                            <img src="https://images.unsplash.com/photo-1519389950473-47ba0277781c')


with open('c:/Users/my/Desktop/chatgpt/about.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Animations added successfully.")
