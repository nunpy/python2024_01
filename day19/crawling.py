#crawling

# 파이썬 문법: [변수, 연산자, 제어문, 함수, 클래스, 상속, 예외처리...]
# 파이썬으로 프로그램 만들기:
# 1. 데이터 분석(pandas) 2. 인공지능(tensorflow, keras) 3. 웹 서버(django, flask)
# 크롤링 -> 웹사이트 정보 가져오기

from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/sise/"
response = requests.get(url)
response.encoding = 'cp949'
html = response.text
soup = BeautifulSoup(html, 'html.parser')

itemList = soup.find(id="popularItemList")
li_list = itemList.find_all('li')

for i in li_list:
    print(i.find('a').text)
    print(i.find('span').text)

# stockList = []
# for i in li_list:
#     stockList.append({companyl i find('a').text, 'price' in find})