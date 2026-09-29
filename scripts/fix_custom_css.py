import glob
import re

css_files = glob.glob('c:/Users/my/Desktop/chatgpt/css/*.css')

for file_path in css_files:
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        original = content
        content = re.sub(r'\.fal', '.fa', content)
        content = re.sub(r'active-fal', 'active-fa', content)
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
    except Exception as e:
        pass

print("Fixed CSS to target standard FA classes.")
