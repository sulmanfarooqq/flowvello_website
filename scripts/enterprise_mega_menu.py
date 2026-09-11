# -*- coding: utf-8 -*-
import os
import re
import glob

files = glob.glob('c:/Users/my/Desktop/chatgpt/*.html') + glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html')

css = '''
<style>
/* Enterprise Mega Menu CSS */
.mega-menu-container {
    padding: 25px !important; 
    width: 100vw !important; 
    max-width: 1100px !important; 
    left: 50% !important; 
    transform: translateX(-50%) !important;
    border-radius: 12px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.08);
    border: 1px solid #e5e7eb;
}
.mega-title {
    font-size: 13px !important; 
    font-weight: 700 !important; 
    color: #fb383b !important; 
    text-transform: uppercase !important; 
    margin-bottom: 20px !important; 
    letter-spacing: 1.5px !important;
}
.mega-item {
    display: flex !important; 
    align-items: center !important; 
    gap: 12px !important; 
    padding: 10px 12px !important; 
    border-radius: 8px !important;
    transition: background 0.2s !important;
}
.mega-item:hover {
    background-color: #f9fafb !important;
}
.mega-item i {
    color: #6b7280;
    width: 20px;
    text-align: center;
    font-size: 18px;
    transition: color 0.2s;
}
.mega-item:hover i {
    color: #fb383b;
}
.mega-item span {
    font-size: 15px !important; 
    font-weight: 500 !important; 
    color: #111827 !important;
}
@media (max-width: 991px) {
    .mega-menu-container {
        width: 100% !important;
        max-width: 100% !important;
        transform: none !important;
        left: 0 !important;
        box-shadow: none !important;
        border: none !important;
        padding: 15px !important;
    }
}
</style>
'''

new_mega_menu = '''
<div id="servicesDropdown" class="dropdown-menus collapse mega-menu-container">
    <div class="row w-100 m-0">
        <!-- Development Column -->
        <div class="col-lg-3 col-md-6 mb-4 mb-lg-0">
            <h3 class="mega-title">Development</h3>
            <a class="dropdown-item mega-item" href="{prefix}services/web-applications.html">
                <i class="fal fa-browser"></i><span>Web Applications</span>
            </a>
            <a class="dropdown-item mega-item" href="{prefix}services/web-based-games.html">
                <i class="fal fa-gamepad"></i><span>Web-Based Games</span>
            </a>
            <a class="dropdown-item mega-item" href="{prefix}services/wordpress-solutions.html">
                <i class="fab fa-wordpress"></i><span>WordPress Solutions</span>
            </a>
            <a class="dropdown-item mega-item" href="{prefix}services/shopify-stores.html">
                <i class="fab fa-shopify"></i><span>Shopify Stores</span>
            </a>
            <a class="dropdown-item mega-item" href="{prefix}services/desktop-applications.html">
                <i class="fal fa-desktop"></i><span>Desktop Apps</span>
            </a>
        </div>

        <!-- Automation Column -->
        <div class="col-lg-3 col-md-6 mb-4 mb-lg-0">
            <h3 class="mega-title">Automation</h3>
            <a class="dropdown-item mega-item" href="{prefix}services/ai-agents.html">
                <i class="fal fa-robot"></i><span>AI Agents</span>
            </a>
            <a class="dropdown-item mega-item" href="{prefix}services/custom-dashboards.html">
                <i class="fal fa-chart-pie"></i><span>Custom Dashboards</span>
            </a>
            <a class="dropdown-item mega-item" href="{prefix}services/calling-agents.html">
                <i class="fal fa-headset"></i><span>Calling Agents</span>
            </a>
            <a class="dropdown-item mega-item" href="{prefix}services/api-system-integration.html">
                <i class="fal fa-plug"></i><span>API Integrations</span>
            </a>
            <a class="dropdown-item mega-item" href="{prefix}services/gohighlevel.html">
                <i class="fal fa-funnel-dollar"></i><span>GoHighLevel (GHL)</span>
            </a>
        </div>

        <!-- Creative Column -->
        <div class="col-lg-3 col-md-6 mb-4 mb-lg-0">
            <h3 class="mega-title">Creative</h3>
            <a class="dropdown-item mega-item" href="{prefix}services/ui-ux-design.html">
                <i class="fal fa-mobile-alt"></i><span>UI/UX Design</span>
            </a>
            <a class="dropdown-item mega-item" href="{prefix}services/graphic-design.html">
                <i class="fal fa-pen-nib"></i><span>Graphic Design</span>
            </a>
            <a class="dropdown-item mega-item" href="{prefix}services/video-editing.html">
                <i class="fal fa-video"></i><span>Video Editing</span>
            </a>
            <a class="dropdown-item mega-item" href="{prefix}services/social-media-design.html">
                <i class="fal fa-share-alt"></i><span>Social Media Design</span>
            </a>
            <a class="dropdown-item mega-item" href="{prefix}services/3d-vfx.html">
                <i class="fal fa-cubes"></i><span>3D & VFX</span>
            </a>
        </div>

        <!-- Marketing Column -->
        <div class="col-lg-3 col-md-6 mb-4 mb-lg-0">
            <h3 class="mega-title">Marketing</h3>
            <a class="dropdown-item mega-item" href="{prefix}services/linkedin-growth.html">
                <i class="fab fa-linkedin-in"></i><span>LinkedIn Growth</span>
            </a>
            <a class="dropdown-item mega-item" href="{prefix}services/digital-marketing.html">
                <i class="fal fa-bullhorn"></i><span>Digital Marketing</span>
            </a>
            <a class="dropdown-item mega-item" href="{prefix}services/email-marketing.html">
                <i class="fal fa-envelope-open-text"></i><span>Email Marketing</span>
            </a>
            <a class="dropdown-item mega-item" href="{prefix}services/freelancing-platform-management.html">
                <i class="fal fa-briefcase"></i><span>Platform Management</span>
            </a>
            
            <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid #e5e7eb;">
                <a href="{prefix}services.html" class="d-flex align-items-center" style="color: #fb383b; font-weight: 600; font-size: 14px; text-decoration: none; padding: 10px 12px; transition: opacity 0.2s;" onmouseover="this.style.opacity='0.8'" onmouseout="this.style.opacity='1'">
                    View Master Directory <i class="fal fa-arrow-right ml-2"></i>
                </a>
            </div>
        </div>
    </div>
</div>
'''

for file in files:
    with open(file, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    prefix = '../' if ('services\\' in file or 'services/' in file) else ''
    formatted_menu = new_mega_menu.replace('{prefix}', prefix)

    # Clean up the previous nested CSS from index.html if it exists
    content = re.sub(r'(?s)<style>\s*/\* Submenu CSS for highly professional side-flyout \*/.*?</style>', '', content)
    
    # Inject new enterprise CSS into head
    if '/* Enterprise Mega Menu CSS */' not in content:
        content = content.replace('</head>', css + '\n</head>')

    # Target the dropdown block
    match = re.search(r'(?s)(<div id="servicesDropdown".*?)(</li>)', content)
    if match:
        new_content = content[:match.start()] + formatted_menu + '\n                  </li>' + content[match.end():]
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Applied enterprise 4-column mega menu across entire site.")
