import urllib.request
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
titles = soup.find_all(class_ = 'api_txt_lines')

for i in titles:
    print(i.select_one('api_txt_lines.total_tit'))