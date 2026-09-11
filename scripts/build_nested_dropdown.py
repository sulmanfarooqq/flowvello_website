# -*- coding: utf-8 -*-
import re

with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

css = '''
<style>
/* Submenu CSS for highly professional side-flyout */
.dropdown-submenu {
    position: relative;
    border-radius: 8px;
}
.dropdown-submenu:hover {
    background-color: #f9fafb;
}
.dropdown-submenu > .dropdown-menu {
    top: 0;
    left: 100%;
    margin-top: -6px;
    margin-left: 0px;
    border-radius: 12px;
    border: 1px solid rgba(0,0,0,0.05);
    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
    min-width: 260px;
    padding: 12px;
    opacity: 0;
    visibility: hidden;
    transform: translateX(10px);
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    display: block;
}
.dropdown-submenu:hover > .dropdown-menu {
    opacity: 1;
    visibility: visible;
    transform: translateX(0);
}
.dropdown-menu .dropdown-item {
    padding: 10px 15px;
    border-radius: 6px;
    font-family: 'Rubik', sans-serif;
    font-size: 15px;
    color: #111827;
    transition: background 0.2s, color 0.2s;
    font-weight: 500;
}
.dropdown-menu .dropdown-item:hover {
    background-color: #f9fafb;
    color: #fb383b;
}
.explore-all-link {
    color: #fb383b !important;
    font-weight: 600 !important;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.explore-all-link i {
    transition: transform 0.2s;
}
.explore-all-link:hover i {
    transform: translateX(4px);
}
.dropdown-submenu > a.mega-item:hover {
    background-color: transparent !important;
}
</style>
'''

if '.dropdown-submenu' not in html:
    html = html.replace('</head>', css + '\n</head>')

