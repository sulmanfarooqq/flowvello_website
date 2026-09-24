import glob
import re

directory = 'c:/Users/my/Desktop/chatgpt/services'
html_files = glob.glob(f'{directory}/*.html')

count = 0
for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        original = content
        
        # Fix favicon paths
        content = re.sub(r'href="img/favicon\.png"', r'href="../img/favicon.png"', content)
        content = re.sub(r'href="img/favicon\.ico"', r'href="../img/favicon.ico"', content)
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
    except Exception as e:
        pass

print(f"Fixed favicon paths in {count} sub-pages.")
