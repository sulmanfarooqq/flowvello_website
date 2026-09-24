import glob
import re

directory = 'c:/Users/my/Desktop/chatgpt'
html_files = glob.glob(f'{directory}/**/*.html', recursive=True)
css_files = glob.glob(f'{directory}/**/*.css', recursive=True)

# 1. Update logos to be larger and consistent
count_logos = 0
for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        original = content
        # Update desktop logo height to 45px
        content = re.sub(r'style="height:\s*35px;\s*width:\s*auto;"', 'style="height: 45px; width: auto;"', content)
        # Update mobile logo height to 45px
        content = re.sub(r'style="height:\s*30px;\s*width:\s*auto;"', 'style="height: 45px; width: auto;"', content)
        # Update footer logo height to 40px
        content = re.sub(r'style="height:28px;\s*width:\s*auto;\s*margin-right:12px;"', 'style="height:40px; width: auto; margin-right:12px;"', content)
        
        # Inject Google Fonts for Sora if it doesn't exist
        if 'fonts.googleapis.com/css2?family=Sora' not in content:
            sora_link = '<link href="https://fonts.googleapis.com/css2?family=Sora:wght@100;200;300;400;500;600;700;800&display=swap" rel="stylesheet">'
            # find </title> and insert after
            content = re.sub(r'(</title>)', r'\1\n    ' + sora_link, content, flags=re.IGNORECASE)
        
        # Replace inline font-families
        content = re.sub(r"font-family:\s*'?Rubik'?,?\s*sans-serif;?", "font-family: 'Sora', sans-serif;", content, flags=re.IGNORECASE)
        content = re.sub(r"font-family:\s*'?Teko'?,?\s*sans-serif;?", "font-family: 'Sora', sans-serif;", content, flags=re.IGNORECASE)
        content = re.sub(r"font-family:\s*'?Inter'?,?\s*sans-serif;?", "font-family: 'Sora', sans-serif;", content, flags=re.IGNORECASE)
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            count_logos += 1
    except Exception as e:
        pass

print(f"Updated logos & inline fonts in {count_logos} HTML files.")

# 2. Update CSS files to use Sora
count_css = 0
for file_path in css_files:
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        original = content
        
        content = re.sub(r"font-family:\s*'?Rubik'?,?\s*sans-serif;?", "font-family: 'Sora', sans-serif;", content, flags=re.IGNORECASE)
        content = re.sub(r"font-family:\s*'?Teko'?,?\s*sans-serif;?", "font-family: 'Sora', sans-serif;", content, flags=re.IGNORECASE)
        content = re.sub(r"font-family:\s*'?Inter'?,?\s*sans-serif;?", "font-family: 'Sora', sans-serif;", content, flags=re.IGNORECASE)
        content = re.sub(r"font-family:\s*'?Outfit'?,?\s*sans-serif;?", "font-family: 'Sora', sans-serif;", content, flags=re.IGNORECASE)
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            count_css += 1
    except Exception as e:
        pass

print(f"Updated global fonts to Sora in {count_css} CSS files.")
