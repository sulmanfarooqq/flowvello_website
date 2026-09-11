import glob, re
for file in glob.glob('c:/Users/my/Desktop/chatgpt/*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'href="about.html"' not in html:
        print(f"MISSING IN ROOT: {file}")
for file in glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'href="../about.html"' not in html and 'href="about.html"' not in html:
        print(f"MISSING IN SERVICES: {file}")
