import urllib.request

urls = [
    'https://images.unsplash.com/photo-1498050108023-c5249f4df085',
    'https://images.unsplash.com/photo-1552820728-8b83bb6b773f',
    'https://images.unsplash.com/photo-1616469829581-73993eb86b02',
    'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d',
    'https://images.unsplash.com/photo-1517694712202-14dd9538aa97',
    'https://images.unsplash.com/photo-1677442136019-21780ecad995',
    'https://images.unsplash.com/photo-1551288049-bebda4e38f71',
    'https://images.unsplash.com/photo-1519389950473-47ba0277781c',
    'https://images.unsplash.com/photo-1558494949-ef010cbdcc31',
    'https://images.unsplash.com/photo-1460925895917-afdab827c52f',
    'https://images.unsplash.com/photo-1561070791-2526d30994b5',
    'https://images.unsplash.com/photo-1626785774573-4b799315345d',
    'https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d',
    'https://images.unsplash.com/photo-1611162617474-5b21e879e113',
    'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe',
    'https://images.unsplash.com/photo-1611944212129-29977ae1398c',
    'https://images.unsplash.com/photo-1432888117426-1d6ac08ae005',
    'https://images.unsplash.com/photo-1563986768494-4dee2763ff0f',
    'https://images.unsplash.com/photo-1522071820081-009f0129c71c'
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        print(f"OK: {url}")
    except Exception as e:
        print(f"FAILED: {url} - {e}")
