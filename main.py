import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20210228'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
title_list = soup.select('div.info-movie')
for i in title_list:
    print(i.select_one('a > strong').text.strip()) # strip = 공백 제거. text = 텍스트만 가져옴 ==> 제목만 가져온다.