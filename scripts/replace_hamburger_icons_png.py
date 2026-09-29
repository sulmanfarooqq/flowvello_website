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
            
            # Replace Open Menu (Hamburger) png/webp
            content = re.sub(
                r'<img src="\.\./img/icon/menu\.(png|webp)"[^>]*>',
                r'<i class="fa fa-bars" style="font-size: 28px; color: #ffffff; cursor: pointer;"></i>',
                content
            )
            
            # Replace Close Menu (X) png/webp
            content = re.sub(
                r'<img src="\.\./img/icon/letter-x\.(png|webp)"[^>]*>',
                r'<i class="fa fa-times" style="font-size: 28px; color: #ffffff; cursor: pointer;"></i>',
                content
            )
            
            if content != original:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
        except Exception as e:
            pass

print(f"Replaced menu images with FontAwesome icons in {count} sub-files.")
