import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20210228'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
imax_list = soup.select('span.imax')

# imax 열린 제목들 나열
for imax in imax_list:
    if(imax):
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        print(title + " IMAX Open")
    else:
        print("IMAX Not Open")