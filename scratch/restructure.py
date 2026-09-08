import os
import glob
import re

moves = {
    'service.html': 'services/index.html',
    'workflow-automation.html': 'services/workflow-automation.html',
    'ai-customer-support.html': 'services/ai-customer-support.html',
    'custom-ai-agents.html': 'services/custom-ai-agents.html',
    'executive-dashboards.html': 'services/executive-dashboards.html',
    'sales-automation.html': 'services/sales-automation.html',
    'whatsapp-messaging.html': 'services/whatsapp-messaging.html'
}

os.makedirs('services', exist_ok=True)

def update_links(content, is_in_subdir):
    prefix = '../' if is_in_subdir else ''
    
    # 1. Update asset links
    content = re.sub(r'(href|src)="css/', fr'\1="{prefix}css/', content)
    content = re.sub(r'(href|src)="js/', fr'\1="{prefix}js/', content)
    content = re.sub(r'(href|src)="img/', fr'\1="{prefix}img/', content)
    content = re.sub(r'(href|src)="fonts/', fr'\1="{prefix}fonts/', content)
    
    # 2. Update page links safely
    href_replacements = {
        'service.html': 'services/index.html' if not is_in_subdir else 'index.html',
        'workflow-automation.html': 'services/workflow-automation.html' if not is_in_subdir else 'workflow-automation.html',
        'ai-customer-support.html': 'services/ai-customer-support.html' if not is_in_subdir else 'ai-customer-support.html',
        'custom-ai-agents.html': 'services/custom-ai-agents.html' if not is_in_subdir else 'custom-ai-agents.html',
        'executive-dashboards.html': 'services/executive-dashboards.html' if not is_in_subdir else 'executive-dashboards.html',
        'sales-automation.html': 'services/sales-automation.html' if not is_in_subdir else 'sales-automation.html',
        'whatsapp-messaging.html': 'services/whatsapp-messaging.html' if not is_in_subdir else 'whatsapp-messaging.html',
        'index.html': 'index.html' if not is_in_subdir else '../index.html',
        'about.html': 'about.html' if not is_in_subdir else '../about.html',
        'contact.html': 'contact.html' if not is_in_subdir else '../contact.html',
        'faq.html': 'faq.html' if not is_in_subdir else '../faq.html',
        'case-studies.html': 'case-studies.html' if not is_in_subdir else '../case-studies.html',
    }
    
    # Use a regex that matches exactly the target strings
    # We construct a regex like: href="(service\.html|index\.html|...)"
    pattern = r'(href|src)="(' + '|'.join(map(re.escape, href_replacements.keys())) + r')"'
    
    def replacer(match):
        attr = match.group(1)
        filename = match.group(2)
        new_filename = href_replacements[filename]
        return f'{attr}="{new_filename}"'
        
    content = re.sub(pattern, replacer, content)
    
    return content

html_files = [f for f in glob.glob('*.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_path = moves.get(file, file)
    is_in_subdir = '/' in new_path
    
    updated_content = update_links(content, is_in_subdir)
    
    with open(new_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
        
    if file != new_path:
        os.remove(file)
        print(f"Moved and updated {file} -> {new_path}")
    else:
        print(f"Updated {file}")

print("Restructuring complete.")
