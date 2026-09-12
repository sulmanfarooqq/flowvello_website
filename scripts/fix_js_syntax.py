with open('c:/Users/my/Desktop/chatgpt/js/chatbot.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the first " after SYSTEM_PROMPT = \n with a backtick
# and replace the last "; before ar conversationHistory with a backtick

import re

# Find the start of the bad string
start_idx = js.find('var SYSTEM_PROMPT = \n"')
if start_idx != -1:
    # Replace that specific double quote with a backtick
    js = js[:start_idx + 21] + '' + js[start_idx + 22:]
    
    # Find the end of the bad string (right before var conversationHistory)
    end_idx = js.find('";\n\n   var conversationHistory')
    if end_idx != -1:
        js = js[:end_idx] + '' + js[end_idx + 1:]
        
with open('c:/Users/my/Desktop/chatgpt/js/chatbot.js', 'w', encoding='utf-8') as f:
    f.write(js)
