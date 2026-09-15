import os
import glob
import re

directory = 'c:/Users/my/Desktop/chatgpt'
html_files = glob.glob(f'{directory}/**/*.html', recursive=True)
css_files = glob.glob(f'{directory}/**/*.css', recursive=True)
js_files = glob.glob(f'{directory}/**/*.js', recursive=True)
all_files = html_files + css_files + js_files

# Find all potential image references in the code
used_images = set()
pattern = re.compile(r'[\w\-\.]+\.(?:png|jpg|jpeg|gif|webp|svg|ico)', re.IGNORECASE)

for file_path in all_files:
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            matches = pattern.findall(content)
            for match in matches:
                used_images.add(match.lower())
    except:
        pass

# Hardcode some we know we need
used_images.add('logo.png')
used_images.add('logo-dark.png')
used_images.add('favicon.png')
used_images.add('favicon.ico')
used_images.add('logo.webp')
used_images.add('logo-dark.webp')

img_dir = os.path.join(directory, 'img')
all_images = glob.glob(f'{img_dir}/**/*', recursive=True)

deleted_count = 0
for img_path in all_images:
    if os.path.isfile(img_path):
        filename = os.path.basename(img_path).lower()
        if filename not in used_images:
            try:
                os.remove(img_path)
                deleted_count += 1
            except:
                pass

print(f"Deleted {deleted_count} unused images.")
