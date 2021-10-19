import os
import re
import requests
import json
from bs4 import BeautifulSoup
from github import Github
from datetime import datetime
from pytz import timezone
from urllib.request import urlopen
from html import unescape

seoul_timezone = timezone('Asia/Seoul')
today = datetime.now(seoul_timezone)
today_date = today.strftime("%Y년 %m월 %d일")

url = 'https://kleague.com/api/clubRank.do'
req = requests.get(url)
html = req.content
soup = BeautifulSoup(html, 'html.parser')
rank_json=json.loads(soup.text)
rank1 = []
rank2 = []
rank1 = rank_json["data"]["league1"]
rank2 = rank_json["data"]["league2"]
rank_zip = rank1 + rank2
league_ranking = json.dumps(rank_zip, ensure_ascii=False, indent="\t")

access_token = os.environ['MY_GITHUB_TOKEN']
repository_name = "database" # 내 저장소 이름 필수로 바꿔야함 

repo = Github(access_token).get_user().get_repo(repository_name)

issue_title = f"K리그 순위 ({today_date})"

if league_ranking != '' and repository_name == repo.name:
    # reg = repo.create_issue(title=issue_title, body=league_ranking)
with open('rank.json', 'w+',encoding='utf-8') as write_file:
    reg = json.dump(league_ranking, write_file, ensure_ascii = False, indent='\t')
    
    print(reg)