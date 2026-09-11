import re

# Read correct nav from index.html
with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

nav_match = re.search(r'(?s)(<nav id="navigration" class="navbar fixed-top p-0">.*?</nav>)', index_html)
if not nav_match:
    print("Could not find nav in index")
    exit()
correct_nav = nav_match.group(1)

# Inject into about.html
with open('c:/Users/my/Desktop/chatgpt/about.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

new_about_html = re.sub(r'(?s)<nav id="navigration" class="navbar fixed-top p-0">.*?</nav>', correct_nav.replace('\\', '\\\\'), about_html)

with open('c:/Users/my/Desktop/chatgpt/about.html', 'w', encoding='utf-8') as f:
    f.write(new_about_html)

print("Nav repaired in about.html")
