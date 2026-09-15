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
        
        # We only want to replace it in the footer section.
        # Find the footer section and do the replacement.
        def replace_footer_logo(match):
            footer_content = match.group(0)
            updated_footer = footer_content.replace('img/logo.png', 'img/logo-dark.png')
            return updated_footer
            
        content = re.sub(r'<footer.*?</footer>', replace_footer_logo, content, flags=re.IGNORECASE | re.DOTALL)
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print(f"Updated footer to use logo-dark.png in {count} HTML files.")
