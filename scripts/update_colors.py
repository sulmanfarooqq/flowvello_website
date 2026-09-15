import os
import glob
import re

directory = 'c:/Users/my/Desktop/chatgpt'
files = glob.glob(f'{directory}/**/*.css', recursive=True) + glob.glob(f'{directory}/**/*.html', recursive=True)

count = 0

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        original = content
        
        # Replace the old red with the new Techtox Red
        content = re.sub(r'#fb383b', '#FF2E3E', content, flags=re.IGNORECASE)
        # Some places might have it in rgb
        content = re.sub(r'251,\s*56,\s*59', '255, 46, 62', content)
        
        # Replace the old dark brand color with pure black
        content = re.sub(r'#222429', '#000000', content, flags=re.IGNORECASE)
        content = re.sub(r'34,\s*36,\s*41', '0, 0, 0', content)
        
        # Replace the tailwind dark slate used in headings with pure black
        content = re.sub(r'#111827', '#000000', content, flags=re.IGNORECASE)
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Update AGENTS.md
agents_path = os.path.join(directory, 'AGENTS.md')
if os.path.exists(agents_path):
    with open(agents_path, 'r', encoding='utf-8') as f:
        agents = f.read()
    agents = re.sub(r'Flow Vello', 'Techtox', agents, flags=re.IGNORECASE)
    agents = re.sub(r'#fb383b', '#FF2E3E', agents, flags=re.IGNORECASE)
    agents = re.sub(r'#222429', '#000000', agents, flags=re.IGNORECASE)
    with open(agents_path, 'w', encoding='utf-8') as f:
        f.write(agents)
    print("AGENTS.md updated.")

print(f"Updated color palette in {count} files.")
