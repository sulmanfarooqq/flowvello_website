# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re

with open('c:/Users/my/Desktop/chatgpt/scripts/services_backup.html', 'r', encoding='utf-16') as f:
    backup_html = f.read()

soup_backup = BeautifulSoup(backup_html, 'html.parser')
dept_blocks = soup_backup.find_all('div', class_='w-full')

names = []
for block in dept_blocks:
    header = block.find('h2')
    if header:
        names.append(header.get_text(strip=True))

print("Names found in backup:", names)
