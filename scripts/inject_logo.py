import glob
import re

directory = 'c:/Users/my/Desktop/chatgpt'
html_files = glob.glob(f'{directory}/**/*.html', recursive=True)

favicon_tags = """
    <!-- FAVICON -->
    <link rel="icon" type="image/png" href="img/favicon.png">
    <link rel="shortcut icon" href="img/favicon.ico">
"""

navbar_logo_full = '<a class="logo d-flex align-items-center" href="index.html" style="text-decoration: none;"><img src="img/logo.png" alt="Techtox Logo" style="height: 35px; width: auto;"></a>'
navbar_logo_mobile = '<a class="logo d-lg-none d-flex align-items-center" href="index.html" style="text-decoration: none;"><img src="img/logo.png" alt="Techtox Logo" style="height: 30px; width: auto;"></a>'
footer_logo = '<img src="img/logo.png" alt="Techtox Logo" style="height:28px; width: auto; margin-right:12px;">'

count = 0

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        original = content
        
        # 1. Add Favicon if not exists
        if 'img/favicon.png' not in content:
            content = re.sub(r'(</head>)', f"{favicon_tags}\\1", content, flags=re.IGNORECASE)
            
        # 2. Fix Navbar Logo (Desktop)
        content = re.sub(r'<a class="logo"\s+href="index\.html">Techtox</a>', navbar_logo_full, content, flags=re.IGNORECASE)
        
        # 3. Fix Navbar Logo (Mobile)
        content = re.sub(r'<a class="logo d-lg-none"\s+href="index\.html">Techtox</a>', navbar_logo_mobile, content, flags=re.IGNORECASE)
        
        # 4. Fix Footer Logo
        content = re.sub(r'<img src="img/softoweb\.webp"[^>]*>\s*Techtox', footer_logo, content, flags=re.IGNORECASE)
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print(f"Injected production logo and favicon into {count} HTML files.")
