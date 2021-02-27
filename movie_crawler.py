import requests
from bs4 import BeautifulSoup
import pandas as pd

date = input("원하는 날짜를 입력하시오.").split()

month = str(date[0])
day = str(date[1])
month_day = month+"월 " + day + "일"

if len(date[0]) == 1:
    date[0] = "0" + date[0]
if len(date[1]) == 1:
    date[1] = "0" + date[1]

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=2021'

url = url + date[0] + date[1]
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
imax_list = soup.select('span.imax')
forDX_list = soup.select('span.forDX')
csv = []
# imax 열린 제목들 나열
print(month + "월 " + day + "일에는")
for imax in imax_list:
    if(imax):
        imax = imax.find_parent('div', class_='type-hall')
        timetabel = imax.select('em')
        lst = []
        for playtime in timetabel:
            lst.append(playtime.text.strip())
        lst = str(lst)[1:-1].replace("'", "")
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        time = imax.select_one('div.info-movie > i:nth-child(6)').text.strip()
        genre = imax.select_one('div.info-movie > i:nth-child(5)').text.strip()
        excel = [month_day,'IMAX',title, genre, time, lst]
        csv.append(excel)
        print(title + " IMAX가 열렸습니다. \n" + title + "의 상영시간은 " + time + " 입니다.\n" + "장르는 " + genre + "입니다.")
        print("관람할 수 있는 시간은 " + lst + " 입니다.")
    else:
        print("IMAX Not Open")
for forDX in forDX_list:
    if(forDX):
        forDX = forDX.find_parent('div', class_='type-hall')
        timetabel = forDX.select('em')
        lst = []
        for playtime in timetabel:
            lst.append(playtime.text.strip())
        lst = str(lst)[1:-1].replace("'", "")
        forDX = forDX.find_parent('div', class_='col-times')
        title = forDX.select_one('div.info-movie > a > strong').text.strip()
        time = forDX.select_one('div.info-movie > i:nth-child(6)').text.strip()
        genre = forDX.select_one('div.info-movie > i:nth-child(5)').text.strip()
        excel = [month_day,'4DX',title, genre, time, lst]
        csv.append(excel)
        print(title + " 4DX가 열렸습니다. \n" + title + "의 상영시간은 " + time + " 입니다.\n" + "장르는 " + genre + "입니다.")
        print("관람할 수 있는 시간은 " + lst + " 입니다.")
    else:
        print("IMAX Not Open")
df = pd.DataFrame(csv, columns=['날짜','영화관','제목', '장르', '상영 시간', '관람 시간'])
df.to_csv('/Users/jjanghyoni/Desktop/Movie.csv', index= False, encoding='cp949')