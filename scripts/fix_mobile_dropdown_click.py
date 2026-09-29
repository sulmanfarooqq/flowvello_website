import re

file_path = 'c:/Users/my/Desktop/chatgpt/css/custom.css'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add CSS rules to make sure the dropdown menu is visible on mobile when .show is added by Bootstrap JS
fix_css = """
#navigration .collapse.show,
#navigration .dropdown-menus.show {
    opacity: 1 !important;
    visibility: visible !important;
    z-index: 99 !important;
    display: block !important;
}
"""

# inject it safely
if '#navigration .collapse.show' not in content:
    content += fix_css

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed mobile dropdown visibility on click.")
