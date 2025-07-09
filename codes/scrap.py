import requests
from bs4 import BeautifulSoup

# 1. Récupérer la page
url = 'https://blog.python.org'
response = requests.get(url)
html = response.text

# 2. Parser le HTML
soup = BeautifulSoup(html, 'html.parser')

# 3. Extraire les titres d’articles
titles = soup.find_all('h3', class_='post-title')

# 4. Afficher les titres
for title in titles:
    print(title.get_text(strip=True))
