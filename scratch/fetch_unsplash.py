import urllib.request
import re

url = "https://unsplash.com/photos/white-wall-paint-with-white-light-nL51SgR98Yg"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    match = re.search(r'https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+', html)
    if match:
        img_url = match.group(0) + "?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80"
        print(f"FOUND: {img_url}")
    else:
        print("Not found")
except Exception as e:
    print(e)
