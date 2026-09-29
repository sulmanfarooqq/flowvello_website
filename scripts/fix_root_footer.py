import glob
import re

html_files = glob.glob('c:/Users/my/Desktop/chatgpt/*.html')

count = 0
for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        original = content
        
        # Replace softoweb.png footer logo in root HTML files
        content = re.sub(
            r'<a class="logo d-flex align-items-center" href="index\.html">\s*<img src="img/softoweb\.png"[^>]*>\s*Techtox\s*</a>',
            r'<a class="logo d-flex align-items-center" href="index.html" style="text-decoration: none;"><img src="img/logo-dark.png" alt="Techtox Logo" style="height:40px; width: auto; margin-right:12px;"></a>',
            content,
            flags=re.IGNORECASE | re.DOTALL
        )
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
    except Exception as e:
        print(e)

print(f"Fixed root footer logos in {count} pages.")
