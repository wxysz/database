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
rank_json=json.loads(soup1.text)

datas = soup.select(
    'div.contents > div.content01 > div > ul > li >article > div >h3'
    )

data = {}

for title in datas:   
    name = title.find_all('a')[0].text
    url = 'http:'+title.find('a')['href']
    data[name] = url

with open(os.path.join(BASE_DIR, 'news.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')

rank1 = []
rank2 = []
rank1 = rank_json["data"]["league1"]
rank2 = rank_json["data"]["league2"]
rank_zip = rank1 + rank2
for league_ranking in rank_zip:
    json.dumps(league_ranking, ensure_ascii=False, indent="\t")

with open(os.path.join(BASE_DIR, 'rank.json'), 'w+',encoding='utf-8') as make_file:
    json.dump(rank_zip, make_file, ensure_ascii = False, indent='\t')
    
print('뉴스기사 스크래핑 끝')
