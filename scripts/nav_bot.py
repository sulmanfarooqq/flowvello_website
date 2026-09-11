import re

with open('c:/Users/my/Desktop/chatgpt/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Quick Meeting button to navbar
old_nav_btn = '<a class="fv-dual-btn d-none d-lg-inline-flex ml-lg-4" href="contact.html">'
new_nav_btn = '''
<a class="fv-dual-btn d-none d-lg-inline-flex ml-lg-4" href="contact.html" style="background: transparent !important; border: 1px solid #fb383b !important; padding: 10px 24px; border-radius: 50px;">
    <span class="fv-btn-pill" style="color: #fb383b;">QUICK MEETING</span>
</a>
<a class="fv-dual-btn d-none d-lg-inline-flex ml-lg-2" href="contact.html">
'''

content = content.replace(old_nav_btn, new_nav_btn)

# Add chatbot widget just before </body>
chatbot_html = '''
<!-- AI CHATBOT INTEGRATION -->
<div id="ai-chatbot-widget" class="wow bounceInUp" data-wow-delay="1.5s" style="position: fixed; bottom: 30px; right: 30px; z-index: 9999;">
    <a href="contact.html" style="display: flex; align-items: center; justify-content: center; width: 60px; height: 60px; background-color: #111827; border: 2px solid #fb383b; border-radius: 50%; box-shadow: 0 4px 12px rgba(0,0,0,0.15); text-decoration: none; cursor: pointer; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.1)';" onmouseout="this.style.transform='scale(1)'">
        <i class="fal fa-comment-alt-lines" style="color: #ffffff; font-size: 24px;"></i>
    </a>
</div>
</body>
'''
content = content.replace('</body>', chatbot_html)

with open('c:/Users/my/Desktop/chatgpt/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Nav and chatbot updated.')
