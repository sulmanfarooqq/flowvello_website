import re

file_path = 'c:/Users/my/Desktop/chatgpt/css/custom.css'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

fix_css = """
#navigration .dropdown-item {
    pointer-events: auto !important;
    cursor: pointer !important;
    z-index: 100 !important;
    position: relative !important;
}
"""

if 'pointer-events: auto !important;' not in content:
    content += fix_css

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Forced pointer-events on dropdown items to guarantee clickability.")
