import glob
import re

directories = [
    'c:/Users/my/Desktop/chatgpt',
    'c:/Users/my/Desktop/chatgpt/services',
    'c:/Users/my/Desktop/chatgpt/industries'
]

count = 0
for directory in directories:
    html_files = glob.glob(f'{directory}/*.html')
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            original = content
            
            # Re-map icons to valid FontAwesome 5 Pro/Brand classes
            content = re.sub(r'class="fa fa-android"', r'class="fal fa-robot"', content)
            content = re.sub(r'class="fa fa-globe"', r'class="fal fa-globe"', content)
            content = re.sub(r'class="fa fa-gamepad"', r'class="fal fa-gamepad"', content)
            content = re.sub(r'class="fa fa-wordpress"', r'class="fab fa-wordpress"', content)
            content = re.sub(r'class="fa fa-shopping-bag"', r'class="fab fa-shopify"', content)
            content = re.sub(r'class="fa fa-chart-pie"', r'class="fal fa-chart-pie"', content)
            content = re.sub(r'class="fa fa-headphones"', r'class="fal fa-headset"', content)
            content = re.sub(r'class="fa fa-plug"', r'class="fal fa-plug"', content)
            content = re.sub(r'class="fa fa-cubes"', r'class="fal fa-layer-group"', content)
            content = re.sub(r'class="fa fa-desktop"', r'class="fal fa-desktop"', content)
            
            # Make sure dropdown icons have correct width and spacing
            content = re.sub(
                r'style="width:20px; color:#FF2E3E; margin-right:8px; background:transparent; display:inline-block; text-align:center;"',
                r'style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"',
                content
            )
            
            if content != original:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
        except Exception as e:
            print(f"Error: {e}")

print(f"Fixed FontAwesome icon mapping in {count} files.")
