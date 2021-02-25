import requests
from bs4 import BeautifulSoup

date = input("원하는 날짜를 입력하시오.").split()

if len(date[0]) == 1:
    date[0] = "0" + date[0]
if len(date[1]) == 1:
    date[1] = "0" + date[1]

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=2021'

url = url + date[0] + date[1]

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