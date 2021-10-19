import os
import requests
import json
from bs4 import BeautifulSoup
from github import Github
from datetime import datetime
from pytz import timezone

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


GITHUB_TOKEN = os.environ['MY_GITHUB_TOKEN']
REPOSITORY_NAME = "database"
repo = Github(GITHUB_TOKEN).get_user().get_repo(REPOSITORY_NAME)
issue_title = f"K리그 순위 ({today_date})"

if issue_body != '' and REPO_NAME == repo.name:
    reg = repo.create_issue(title=issue_title, body=league_ranking)
    print(reg)
