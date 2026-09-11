import os
import re
import glob

files = glob.glob('c:/Users/my/Desktop/chatgpt/*.html') + glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html')

new_footer_services = '''<div class="footer-box"><p class="title">Departments</p><a href="{prefix}services.html">Development</a><a href="{prefix}services.html">Automation</a><a href="{prefix}services.html">Creative</a><a href="{prefix}services.html">Sales & Marketing</a></div>'''

for file in files:
    with open(file, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    prefix = '../' if ('services\\' in file or 'services/' in file) else ''
    
    # 1. Update footer links
    # Old footer box for services
    footer_match = re.search(r'(?s)(<div class="footer-box"><p class="title">Services</p>.*?</div>)', content)
    if footer_match:
        content = content.replace(footer_match.group(1), new_footer_services.replace('{prefix}', prefix))
    
    # 2. Update footer paragraph
    content = content.replace(
        'Automate, build and scale with custom AI, automation and software systems designed around your business.',
        'Design, build, automate and scale with full-service digital solutions designed around your business.'
    )
    
    # 3. Update "LEAD WITH AI" buttons to "START YOUR PROJECT"
    content = content.replace('LEAD WITH AI', 'START YOUR PROJECT')
    
    # 4. Updates specific to index.html body text
    if 'index.html' in file:
        content = content.replace(
            'for robust <strong style="color: #111827; font-weight: 600;">AI automation</strong>.',
            'for robust <strong style="color: #111827; font-weight: 600;">digital growth</strong>.'
        )
        content = content.replace(
            'We build AI workflows that answer, qualify, route, and execute real business tasks, turning scattered operational data into clear dashboards and decisions.',
            'We build custom web apps, scalable automations, and data-driven marketing campaigns that turn scattered operations into predictable, high-growth systems.'
        )
        content = content.replace(
            'automation, AI or custom software can create the biggest operational improvement.',
            'development, automation, or creative marketing can drive the biggest ROI for your business.'
        )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Sweeping copy updates completed across all files.")
