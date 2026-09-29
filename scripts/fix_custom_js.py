import re

file_path = 'c:/Users/my/Desktop/chatgpt/js/custom.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'\.fal', '.fa', content)
content = re.sub(r'active-fal', 'active-fa', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed custom.js to target standard FA classes.")
