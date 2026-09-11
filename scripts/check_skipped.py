from bs4 import BeautifulSoup
with open('c:/Users/my/Desktop/chatgpt/services.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = soup.find_all('a', class_='shadcn-service-card')
for card in cards:
    title = card.find('h3', class_='shadcn-card-title').get_text(strip=True)
    if card.find('div', class_='shadcn-img-block'):
        print(f"Skipped: {title}")