new_menu = '''
<div id="servicesDropdown" class="dropdown-menus collapse mega-menu-container" style="padding: 15px; min-width: 340px;">
    <div class="mega-menu-content p-0" style="width: 100%;">
       <ul class="list-unstyled mb-0 w-100">
          
          <!-- Development -->
          <li class="dropdown-submenu w-100 mb-1">
             <a class="dropdown-item mega-item d-flex justify-content-between align-items-center" href="services.html" style="padding: 15px; border-radius: 8px;">
                <div class="d-flex align-items-center w-100">
                   <div class="mega-icon mr-3"><i class="fal fa-browser" style="font-size: 20px; color: #fb383b;"></i></div>
                   <div class="mega-text">
                      <span style="font-weight: 600; font-size: 16px;">Development</span>
                      <p style="margin: 0; font-size: 13px; color: #6b7280; line-height: 1.4; margin-top: 2px;">Web, Apps & Custom Software</p>
                   </div>
                </div>
                <i class="fal fa-angle-right ml-2" style="color: #9ca3af; font-size: 18px;"></i>
             </a>
             <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="services/web-applications.html"><i class="fal fa-window-alt mr-2" style="color:#6b7280; width: 20px;"></i>Web Applications</a></li>
                <li><a class="dropdown-item" href="services/wordpress-solutions.html"><i class="fab fa-wordpress mr-2" style="color:#6b7280; width: 20px;"></i>WordPress Solutions</a></li>
                <li><hr class="dropdown-divider my-2"></li>
                <li><a class="dropdown-item explore-all-link" href="services.html">Explore All <i class="fal fa-arrow-right"></i></a></li>
             </ul>
          </li>

          <!-- Automation -->
          <li class="dropdown-submenu w-100 mb-1">
             <a class="dropdown-item mega-item d-flex justify-content-between align-items-center" href="services.html" style="padding: 15px; border-radius: 8px;">
                <div class="d-flex align-items-center w-100">
                   <div class="mega-icon mr-3"><i class="fal fa-robot" style="font-size: 20px; color: #fb383b;"></i></div>
                   <div class="mega-text">
                      <span style="font-weight: 600; font-size: 16px;">Automation</span>
                      <p style="margin: 0; font-size: 13px; color: #6b7280; line-height: 1.4; margin-top: 2px;">AI Agents & System Workflows</p>
                   </div>
                </div>
                <i class="fal fa-angle-right ml-2" style="color: #9ca3af; font-size: 18px;"></i>
             </a>
             <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="services/ai-agents.html"><i class="fal fa-microchip mr-2" style="color:#6b7280; width: 20px;"></i>AI Agents</a></li>
                <li><a class="dropdown-item" href="services/gohighlevel.html"><i class="fal fa-funnel-dollar mr-2" style="color:#6b7280; width: 20px;"></i>GoHighLevel (GHL)</a></li>
                <li><hr class="dropdown-divider my-2"></li>
                <li><a class="dropdown-item explore-all-link" href="services.html">Explore All <i class="fal fa-arrow-right"></i></a></li>
             </ul>
          </li>

          <!-- Creative -->
          <li class="dropdown-submenu w-100 mb-1">
             <a class="dropdown-item mega-item d-flex justify-content-between align-items-center" href="services.html" style="padding: 15px; border-radius: 8px;">
                <div class="d-flex align-items-center w-100">
                   <div class="mega-icon mr-3"><i class="fal fa-pen-nib" style="font-size: 20px; color: #fb383b;"></i></div>
                   <div class="mega-text">
                      <span style="font-weight: 600; font-size: 16px;">Creative</span>
                      <p style="margin: 0; font-size: 13px; color: #6b7280; line-height: 1.4; margin-top: 2px;">UI/UX, Video & Branding</p>
                   </div>
                </div>
                <i class="fal fa-angle-right ml-2" style="color: #9ca3af; font-size: 18px;"></i>
             </a>
             <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="services/ui-ux-design.html"><i class="fal fa-mobile-alt mr-2" style="color:#6b7280; width: 20px;"></i>UI/UX Design</a></li>
                <li><a class="dropdown-item" href="services/graphic-design.html"><i class="fal fa-swatchbook mr-2" style="color:#6b7280; width: 20px;"></i>Graphic Design</a></li>
                <li><hr class="dropdown-divider my-2"></li>
                <li><a class="dropdown-item explore-all-link" href="services.html">Explore All <i class="fal fa-arrow-right"></i></a></li>
             </ul>
          </li>

          <!-- Sales & Marketing -->
          <li class="dropdown-submenu w-100">
             <a class="dropdown-item mega-item d-flex justify-content-between align-items-center" href="services.html" style="padding: 15px; border-radius: 8px;">
                <div class="d-flex align-items-center w-100">
                   <div class="mega-icon mr-3"><i class="fal fa-bullhorn" style="font-size: 20px; color: #fb383b;"></i></div>
                   <div class="mega-text">
                      <span style="font-weight: 600; font-size: 16px;">Sales & Marketing</span>
                      <p style="margin: 0; font-size: 13px; color: #6b7280; line-height: 1.4; margin-top: 2px;">Growth, Email & Campaigns</p>
                   </div>
                </div>
                <i class="fal fa-angle-right ml-2" style="color: #9ca3af; font-size: 18px;"></i>
             </a>
             <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="services/linkedin-growth.html"><i class="fab fa-linkedin-in mr-2" style="color:#6b7280; width: 20px;"></i>LinkedIn Growth</a></li>
                <li><a class="dropdown-item" href="services/digital-marketing.html"><i class="fal fa-chart-line mr-2" style="color:#6b7280; width: 20px;"></i>Digital Marketing</a></li>
                <li><hr class="dropdown-divider my-2"></li>
                <li><a class="dropdown-item explore-all-link" href="services.html">Explore All <i class="fal fa-arrow-right"></i></a></li>
             </ul>
          </li>

       </ul>
    </div>
</div>
'''

match = re.search(r'(?s)(<div id="servicesDropdown" class="dropdown-menus collapse mega-menu-container">)(.*?)(</li>)', html)
if match:
    new_html = html[:match.start()] + new_menu + '\n                  </li>' + html[match.end():]
    with open('c:/Users/my/Desktop/chatgpt/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Injected ultra-premium nested dropdown into index.html")
else:
    print("Could not find dropdown block.")
