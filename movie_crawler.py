import requests
from bs4 import BeautifulSoup

date = input("원하는 날짜를 입력하시오.").split()

month = date[0]
day = date[1]

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
print(str(month) + "월 " + str(date[1]) + "일에는")
for imax in imax_list:
    if(imax):
        imax = imax.find_parent('div', class_='type-hall')
        timetabel = imax.select('em')
        lst = []
        for playtime in timetabel:
            lst.append(playtime.text.strip())
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        time = imax.select_one('div.info-movie > i:nth-child(6)').text.strip()
        genre = imax.select_one('div.info-movie > i:nth-child(5)').text.strip()
        print(title + " IMAX가 열렸습니다. \n" + title + "의 상영시간은 " + time + " 입니다.\n" + "장르는 " + genre + "입니다.")
        print("관람할 수 있는 시간은 " + str(lst)[1:-1] + " 입니다.")
    else:
        print("IMAX Not Open")