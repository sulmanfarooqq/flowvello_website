# -*- coding: utf-8 -*-
import re
import glob

files = glob.glob('c:/Users/my/Desktop/chatgpt/*.html') + glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html')

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

    # We need to wipe EVERYTHING from <div id="servicesDropdown" up to <li class="nav-item"><a class="nav-link" href=".*about.html
    # This will cleanly remove any broken nested <li> and <ul> tags that were left behind.
    
    match = re.search(r'(?s)(<div id="servicesDropdown".*?)(<li class="nav-item">\s*<a class="nav-link".*?about\.html)', content)
    if match:
        new_content = content[:match.start()] + formatted_menu + '\n                  </li>\n                  ' + match.group(2) + content[match.end():]
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Surgically cleaned up nav items and re-injected enterprise mega menu.")
