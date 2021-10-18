import requests
from bs4 import BeautifulSoup
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print('뉴스기사 스크래핑 시작')

url = 'https://www.yna.co.kr/safe/news'
req = requests.get(url)
#req.encoding= None
html = req.content
soup = BeautifulSoup(html, 'html.parser')

url1 = 'https://kleague.com/api/clubRank.do'
req1 = requests.get(url1)
html1 = req1.content
soup1 = BeautifulSoup(html1, 'html.parser')
site_json=json.loads(soup1.content)


datas = soup.select(
    'div.contents > div.content01 > div > ul > li >article > div >h3'
    )

data = []

for title in datas:   
    name = title.find_all('a')[0].text
    url = 'http:'+title.find('a')['href']
    data[name] = url

with open(os.path.join(BASE_DIR, 'news.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')

print('뉴스기사 스크래핑 끝')
