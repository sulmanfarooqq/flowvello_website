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
        
        # 1. Desktop Nav Logo
        content = re.sub(
            r'<a class="logo" href="\.\./index\.html">Techtox</a>',
            r'<a class="logo d-flex align-items-center" href="../index.html" style="text-decoration: none;"><img src="../img/logo.png" alt="Techtox Logo" style="height: 45px; width: auto;"></a>',
            content
        )
        
        # 2. Mobile Nav Logo
        content = re.sub(
            r'<a class="logo d-lg-none" href="\.\./index\.html">Techtox</a>',
            r'<a class="logo d-lg-none d-flex align-items-center" href="../index.html" style="text-decoration: none;"><img src="../img/logo.png" alt="Techtox Logo" style="height: 45px; width: auto;"></a>',
            content
        )
        
        # 3. Footer Logo
        content = re.sub(
            r'<a class="logo d-flex align-items-center" href="\.\./index\.html">\s*<img src="\.\./img/softoweb\.png"[^>]*>\s*Techtox\s*</a>',
            r'<a class="logo d-flex align-items-center" href="../index.html" style="text-decoration: none;"><img src="../img/logo-dark.png" alt="Techtox Logo" style="height:40px; width: auto; margin-right:12px;"></a>',
            content,
            flags=re.IGNORECASE | re.DOTALL
        )
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
    except Exception as e:
        print(f"Error on {file_path}: {e}")

print(f"Fixed nested logos in {count} sub-pages.")
