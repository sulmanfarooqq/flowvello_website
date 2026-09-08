import re

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We just replaced the CTA, let's find the current h2 and p and button and replace them
html = html.replace('Ready to work with Flow Vello?', 'Ready to automate and scale?')
html = html.replace('Book a free consultation and let us show you where automation, AI or custom software can create the biggest operational improvement for your business.', 'Tell us what is slowing your team down. We will help you identify where automation, AI or custom software can create the biggest operational improvement.')
html = html.replace('BOOK A FREE CONSULTATION', 'REQUEST A FREE STRATEGY CALL')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("about CTA text replaced to match homepage exactly.")
