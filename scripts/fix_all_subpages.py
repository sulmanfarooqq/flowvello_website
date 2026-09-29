import glob
import re

directories = ['c:/Users/my/Desktop/chatgpt/services', 'c:/Users/my/Desktop/chatgpt/industries']

count = 0
for directory in directories:
    html_files = glob.glob(f'{directory}/*.html')
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            original = content
            
            # 1. Desktop Nav Logo (fixing industries which missed the last script)
            content = re.sub(
                r'<a class="logo" href="\.\./index\.html">Techtox</a>',
                r'<a class="logo d-flex align-items-center" href="../index.html" style="text-decoration: none;"><img src="../img/logo.png" alt="Techtox Logo" style="height: 45px; width: auto;"></a>',
                content
            )
            
            # 2. Mobile Nav Logo (fixing industries)
            content = re.sub(
                r'<a class="logo d-lg-none" href="\.\./index\.html">Techtox</a>',
                r'<a class="logo d-lg-none d-flex align-items-center" href="../index.html" style="text-decoration: none;"><img src="../img/logo.png" alt="Techtox Logo" style="height: 45px; width: auto;"></a>',
                content
            )
            
            # 3. Footer Logo (fixing industries)
            content = re.sub(
                r'<a class="logo d-flex align-items-center" href="\.\./index\.html">\s*<img src="\.\./img/softoweb\.png"[^>]*>\s*Techtox\s*</a>',
                r'<a class="logo d-flex align-items-center" href="../index.html" style="text-decoration: none;"><img src="../img/logo-dark.png" alt="Techtox Logo" style="height:40px; width: auto; margin-right:12px;"></a>',
                content,
                flags=re.IGNORECASE | re.DOTALL
            )
            
            # 4. Fix hamburger menu icon paths
            content = re.sub(r'src="img/icon/menu\.webp"', r'src="../img/icon/menu.webp"', content)
            content = re.sub(r'src="img/icon/letter-x\.webp"', r'src="../img/icon/letter-x.webp"', content)
            # just in case it was png in some files
            content = re.sub(r'src="img/icon/menu\.png"', r'src="../img/icon/menu.webp"', content)
            content = re.sub(r'src="img/icon/letter-x\.png"', r'src="../img/icon/letter-x.webp"', content)
            
            # 5. Fix favicons in industries
            content = re.sub(r'href="img/favicon\.png"', r'href="../img/favicon.png"', content)
            content = re.sub(r'href="img/favicon\.ico"', r'href="../img/favicon.ico"', content)

            # 6. Fix dropdown menu missing icons turning into red blocks
            # If the icon font doesn't have fal, let's just make sure there is no red background on the <i> tags.
            # Wait, the screenshot shows solid red squares with no icon inside.
            # Let's replace the inline style of the i tags in the dropdown:
            # Replace style="width:20px; color:#FF2E3E; margin-right:8px;" with style="width:20px; color:#FF2E3E; margin-right:8px; background:transparent;"
            content = re.sub(
                r'style="width:20px; color:#FF2E3E; margin-right:8px;"',
                r'style="width:20px; color:#FF2E3E; margin-right:8px; background:transparent; display:inline-block; text-align:center;"',
                content
            )
            
            # Replace "fal" with "fa" or "fas" if it's missing in FontAwesome 4.7
            content = re.sub(r'class="fal fa-browser"', r'class="fa fa-globe"', content)
            content = re.sub(r'class="fal fa-gamepad"', r'class="fa fa-gamepad"', content)
            content = re.sub(r'class="fab fa-wordpress"', r'class="fa fa-wordpress"', content)
            content = re.sub(r'class="fab fa-shopify"', r'class="fa fa-shopping-bag"', content)
            content = re.sub(r'class="fal fa-desktop"', r'class="fa fa-desktop"', content)
            content = re.sub(r'class="fal fa-robot"', r'class="fa fa-android"', content)
            content = re.sub(r'class="fal fa-chart-network"', r'class="fa fa-line-chart"', content)
            content = re.sub(r'class="fal fa-headset"', r'class="fa fa-headphones"', content)
            content = re.sub(r'class="fal fa-plug"', r'class="fa fa-plug"', content)
            content = re.sub(r'class="fal fa-layer-group"', r'class="fa fa-cubes"', content)
            
            if content != original:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
        except Exception as e:
            print(f"Error on {file_path}: {e}")

print(f"Fixed {count} nested sub-pages.")
