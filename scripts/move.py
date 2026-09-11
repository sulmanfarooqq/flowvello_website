import re

with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(?s)(<!-- CORE SERVICES \(CAROUSEL\) -->.*?</section>)', content)
if match:
    services_block = match.group(1)
    content = content.replace(services_block, '')
    
    hero_start = content.find('id="homeSection"')
    hero_end = content.find('</section>', hero_start) + 10
    
    content = content[:hero_end] + '\n\n   ' + services_block + content[hero_end:]
    
    with open('c:/Users/my/Desktop/chatgpt/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Services successfully moved.')
else:
    print('Could not find CORE SERVICES block.')
