import os
import sys
import requests
import json
from bs4 import BeautifulSoup
from github import Github
from datetime import datetime
from pytz import timezone

# 시간을 알려주는 부분
seoul_timezone = timezone('Asia/Seoul')
today = datetime.now(seoul_timezone)
today_date = today.strftime("%Y년 %m월 %d일 %H시 %M분 : %S초")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

url = 'https://kleague.com/api/clubRank.do'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
rank = json.loads(soup.text)

access_token = os.environ['MY_GITHUB_TOKEN']
repository_name = "database" # 내 저장소 이름 필수로 바꿔야함 

repo = Github(access_token).get_user().get_repo(repository_name)

issue_title = f"리그 순위표({today_date})"

print(today)
print(today_date)

with open(os.path.join(BASE_DIR, 'rank.json'), 'w+', encoding="utf-8") as make_file:
    json.dump(rank, make_file, ensure_ascii = False)    # , indent="\t"

rank_json = json.dumps(rank, sort_keys=True)  # dict()를 str로 변경 rank, indent=2, sort_keys=True

# repo.create_issue(title=issue_title, body=rank_json)  # 실행가능 
# repo.create_file('rank.json', "commit message", rank_json) # 실행가능

'''
with open (os.path.join(BASE_DIR, 'rank.json'), "r", encoding="utf-8") as f:
    reg = json.load(f)
print(reg)
'''

# https://github.com/Piorosen/github-Action-HangKik 이슈 자동 생성 및 삭제
# https://light-tree.tistory.com/236
'''
import os
from datetime import datetime
from pytz import timezone
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from github import Github

students = [["황진주", "20193148", "B501"], ["박근민", "20213056", "A1028"], ["엄소현", "20192020", "B501"]]

def get_github_repo(access_token, repository_name):
    g = Github(access_token)
    repo = g.get_user().get_repo(repository_name)
    return repo

def upload_github_issue(repo, title, body):
    repo.create_issue(title=title, body=body)

def delete_github_issue(repo):	# 이슈 삭제
    issues = repo.get_issues(state='open')	# 저장소 이슈를 받아와서 상태=열기
    for issue in issues:
        if "날짜 발열 테스트" in issue.title:	# 만약 이슈의 제목이 ""와 같다면 
            issue.edit(state='closed')	# 이슈를 수정해서 상태=닫기
            print(issue.title)


githubCall = False
if 'GITHUB_TOKEN' in os.environ:
    access_token = os.environ['GITHUB_TOKEN']
    githubCall = True
	

repository_name = "github-Action-HangKik"

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("lang=ko_KR")
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("--no-sandbox")

# chrome driver
driver = webdriver.Chrome('chromedriver', chrome_options=options)


def call(username, usernumber, userroom, temperture):
    # 원하는 url로 접속
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdka3B7OA0l1aj7H26bPkNynKzHaH2PahuRNdbqGpyEepCX3w/viewform')
    driver.maximize_window()
    name = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name.send_keys(username)
    number = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    number.send_keys(usernumber)
    room = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    room.send_keys(userroom)
    # 랜덤 체온
    fever = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fever.send_keys(temperture)
    etc = driver.find_element_by_xpath('//*[@id="i22"]/div[2]').click()
    login_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()
    return

def makeBody(list):
    result = ""
    for item in list:
        result += f"이름 : {item[0]}, 학번 : {item[1]}, 방번호 : {item[2]}, 체온 : {item[3]}\n"
    return result

seoul_timezone = timezone('Asia/Seoul')
today = datetime.now(seoul_timezone)
today_data = today.strftime("%Y년 %m월 %d일 %H시 %M분 : %S초")

for student in students:
    temp = random.randrange(0, 8)
    temp = 36 + (temp / 10)
    temp = str(temp)
    student.append(temp)
    call(student[0], student[1], student[2], temp)

if githubCall:	# 깃허브콜? 
    repo = get_github_repo(access_token, repository_name)	# 저장송에 토큰과 저장소 이름을 받아와서
    delete_github_issue(repo)	# 이 함수로 보냄
        
    title = f"날짜 발열 테스트 : ({today_data})"
    body = makeBody(students)
    upload_github_issue(repo, title, body)
'''
