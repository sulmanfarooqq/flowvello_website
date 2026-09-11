import re

with open('c:/Users/my/Desktop/chatgpt/services.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'(?s)<section class="fv-services-presentation[^>]*>(.*?)</section>', html)
if match:
    content = match.group(1)
    # find all departments
    depts = re.findall(r'<h2[^>]*>(.*?)</h2>', content)
    print("Departments found:", depts)
