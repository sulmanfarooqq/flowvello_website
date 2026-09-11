import os
import re

files_to_update = [
    'c:/Users/my/Desktop/chatgpt/index.html',
    'c:/Users/my/Desktop/chatgpt/about.html',
    'c:/Users/my/Desktop/chatgpt/faq.html',
    'c:/Users/my/Desktop/chatgpt/contact.html',
    'c:/Users/my/Desktop/chatgpt/case-studies.html'
]

seo_replacements = {
    'index.html': {
        'title': 'Flow Vello | Full-Service Digital Agency: Dev, Automation & Marketing',
        'desc': 'Flow Vello is a premium digital agency delivering custom web development, intelligent automation, elite creative design, and data-driven marketing to scale your business.',
        'hero1': 'Leading change<br>through digital<br>excellence',
        'hero2': 'Build, automate, and<br>scale your business<br>faster & smarter'
    },
    'about.html': {
        'title': 'About Flow Vello | The Digital Growth Agency',
        'desc': 'Learn how Flow Vello transformed from a specialized automation firm into a full-service digital agency powering development, creative, and marketing for global brands.'
    },
    'faq.html': {
        'title': 'FAQ | Flow Vello Digital Agency',
        'desc': 'Get answers to common questions about our web development, automation, creative design, and marketing services.'
    },
    'contact.html': {
        'title': 'Contact Flow Vello | Start Your Digital Project',
        'desc': 'Ready to scale? Contact Flow Vello to discuss your web development, AI automation, creative, or marketing needs.'
    },
    'case-studies.html': {
        'title': 'Case Studies | Flow Vello Digital Agency',
        'desc': 'Explore our portfolio of successful web applications, automated workflows, brand identities, and high-ROI marketing campaigns.'
    }
}

for file in files_to_update:
    if not os.path.exists(file):
        continue
    
    with open(file, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    filename = os.path.basename(file)
    data = seo_replacements.get(filename)
    
    if data:
        # Update title
        content = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>', content)
        
        # Update meta description
        content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{data["desc"]}">', content)
        
        # Specific homepage hero updates
        if filename == 'index.html':
            content = content.replace('Leading change<br>through AI-native<br>technology', data['hero1'])
            content = content.replace('Automate business<br>processes to scale<br>faster & smarter', data['hero2'])
            # Also update the About section in index.html if it mentions just AI
            content = content.replace('We are an AI automation agency', 'We are a full-service digital agency')
            
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated SEO and core messaging across main HTML files.")
