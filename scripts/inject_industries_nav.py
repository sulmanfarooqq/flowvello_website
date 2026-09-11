# -*- coding: utf-8 -*-
import glob
import re

files = glob.glob('c:/Users/my/Desktop/chatgpt/*.html') + glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html') + glob.glob('c:/Users/my/Desktop/chatgpt/industries/*.html')

for file_path in files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # Determine if we are in a subfolder
    prefix = '../' if ('/services/' in file_path.replace('\\', '/') or '/industries/' in file_path.replace('\\', '/')) else ''

    industries_nav = f'''
                <li class="nav-item dropdown">
                   <a class="nav-link dropdown-toggle" data-toggle="collapse" href="#industriesDropdown" aria-expanded="false" aria-haspopup="true">Industries <i class="fal fa-angle-down"></i></a>
                   <div id="industriesDropdown" class="dropdown-menus collapse" style="padding: 15px; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); border: 1px solid #e5e7eb; min-width: 260px; background: #ffffff;">
                       <a class="dropdown-item" href="{prefix}industries/real-estate.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fal fa-building" style="width:20px; color:#fb383b; margin-right:8px;"></i> Real Estate</a>
                       <a class="dropdown-item" href="{prefix}industries/b2b-saas.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fal fa-cloud" style="width:20px; color:#fb383b; margin-right:8px;"></i> B2B SaaS</a>
                       <a class="dropdown-item" href="{prefix}industries/ecommerce.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fal fa-shopping-cart" style="width:20px; color:#fb383b; margin-right:8px;"></i> E-Commerce</a>
                       <a class="dropdown-item" href="{prefix}industries/legal.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fal fa-balance-scale" style="width:20px; color:#fb383b; margin-right:8px;"></i> Legal Practices</a>
                       <a class="dropdown-item" href="{prefix}industries/healthcare.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fal fa-heartbeat" style="width:20px; color:#fb383b; margin-right:8px;"></i> Healthcare</a>
                       <a class="dropdown-item" href="{prefix}industries/financial.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fal fa-chart-line" style="width:20px; color:#fb383b; margin-right:8px;"></i> Financial Services</a>
                   </div>
                </li>'''

    # To inject right after the Services dropdown, we need to find the </li> that closes it.
    # The Services dropdown ends with:
    #                 View Master Directory <i class="fal fa-arrow-right ml-2"></i>
    #             </a>
    #         </div>
    #     </div>
    # </div>
    #                   </li>
    
    # We'll use a regex to find the end of the servicesDropdown and insert our industries_nav there.
    # But wait, if we run this script multiple times, it will duplicate. So first we remove any existing industriesDropdown.
    html = re.sub(r'(?s)<li class="nav-item dropdown">\s*<a class="nav-link dropdown-toggle"[^>]*href="#industriesDropdown".*?</li>', '', html)
    
    # Now find the </a>\n            </div>\n        </div>\n    </div>\n</div>\n\n                  </li>
    # and append the industries dropdown.
    search_pattern = r'(<div id="servicesDropdown".*?</div>\s*</div>\s*</div>\s*</div>\s*</li>)'
    match = re.search(search_pattern, html, flags=re.DOTALL)
    if match:
        html = html.replace(match.group(1), match.group(1) + industries_nav)
    else:
        print("Could not find Services dropdown in", file_path)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Industries dropdown injected successfully.")
