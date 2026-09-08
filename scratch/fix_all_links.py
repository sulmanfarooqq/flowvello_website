import os
import glob

def ensure_link(file_path, css_file):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    prefix = '../' if '/' in file_path or '\\' in file_path else ''
    target_link = f'<link rel="stylesheet" href="{prefix}css/{css_file}">'
    if target_link not in html:
        html = html.replace(f'<link rel="stylesheet" href="{prefix}css/custom.css">', 
                            f'<link rel="stylesheet" href="{prefix}css/custom.css">\n   {target_link}')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)

ensure_link('contact.html', 'contact.css')
ensure_link('services/index.html', 'service.css')
ensure_link('services/index.html', 'services.css')
ensure_link('services/index.html', 'detail-pages.css')
ensure_link('services/workflow-automation.html', 'detail-pages.css')
ensure_link('services/ai-customer-support.html', 'detail-pages.css')
ensure_link('services/custom-ai-agents.html', 'detail-pages.css')
ensure_link('services/executive-dashboards.html', 'detail-pages.css')
ensure_link('services/sales-automation.html', 'detail-pages.css')
ensure_link('services/whatsapp-messaging.html', 'detail-pages.css')
print("All internal css links restored.")
