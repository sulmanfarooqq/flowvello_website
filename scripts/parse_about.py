with open('c:/Users/my/Desktop/chatgpt/about.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
match = re.search(r'(?s)(<section class="fv-page-hero">.*?</section>)(.*?)(<section class="fv-about-mission.*?</section>)(.*?)(<section class="fv-why-grid.*?</section>)(.*?)(<section class="fv-section presentation-section">.*?</section>)(.*?)(<section class="fv-process-dark.*?</section>)(.*?)(<section class="fv-cta-split.*?</section>)', html)

if match:
    print("Found all sections.")
else:
    print("Could not parse perfectly, fallback to finding hero and footer.")
