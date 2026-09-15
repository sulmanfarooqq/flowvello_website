import glob
import re

directory = 'c:/Users/my/Desktop/chatgpt'
html_files = glob.glob(f'{directory}/**/*.html', recursive=True)
count = 0

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        original = content
        
        # Replace the softoweb placeholder anywhere in the footer
        footer_logo = '<img src="img/logo-dark.png" alt="Techtox Logo" style="height:28px; width: auto; margin-right:12px;">'
        
        content = re.sub(
            r'<img[^>]*src="img/softoweb\.webp"[^>]*>\s*Techtox', 
            footer_logo, 
            content, 
            flags=re.IGNORECASE
        )
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print(f"Aggressively updated footer logo in {count} HTML files.")
