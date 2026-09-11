import os
import shutil

departments = {
    'Development Department': [
        ('Web Applications', 'web-applications.html', 'Custom scalable web applications.'),
        ('Web-Based Games', 'web-based-games.html', 'Interactive browser gaming experiences.'),
        ('WordPress Solutions', 'wordpress-solutions.html', 'Custom themes, plugins, and CMS buildouts.'),
        ('Shopify Stores', 'shopify-stores.html', 'E-commerce store design and optimization.'),
        ('Wix.com Development', 'wix-development.html', 'Fast, modern low-code web solutions.'),
        ('Desktop Applications', 'desktop-applications.html', 'Cross-platform desktop software.')
    ],
    'Automation Department': [
        ('AI Agents', 'ai-agents.html', 'Autonomous task and customer workflow agents.'),
        ('Custom Dashboards', 'custom-dashboards.html', 'Real-time operational data visualization.'),
        ('Calling Agents', 'calling-agents.html', 'AI-powered voice outreach and inbound calling.'),
        ('API & System Integration', 'api-system-integration.html', 'Seamless multi-platform data syncing.'),
        ('GoHighLevel (GHL)', 'gohighlevel.html', 'Complete CRM automation and funnel setup.')
    ],
    'Creative Development Department': [
        ('Graphic Design', 'graphic-design.html', 'Brand identity, social assets, and collateral.'),
        ('Video Editing', 'video-editing.html', 'High-impact promotional and social media videos.'),
        ('Social Media Design', 'social-media-design.html', 'Engaging feed graphics and ad creatives.'),
        ('3D & VFX', '3d-vfx.html', '3D modeling, rendering, and visual effects production.'),
        ('UI/UX Design', 'ui-ux-design.html', 'Modern web and mobile user interface prototyping.')
    ],
    'Sales & Marketing Department': [
        ('Email Marketing', 'email-marketing.html', 'Targeted drip campaigns and lead nurturing.'),
        ('Digital Marketing', 'digital-marketing.html', 'Omnichannel PPC, SEO, and paid growth campaigns.'),
        ('Freelancing Platform Management', 'freelancing-platform-management.html', 'Upwork & Fiverr agency optimization.'),
        ('LinkedIn Growth & Outreach', 'linkedin-growth.html', 'B2B lead generation and personal branding.')
    ]
}

template_path = 'c:/Users/my/Desktop/chatgpt/services/workflow-automation.html'
with open(template_path, 'r', encoding='utf-8', errors='replace') as f:
    base_html = f.read()

for dept, services in departments.items():
    for title, filename, desc in services:
        out_path = os.path.join('c:/Users/my/Desktop/chatgpt/services', filename)
        new_html = base_html.replace('Workflow Automation', title)
        new_html = new_html.replace('Eliminate manual tasks and connect your entire tech stack', desc)
        new_html = new_html.replace('flowvello automation services', dept)
        
        with open(out_path, 'w', encoding='utf-8') as out:
            out.write(new_html)

print('Successfully scaffolded 20 service pages!')
