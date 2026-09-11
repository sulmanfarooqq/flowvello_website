import urllib.request
urls = [
    'https://images.unsplash.com/photo-1432821596592-e2c18b78144f',
    'https://images.unsplash.com/photo-1512314889357-e157c22f938d',
    'https://images.unsplash.com/photo-1533750516457-a7f992034fec', # digital marketing laptop
    'https://images.unsplash.com/photo-1557804506-669a67965ba0' # abstract email/marketing
]
for url in urls:
    try:
        urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
        print(f"OK: {url}")
    except:
        print(f"FAIL: {url}")
