'''
pip install beautifulsoup4
'''
import requests
from bs4 import BeautifulSoup

# Naver 접속 후 네이버에 있는 글자데이터 가져오기
# 외부 개발자가 접속해서 데이터 가져오기 차단한 상태
# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98%EB%AA%85%EC%96%B8&ackey=j904enlb
url="https://search.naver.com/search.naver?query=오늘의명언"
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
print(soup.find('p', class_="ingkr").text)
