import glob

directory = 'c:/Users/my/Desktop/chatgpt'
html_files = glob.glob(f'{directory}/**/*.html', recursive=True)
count = 0

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        original = content
        
        # Find index of footer
        footer_idx = content.lower().find('<footer')
        if footer_idx != -1:
            # split at footer
            pre_footer = content[:footer_idx]
            post_footer = content[footer_idx:]
            
            # replace logo in post_footer
            post_footer = post_footer.replace('img/logo.png', 'img/logo-dark.png')
            
            content = pre_footer + post_footer
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print(f"Updated footer to logo-dark in {count} HTML files.")
