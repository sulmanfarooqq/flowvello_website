import os
import re
import glob

files = glob.glob('c:/Users/my/Desktop/chatgpt/*.html') + glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html')

new_mega_menu = '''
<div id="servicesDropdown" class="dropdown-menus collapse mega-menu-container">
    <div class="mega-menu-content">
       <div class="mega-column">
          <h3 class="mega-title">Our Departments</h3>
          
          <a class="dropdown-item mega-item" href="{prefix}services.html">
             <div class="mega-icon"><i class="fal fa-browser"></i></div>
             <div class="mega-text">
                <span>Development Department</span>
                <p>Web, Apps & Custom Software</p>
             </div>
          </a>
          
          <a class="dropdown-item mega-item" href="{prefix}services.html">
             <div class="mega-icon"><i class="fal fa-robot"></i></div>
             <div class="mega-text">
                <span>Automation Department</span>
                <p>AI Agents & System Workflows</p>
             </div>
          </a>
          
          <a class="dropdown-item mega-item" href="{prefix}services.html">
             <div class="mega-icon"><i class="fal fa-pen-nib"></i></div>
             <div class="mega-text">
                <span>Creative Development</span>
                <p>UI/UX, Video & Branding</p>
             </div>
          </a>
          
          <a class="dropdown-item mega-item" href="{prefix}services.html">
             <div class="mega-icon"><i class="fal fa-bullhorn"></i></div>
             <div class="mega-text">
                <span>Sales & Marketing</span>
                <p>Growth, Email & SEO Campaigns</p>
             </div>
          </a>

       </div>
    </div>
</div>
'''

for file in files:
    with open(file, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    prefix = '../' if ('services\\' in file or 'services/' in file) else ''
    formatted_menu = new_mega_menu.replace('{prefix}', prefix)

    match = re.search(r'(?s)(<div id="servicesDropdown".*?)(</li>)', content)
    if match:
        new_content = content[:match.start()] + formatted_menu + '\n                  </li>' + content[match.end():]
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Reverted to original dropdown layout with 4 core departments.")
