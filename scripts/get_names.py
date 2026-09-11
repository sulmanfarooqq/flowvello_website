import glob, re
files = glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html')
names = []
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        match = re.search(r'<h1[^>]*>(.*?)</h1>', file.read())
        if match:
            names.append(match.group(1).strip().title())
print(names)
