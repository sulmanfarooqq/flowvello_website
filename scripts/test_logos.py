import urllib.request

urls = {
    'OpenAI': 'https://cdn.worldvectorlogo.com/logos/openai-2.svg',
    'HubSpot': 'https://cdn.worldvectorlogo.com/logos/hubspot.svg',
    'AWS': 'https://cdn.worldvectorlogo.com/logos/aws-2.svg',
    'Salesforce': 'https://cdn.worldvectorlogo.com/logos/salesforce-2.svg',
    'Make': 'https://cdn.worldvectorlogo.com/logos/make-3.svg'
}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        print(f"{name}: {res.getcode()}")
    except Exception as e:
        print(f"{name}: FAILED - {e}")
