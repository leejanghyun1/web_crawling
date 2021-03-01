import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
variations = soup.find_all('em', class_ = 'info_variation')
corona_url = 'http://ncov.mohw.go.kr/'
html = requests.get(corona_url)
soup = BeautifulSoup(html.text, 'html.parser')
date = soup.find('span', class_ = 'livedate').text.strip()[1:13]
print(date)
lst = [date]
for variation in variations:
    lst.append(variation.text.strip() + ' ↑')
print(lst[0:-2])
df = pd.DataFrame([lst[0:-2]], columns=['날짜','확진자 수', '검사 중', '격리 해제', '사망자 수'])
df.to_csv('/Users/jjanghyoni/Desktop/corona.csv', index= False, encoding='cp949')