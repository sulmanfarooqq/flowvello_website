import os
import re
import glob

# Files to update
files = glob.glob('c:/Users/my/Desktop/chatgpt/*.html') + glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html')

new_mega_menu = '''
<div id="servicesDropdown" class="dropdown-menus collapse mega-menu-container" style="padding: 20px; width: 100%; max-width: 1200px; left: 50%; transform: translateX(-50%);">
    <div class="row w-100 m-0">
        <!-- Development Column -->
        <div class="col-lg-3 col-md-6 mb-4 mb-lg-0">
            <h3 class="mega-title" style="font-size: 14px; font-weight: 700; color: #fb383b; text-transform: uppercase; margin-bottom: 15px; letter-spacing: 1px;">Development</h3>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/web-applications.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fal fa-browser" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">Web Applications</span>
            </a>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/web-based-games.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fal fa-gamepad" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">Web-Based Games</span>
            </a>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/wordpress-solutions.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fab fa-wordpress" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">WordPress Solutions</span>
            </a>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/shopify-stores.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fab fa-shopify" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">Shopify Stores</span>
            </a>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/wix-development.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fab fa-wix" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">Wix Development</span>
            </a>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/desktop-applications.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fal fa-desktop" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">Desktop Apps</span>
            </a>
        </div>

        <!-- Automation Column -->
        <div class="col-lg-3 col-md-6 mb-4 mb-lg-0">
            <h3 class="mega-title" style="font-size: 14px; font-weight: 700; color: #fb383b; text-transform: uppercase; margin-bottom: 15px; letter-spacing: 1px;">Automation</h3>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/ai-agents.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fal fa-robot" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">AI Agents</span>
            </a>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/custom-dashboards.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fal fa-chart-pie" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">Custom Dashboards</span>
            </a>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/calling-agents.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fal fa-headset" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">Calling Agents</span>
            </a>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/api-system-integration.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fal fa-plug" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">API & Integration</span>
            </a>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/gohighlevel.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fal fa-funnel-dollar" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">GoHighLevel (GHL)</span>
            </a>
        </div>

        <!-- Creative Column -->
        <div class="col-lg-3 col-md-6 mb-4 mb-lg-0">
            <h3 class="mega-title" style="font-size: 14px; font-weight: 700; color: #fb383b; text-transform: uppercase; margin-bottom: 15px; letter-spacing: 1px;">Creative</h3>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/graphic-design.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fal fa-pen-nib" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">Graphic Design</span>
            </a>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/video-editing.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fal fa-video" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">Video Editing</span>
            </a>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/social-media-design.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fal fa-share-alt" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">Social Media Design</span>
            </a>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/3d-vfx.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fal fa-cubes" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">3D & VFX</span>
            </a>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/ui-ux-design.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fal fa-mobile-alt" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">UI/UX Design</span>
            </a>
        </div>

        <!-- Sales & Marketing Column -->
        <div class="col-lg-3 col-md-6 mb-4 mb-lg-0">
            <h3 class="mega-title" style="font-size: 14px; font-weight: 700; color: #fb383b; text-transform: uppercase; margin-bottom: 15px; letter-spacing: 1px;">Marketing</h3>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/email-marketing.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fal fa-envelope-open-text" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">Email Marketing</span>
            </a>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/digital-marketing.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fal fa-bullhorn" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">Digital Marketing</span>
            </a>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/freelancing-platform-management.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fal fa-briefcase" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">Platform Management</span>
            </a>
            <a class="dropdown-item mega-item py-2" href="{prefix}services/linkedin-growth.html" style="display: flex; align-items: center; gap: 10px; padding-left: 0; padding-right: 0;">
                <i class="fab fa-linkedin-in" style="color: #6b7280; width: 20px; text-align: center;"></i>
                <span style="font-size: 15px; font-weight: 500; color: #111827;">LinkedIn Growth</span>
            </a>
            
            <div style="margin-top: 25px; padding-top: 15px; border-top: 1px solid #e5e7eb;">
                <a href="{prefix}services.html" class="d-flex align-items-center" style="color: #fb383b; font-weight: 600; font-size: 15px; text-decoration: none;">
                    View All Services <i class="fal fa-arrow-right ml-2"></i>
                </a>
            </div>
        </div>
    </div>
</div>
'''

for file in files:
    with open(file, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # Determine if we are in root or in services/ to fix relative paths
    prefix = ''
    if 'services\\' in file or 'services/' in file:
        prefix = '../'
        # Inside services folder, link to services is just file.html
        formatted_menu = new_mega_menu.replace('{prefix}services/', '')
        formatted_menu = formatted_menu.replace('{prefix}', prefix)
    else:
        formatted_menu = new_mega_menu.replace('{prefix}', '')

    # We want to replace everything from <div id="servicesDropdown" ...> up to the matching closing </div>
    # A simple regex for this is hard if there are nested divs. 
    # The old mega menu was: <div id="servicesDropdown" class="dropdown-menus collapse mega-menu-container"> ... </div>
    # Actually, the old menu had 2 closing divs inside the <li>
    # So we can target from <div id="servicesDropdown" ...> until </li>
    
    # Or find the exact block.
    # The old mega menu ends right before </li>
    
    match = re.search(r'(?s)(<div id="servicesDropdown" class="dropdown-menus collapse mega-menu-container">)(.*?)(</li>)', content)
    if match:
        new_content = content[:match.start()] + formatted_menu + '\n                  </li>' + content[match.end():]
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
    else:
        # Fallback if structure is slightly different
        match = re.search(r'(?s)(<div id="servicesDropdown".*?)(</li>)', content)
        if match:
            new_content = content[:match.start()] + formatted_menu + '\n                  </li>' + content[match.end():]
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)

print("Mega menu updated across all pages.")
