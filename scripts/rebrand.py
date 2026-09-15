import glob
import re
import os
import shutil

directory = 'c:/Users/my/Desktop/chatgpt'
html_files = glob.glob(f'{directory}/**/*.html', recursive=True)
js_files = glob.glob(f'{directory}/**/*.js', recursive=True)
css_files = glob.glob(f'{directory}/**/*.css', recursive=True)
all_files = html_files + js_files + css_files

count = 0

for file_path in all_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original = content
        
        # Replace exact domain
        content = re.sub(r'flowvello\.com', 'techtox.com', content, flags=re.IGNORECASE)
        content = re.sub(r'contact@flowvello\.com', 'contact@techtox.com', content, flags=re.IGNORECASE)
        
        # Replace variations of the name
        content = re.sub(r'\bFlow Vello\b', 'Techtox', content, flags=re.IGNORECASE)
        content = re.sub(r'\bFlowVello\b', 'Techtox', content, flags=re.IGNORECASE)
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
    except Exception as e:
        print(f"Error on {file_path}: {e}")

print(f"Rebranded {count} files from Flow Vello to Techtox.")

# Copy the logo
src_img = r"C:\Users\my\.gemini\antigravity\brain\7bb54674-e008-4391-b404-f701fc0f504b\.user_uploaded\media_1789476325894.png"
dest_img_png = r"c:\Users\my\Desktop\chatgpt\img\logo.png"
dest_img_webp = r"c:\Users\my\Desktop\chatgpt\img\logo.webp"

if os.path.exists(src_img):
    shutil.copy(src_img, dest_img_png)
    shutil.copy(src_img, dest_img_webp)
    print("Logo updated.")
else:
    print("Could not find uploaded image.")
