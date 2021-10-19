import os
import sys
import requests
import json
from bs4 import BeautifulSoup
from github import Github
from datetime import datetime
from pytz import timezone

seoul_timezone = timezone('Asia/Seoul')
today = datetime.now(seoul_timezone)
today_date = today.strftime("%Y년 %m월 %d일")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
rank = dict()

url = 'https://kleague.com/api/clubRank.do'
req = requests.get(url)
html = req.content
soup = BeautifulSoup(html, 'html.parser')
rank = json.loads(soup.text)

access_token = os.environ['MY_GITHUB_TOKEN']
repository_name = "database" # 내 저장소 이름 필수로 바꿔야함 

repo = Github(access_token).get_user().get_repo(repository_name)
# repo.create_file("rank.json", "commit message", rank)

print(today_date)

file = open("./naver.json", "w")

url = "https://search.shopping.naver.com/search/all?query=%EA%B1%B4%EC%A1%B0%EA%B8%B0&cat_id=&frm=NVSHATC"
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
cnt = len(soup.find_all('div', class_='basicList_title__3P9Q7'))

for i in range(0,cnt) :
    naver = {}
    metadata = soup.find_all('div', class_='basicList_title__3P9Q7')[i]
    title = metadata.a.get('title')
    print("<제품명> : ", title)               # title
    
    price = soup.find_all('span', class_='price_num__2WUXn')[i].text
    print("<가격> : ", price)                # 가격
    
    url = metadata.a.get('href')
    print("<url> : ", url)                  # url
         
    print("===================================================")
    
    naver = {'제품명' : title , '가격' : price, 'url' : url }
    file.write(json.dumps(naver))

file.close()

html_file = open('html_file.html', 'w')
html_file.write(html_text)
html_file.close()

'''
with open(os.path.join(BASE_DIR, 'rank.json'), 'w+', encoding="utf-8") as make_file:
    reg = json.dump(rank_json, make_file, ensure_ascii = False, indent="\t")
print(reg)

with open (os.path.join(BASE_DIR, 'rank.json'), "r", encoding="utf-8") as f:
    reg = json.load(f)
print(reg)
'''
