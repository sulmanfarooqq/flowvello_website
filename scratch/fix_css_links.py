import os
import glob
import re

def update_css_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    filename = os.path.basename(file_path)
    prefix = '../' if '/' in file_path or '\\' in file_path else ''
    
    # Base replacements
    # If custom.css is linked, replace it with global.css
    html = re.sub(r'<link rel="stylesheet" href="([^"]*)custom\.css">', f'<link rel="stylesheet" href="{prefix}css/global.css">', html)
    
    # Make sure global.css is linked if missing completely?
    # If we replaced custom.css with global.css, we are good.
    
    # Determine which component CSS to add
    component_css = None
    if filename == 'index.html' and 'services' not in file_path:
        component_css = 'index.css'
    elif filename == 'index.html' and 'services' in file_path:
        component_css = 'service.css'
    elif filename == 'contact.html':
        component_css = 'contact.css'
    elif filename == 'about.html':
        component_css = 'about.css'
    elif filename in ['workflow-automation.html', 'ai-customer-support.html', 'custom-ai-agents.html', 'executive-dashboards.html', 'sales-automation.html', 'whatsapp-messaging.html']:
        component_css = 'detail-pages.css' # Or service.css? They are services.
        
    # Inject component CSS right after global.css
    if component_css:
        link_str = f'<link rel="stylesheet" href="{prefix}css/{component_css}">'
        # Check if already there
        if link_str not in html:
            html = html.replace(f'<link rel="stylesheet" href="{prefix}css/global.css">', 
                                f'<link rel="stylesheet" href="{prefix}css/global.css">\n   <link rel="stylesheet" href="{prefix}css/{component_css}">')
                                
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

# Process all html files in root
for f in glob.glob('*.html'):
    update_css_links(f)
    
# Process all html files in services
for f in glob.glob('services/*.html'):
    update_css_links(f)

print("CSS links updated in all HTML files.")
