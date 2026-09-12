import glob
import re

files = glob.glob('c:/Users/my/Desktop/chatgpt/*.html') + glob.glob('c:/Users/my/Desktop/chatgpt/services/*.html') + glob.glob('c:/Users/my/Desktop/chatgpt/industries/*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # The exact block to remove:
    # <!-- AI CHATBOT INTEGRATION -->
    # <div id="ai-chatbot-widget" ... </div> (and its a tag)
    
    # We will use regex to find and remove anything from <!-- AI CHATBOT INTEGRATION --> to the closing </a></div>
    pattern = r'(?s)<!-- AI CHATBOT INTEGRATION -->.*?<i class="fal fa-comment-alt-lines".*?</i>\s*</a>\s*</div>'
    html, count = re.subn(pattern, '', html)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Scrubbed dummy chatbot HTML from {filepath}")

