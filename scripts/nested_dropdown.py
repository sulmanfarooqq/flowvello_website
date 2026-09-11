# -*- coding: utf-8 -*-
import glob
import re

files = glob.glob('c:/Users/my/Desktop/chatgpt/*.html') + glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html') + glob.glob('c:/Users/my/Desktop/chatgpt/industries/*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
        
    prefix = '../' if ('/services/' in filepath.replace('\\', '/') or '/industries/' in filepath.replace('\\', '/')) else ''

    new_nav = f'''<style>
.nested-services-menu {{
    padding: 10px; 
    border-radius: 8px; 
    box-shadow: 0 10px 25px rgba(0,0,0,0.1); 
    border: 1px solid #e5e7eb; 
    min-width: 280px; 
    background: #ffffff;
    list-style: none;
    margin: 0;
}}
.dropdown-submenu {{
    position: relative;
    padding: 2px 0;
}}
.dropdown-submenu > .dropdown-menu {{
    top: 0;
    left: 100%;
    margin-top: -5px;
    display: none;
    border-radius: 8px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    border: 1px solid #e5e7eb;
    min-width: 260px;
    background: #ffffff;
    padding: 10px;
}}
.dropdown-submenu:hover > .dropdown-menu {{
    display: block;
}}
.nested-item {{
    padding: 10px 15px !important;
    font-weight: 500 !important;
    font-size: 15px !important;
    color: #374151 !important;
    border-radius: 6px;
    transition: all 0.2s;
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
}}
.nested-item:hover {{
    background-color: #f9fafb !important;
    color: #111827 !important;
}}
.nested-subitem {{
    padding: 8px 15px !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    color: #4b5563 !important;
    border-radius: 6px;
    transition: all 0.2s;
    display: flex !important;
    align-items: center !important;
}}
.nested-subitem:hover {{
    background-color: #f9fafb !important;
    color: #fb383b !important;
}}
@media (max-width: 991px) {{
    .dropdown-submenu > .dropdown-menu {{
        display: block;
        position: static;
        box-shadow: none;
        border: none;
        padding-left: 20px;
        margin-top: 5px;
        background: transparent;
    }}
    .nested-item i.fa-angle-right {{ display: none; }}
}}
</style>

<div id="servicesDropdown" class="dropdown-menus collapse" style="padding:0; border:none; box-shadow:none; background:transparent;">
   <ul class="nested-services-menu">
       
       <li class="dropdown-submenu">
           <a class="dropdown-item nested-item" href="#">
               <span><i class="fal fa-code" style="width:20px; color:#fb383b; margin-right:8px;"></i> Development</span>
               <i class="fal fa-angle-right" style="color: #9ca3af;"></i>
           </a>
           <ul class="dropdown-menu">
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/web-applications.html"><i class="fal fa-browser" style="width:20px; color:#fb383b; margin-right:8px;"></i> Web Applications</a></li>
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/web-based-games.html"><i class="fal fa-gamepad" style="width:20px; color:#fb383b; margin-right:8px;"></i> Web-Based Games</a></li>
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/wordpress-solutions.html"><i class="fab fa-wordpress" style="width:20px; color:#fb383b; margin-right:8px;"></i> WordPress Solutions</a></li>
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/shopify-stores.html"><i class="fab fa-shopify" style="width:20px; color:#fb383b; margin-right:8px;"></i> Shopify Stores</a></li>
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/desktop-applications.html"><i class="fal fa-desktop" style="width:20px; color:#fb383b; margin-right:8px;"></i> Desktop Apps</a></li>
           </ul>
       </li>

       <li class="dropdown-submenu">
           <a class="dropdown-item nested-item" href="#">
               <span><i class="fal fa-robot" style="width:20px; color:#fb383b; margin-right:8px;"></i> Automation</span>
               <i class="fal fa-angle-right" style="color: #9ca3af;"></i>
           </a>
           <ul class="dropdown-menu">
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/ai-agents.html"><i class="fal fa-robot" style="width:20px; color:#fb383b; margin-right:8px;"></i> AI Agents</a></li>
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/custom-dashboards.html"><i class="fal fa-chart-pie" style="width:20px; color:#fb383b; margin-right:8px;"></i> Custom Dashboards</a></li>
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/calling-agents.html"><i class="fal fa-headset" style="width:20px; color:#fb383b; margin-right:8px;"></i> Calling Agents</a></li>
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/api-system-integration.html"><i class="fal fa-plug" style="width:20px; color:#fb383b; margin-right:8px;"></i> API Integrations</a></li>
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/gohighlevel.html"><i class="fal fa-funnel-dollar" style="width:20px; color:#fb383b; margin-right:8px;"></i> GoHighLevel (GHL)</a></li>
           </ul>
       </li>
       
       <li class="dropdown-submenu">
           <a class="dropdown-item nested-item" href="#">
               <span><i class="fal fa-paint-brush" style="width:20px; color:#fb383b; margin-right:8px;"></i> Creative</span>
               <i class="fal fa-angle-right" style="color: #9ca3af;"></i>
           </a>
           <ul class="dropdown-menu">
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/ui-ux-design.html"><i class="fal fa-mobile-alt" style="width:20px; color:#fb383b; margin-right:8px;"></i> UI/UX Design</a></li>
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/graphic-design.html"><i class="fal fa-pen-nib" style="width:20px; color:#fb383b; margin-right:8px;"></i> Graphic Design</a></li>
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/video-editing.html"><i class="fal fa-video" style="width:20px; color:#fb383b; margin-right:8px;"></i> Video Editing</a></li>
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/social-media-design.html"><i class="fal fa-share-alt" style="width:20px; color:#fb383b; margin-right:8px;"></i> Social Media Design</a></li>
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/3d-vfx.html"><i class="fal fa-cube" style="width:20px; color:#fb383b; margin-right:8px;"></i> 3D & VFX</a></li>
           </ul>
       </li>

       <li class="dropdown-submenu">
           <a class="dropdown-item nested-item" href="#">
               <span><i class="fal fa-bullhorn" style="width:20px; color:#fb383b; margin-right:8px;"></i> Marketing</span>
               <i class="fal fa-angle-right" style="color: #9ca3af;"></i>
           </a>
           <ul class="dropdown-menu">
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/linkedin-growth.html"><i class="fab fa-linkedin" style="width:20px; color:#fb383b; margin-right:8px;"></i> LinkedIn Growth</a></li>
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/digital-marketing.html"><i class="fal fa-ad" style="width:20px; color:#fb383b; margin-right:8px;"></i> Digital Marketing</a></li>
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/email-marketing.html"><i class="fal fa-envelope-open-text" style="width:20px; color:#fb383b; margin-right:8px;"></i> Email Marketing</a></li>
               <li><a class="dropdown-item nested-subitem" href="{prefix}services/freelancing-platform-management.html"><i class="fal fa-briefcase" style="width:20px; color:#fb383b; margin-right:8px;"></i> Platform Management</a></li>
           </ul>
       </li>

       <li><hr class="dropdown-divider" style="margin: 8px 0; border-top: 1px solid #e5e7eb;"></li>
       <li>
           <a class="dropdown-item nested-item" href="{prefix}services.html" style="color: #fb383b !important; font-weight: 600 !important; justify-content: flex-start !important;">
               <i class="fal fa-arrow-right" style="width:20px; margin-right:8px;"></i> Explore All Services
           </a>
       </li>
   </ul>
</div>'''

    # Replace the existing mega menu.
    # The mega menu starts with <div id="servicesDropdown" class="dropdown-menus collapse mega-menu-container">
    # and ends with a </li> that closes the entire dropdown.
    search_pattern = r'(<div id="servicesDropdown".*?</div>\s*</div>\s*</div>\s*</div>)'
    match = re.search(search_pattern, html, flags=re.DOTALL)
    
    if match:
        html = html.replace(match.group(1), new_nav)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Replaced in {filepath}")
    else:
        # Check if it was already replaced or structured differently
        search2 = r'(<div id="servicesDropdown" class="dropdown-menus collapse" style="padding:0;.*?</ul>\n</div>)'
        if re.search(search2, html, flags=re.DOTALL):
            html = re.sub(search2, new_nav, html, flags=re.DOTALL)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Updated in {filepath}")
        else:
            print(f"Skipped {filepath} - could not find servicesDropdown pattern")

