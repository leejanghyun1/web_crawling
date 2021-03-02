import requests
from bs4 import BeautifulSoup

url = 'http://web.archive.org/web/20140301191716/http://pokemondb.net/pokedex/national'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

name = soup.find_all(classs_ = 'ent-name')
print(name)