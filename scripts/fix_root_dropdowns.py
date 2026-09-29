import glob
import re

html_files = glob.glob('c:/Users/my/Desktop/chatgpt/*.html')

count = 0
for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        original = content
        
        # Replace fal with fa in root files for dropdowns
        content = re.sub(
            r'style="width:20px; color:#FF2E3E; margin-right:8px;"',
            r'style="width:20px; color:#FF2E3E; margin-right:8px; background:transparent; display:inline-block; text-align:center;"',
            content
        )
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
        pass

print(f"Fixed dropdown icons in {count} root HTML files.")
