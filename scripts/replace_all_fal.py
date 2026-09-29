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
            
            # Replace all fal with fa to ensure compatibility with FontAwesome 4.7
            content = re.sub(r'\bfal\b', 'fa', content)
            
            if content != original:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
        except Exception as e:
            pass

print(f"Replaced all fal icons globally in {count} files.")
