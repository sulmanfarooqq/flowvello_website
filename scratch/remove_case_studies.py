# -*- coding: utf-8 -*-
import re
import codecs

with codecs.open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the Case Studies section
html = re.sub(r'<!-- PROOF / BRIDGE TO CASE STUDIES -->.*?</section>\s*(?=<!-- CLOSING CTA)', '', html, flags=re.DOTALL)

with codecs.open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Case studies section removed.")
