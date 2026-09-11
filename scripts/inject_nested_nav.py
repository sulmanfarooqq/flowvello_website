# -*- coding: utf-8 -*-
import glob
import re

files = glob.glob('c:/Users/my/Desktop/chatgpt/*.html') + glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html') + glob.glob('c:/Users/my/Desktop/chatgpt/industries/*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    prefix = '../' if ('/services/' in filepath.replace('\\', '/') or '/industries/' in filepath.replace('\\', '/')) else ''
    
    new_dropdown = f'''<div id="servicesDropdown" class="dropdown-menus collapse" style="padding: 10px; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); border: 1px solid #e5e7eb; min-width: 260px; background: #ffffff;">
    <style>
        .dropdown-submenu {{ position: relative; }}
        .dropdown-submenu > .dropdown-menu {{ top: 0; left: 100%; margin-top: -6px; margin-left: 0; border-radius: 8px; border: 1px solid #e5e7eb; box-shadow: 0 10px 25px rgba(0,0,0,0.1); display: none; min-width: 260px; padding: 10px; }}
        .dropdown-submenu:hover > .dropdown-menu {{ display: block; }}
        .dropdown-item:hover {{ background-color: #f9fafb !important; color: #fb383b !important; }}
        .dropdown-submenu .dropdown-item:hover i {{ color: #fb383b !important; }}
    </style>
    
    <!-- Development -->
    <div class="dropdown-submenu">
        <a class="dropdown-item d-flex justify-content-between align-items-center" href="#" style="padding: 10px 15px; font-weight: 500; font-size: 15px; border-radius: 6px;">
            <span><i class="fal fa-code" style="width:20px; color:#fb383b; margin-right:8px;"></i> Development</span>
            <i class="fal fa-angle-right"></i>
        </a>
        <div class="dropdown-menu">
            <a class="dropdown-item" href="{prefix}services/web-applications.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-browser" style="width:20px; color:#6b7280; margin-right:8px;"></i> Web Applications</a>
            <a class="dropdown-item" href="{prefix}services/web-based-games.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-gamepad" style="width:20px; color:#6b7280; margin-right:8px;"></i> Web-Based Games</a>
            <a class="dropdown-item" href="{prefix}services/wordpress-solutions.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fab fa-wordpress" style="width:20px; color:#6b7280; margin-right:8px;"></i> WordPress Solutions</a>
            <a class="dropdown-item" href="{prefix}services/shopify-stores.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fab fa-shopify" style="width:20px; color:#6b7280; margin-right:8px;"></i> Shopify Stores</a>
            <a class="dropdown-item" href="{prefix}services/desktop-applications.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-desktop" style="width:20px; color:#6b7280; margin-right:8px;"></i> Desktop Apps</a>
        </div>
    </div>

    <!-- Automation -->
    <div class="dropdown-submenu">
        <a class="dropdown-item d-flex justify-content-between align-items-center" href="#" style="padding: 10px 15px; font-weight: 500; font-size: 15px; border-radius: 6px;">
            <span><i class="fal fa-robot" style="width:20px; color:#fb383b; margin-right:8px;"></i> Automation</span>
            <i class="fal fa-angle-right"></i>
        </a>
        <div class="dropdown-menu">
            <a class="dropdown-item" href="{prefix}services/ai-agents.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-robot" style="width:20px; color:#6b7280; margin-right:8px;"></i> AI Agents</a>
            <a class="dropdown-item" href="{prefix}services/custom-dashboards.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-chart-pie" style="width:20px; color:#6b7280; margin-right:8px;"></i> Custom Dashboards</a>
            <a class="dropdown-item" href="{prefix}services/calling-agents.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-headset" style="width:20px; color:#6b7280; margin-right:8px;"></i> Calling Agents</a>
            <a class="dropdown-item" href="{prefix}services/api-system-integration.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-plug" style="width:20px; color:#6b7280; margin-right:8px;"></i> API Integrations</a>
            <a class="dropdown-item" href="{prefix}services/gohighlevel.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-funnel-dollar" style="width:20px; color:#6b7280; margin-right:8px;"></i> GoHighLevel (GHL)</a>
        </div>
    </div>

    <!-- Creative -->
    <div class="dropdown-submenu">
        <a class="dropdown-item d-flex justify-content-between align-items-center" href="#" style="padding: 10px 15px; font-weight: 500; font-size: 15px; border-radius: 6px;">
            <span><i class="fal fa-paint-brush" style="width:20px; color:#fb383b; margin-right:8px;"></i> Creative</span>
            <i class="fal fa-angle-right"></i>
        </a>
        <div class="dropdown-menu">
            <a class="dropdown-item" href="{prefix}services/ui-ux-design.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-mobile-alt" style="width:20px; color:#6b7280; margin-right:8px;"></i> UI/UX Design</a>
            <a class="dropdown-item" href="{prefix}services/graphic-design.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-pen-nib" style="width:20px; color:#6b7280; margin-right:8px;"></i> Graphic Design</a>
            <a class="dropdown-item" href="{prefix}services/video-editing.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-video" style="width:20px; color:#6b7280; margin-right:8px;"></i> Video Editing</a>
            <a class="dropdown-item" href="{prefix}services/social-media-design.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-share-alt" style="width:20px; color:#6b7280; margin-right:8px;"></i> Social Media Design</a>
            <a class="dropdown-item" href="{prefix}services/3d-vfx.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-cube" style="width:20px; color:#6b7280; margin-right:8px;"></i> 3D & VFX</a>
        </div>
    </div>

    <!-- Marketing -->
    <div class="dropdown-submenu">
        <a class="dropdown-item d-flex justify-content-between align-items-center" href="#" style="padding: 10px 15px; font-weight: 500; font-size: 15px; border-radius: 6px;">
            <span><i class="fal fa-bullhorn" style="width:20px; color:#fb383b; margin-right:8px;"></i> Marketing</span>
            <i class="fal fa-angle-right"></i>
        </a>
        <div class="dropdown-menu">
            <a class="dropdown-item" href="{prefix}services/linkedin-growth.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fab fa-linkedin" style="width:20px; color:#6b7280; margin-right:8px;"></i> LinkedIn Growth</a>
            <a class="dropdown-item" href="{prefix}services/digital-marketing.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-ad" style="width:20px; color:#6b7280; margin-right:8px;"></i> Digital Marketing</a>
            <a class="dropdown-item" href="{prefix}services/email-marketing.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-envelope-open-text" style="width:20px; color:#6b7280; margin-right:8px;"></i> Email Marketing</a>
            <a class="dropdown-item" href="{prefix}services/freelancing-platform-management.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-briefcase" style="width:20px; color:#6b7280; margin-right:8px;"></i> Platform Management</a>
            <a class="dropdown-item" href="{prefix}services/seo-services.html" style="padding: 10px 15px; border-radius: 6px; font-size:14px; font-weight:500;"><i class="fal fa-search" style="width:20px; color:#6b7280; margin-right:8px;"></i> SEO Services</a>
        </div>
    </div>

    <div class="dropdown-divider" style="margin: 8px 0;"></div>
    
    <!-- Explore All -->
    <a class="dropdown-item d-flex align-items-center" href="{prefix}services.html" style="padding: 10px 15px; font-weight: 600; font-size: 15px; color: #fb383b; border-radius: 6px; background-color: rgba(251,56,59,0.05);">
        <i class="fal fa-th-large" style="width:20px; margin-right:8px;"></i> Explore All Services
    </a>
</div>'''
    
    # We need to replace the existing <div id="servicesDropdown"...>...</div>
    # The existing mega-menu might have varying content, so we use regex.
    search_pattern = r'(<div id="servicesDropdown".*?</div>\s*</div>\s*</div>\s*</div>\s*</div>)'
    # Wait, the current mega menu structure has:
    # <div id="servicesDropdown">
    #   <div class="row">
    #      <div class="col-lg-3"> ... </div>
    #      <div class="col-lg-3"> ... </div>
    #      <div class="col-lg-3"> ... </div>
    #      <div class="col-lg-3"> ... </div>
    #   </div>
    # </div>
    # Let's write a safe regex to replace it. We know it ends before <li class="nav-item dropdown (the Industries one) or </li>
    
    # Actually, a better way is to find <div id="servicesDropdown" and replace everything up to the next </li>
    match = re.search(r'(<div id="servicesDropdown".*?)\s*</li>', html, flags=re.DOTALL)
    if match:
        old_div = match.group(1)
        # However, we have other <li>s after this if we aren't careful.
        pass

    # A more precise replacement:
    # Mega menu structure is EXACTLY:
    # <div id="servicesDropdown" class="dropdown-menus collapse mega-menu-container">
    # ...
    # </div> (the one closing servicesDropdown)
    
    # Let's just find <div id="servicesDropdown" and the next <li class="nav-item
    # Wait, if we use regex, balancing brackets is hard.
    
    # In my previous script, I matched: '(<div id="servicesDropdown".*?</div>\s*</div>\s*</div>\s*</div>\s*</div>)'
    html = re.sub(r'<div id="servicesDropdown".*?(?=</li>\s*<li class="nav-item dropdown)', new_dropdown + '\n                  ', html, flags=re.DOTALL)
    
    # Handle the case where industriesDropdown is NOT right after (e.g. services.html)
    if 'mega-menu-container' in html:
        # Fallback if the first regex missed
        html = re.sub(r'<div id="servicesDropdown" class="dropdown-menus collapse mega-menu-container">.*?(?=</li>)', new_dropdown + '\n                  ', html, flags=re.DOTALL)

    # Let's also clean up the mega-menu CSS block if it exists
    html = re.sub(r'<style>\s*/\* Enterprise Mega Menu CSS \*/.*?</style>', '', html, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Nested dropdown injected successfully across all files.")
