import re

file_path = 'c:/Users/my/Desktop/chatgpt/css/custom.css'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace left: -100% and left: 0 with transform logic for buttery smooth 60fps animation
content = re.sub(
    r'left:\s*-100%\s*!important;',
    r'left: 0 !important;\n        transform: translateX(-100%);\n        transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;',
    content
)

content = re.sub(
    r'#navigration\s*\.sidenav\.active-nav\s*\{\s*left:\s*0\s*!important;\s*\}',
    r'#navigration .sidenav.active-nav {\n          transform: translateX(0) !important;\n      }',
    content
)

# Also fix the 0.4s transition in the old code block
content = re.sub(
    r'transition:\s*\.4s;',
    r'transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);',
    content
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Optimized mobile menu animation to 60fps hardware acceleration.")
