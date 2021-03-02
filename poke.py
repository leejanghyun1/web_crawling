import requests
from bs4 import BeautifulSoup

url = 'https://pokemon.fandom.com/ko/wiki/%EC%A0%84%EA%B5%AD%EB%8F%84%EA%B0%90'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

pokemons = soup.find_all('tr', class_ = 'bg-white')

for pokemon in pokemons:
    num = pokemon.select_one('tr.bg-white > td:nth-child(2)').text.strip()[1:]
    name = pokemon.select_one('tr.bg-white > td:nth-child(4) > a').text.strip()
    types = pokemon.select('span.split-cell.text-white')
    type = []
    for t in types:
        type.append(t.text.strip())
    type = str(type)[1:-1].replace("'", "")
    print(num, '', name, '', type)
