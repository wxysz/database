import os
import sys
import requests
import json
from bs4 import BeautifulSoup
from github import Github
from datetime import datetime
from pytz import timezone
from pandas import Series, DataFrame, pandas
from IPython.display import display


# 시간을 알려주는 부분
seoul_timezone = timezone('Asia/Seoul')
today = datetime.now(seoul_timezone)
today_date = today.strftime("%Y년 %m월 %d일 %H시 %M분 : %S초")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

url = 'https://kleague.com/api/clubRank.do'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
rank = json.loads(soup.text)

with open(os.path.join(BASE_DIR, 'rank.json'), 'w+', encoding="utf-8") as make_file:
    json.dump(rank, make_file, ensure_ascii = False)    # , indent="\t"

rank_json = json.dumps(rank, sort_keys=True)  # dict()를 str로 변경 rank, indent=2, sort_keys=True

access_token = os.environ['MY_GITHUB_TOKEN']
repository_name = "database" # 내 저장소 이름 필수로 바꿔야함 

repo = Github(access_token).get_user().get_repo(repository_name)

issue_title = f"저장 시간({today_date})"

issues1 = repo.get_issues(state='open')	# 저장소의 이슈를 받아와서 상태를 열기
for issue1 in issues1:
    if "날짜 발열 테스트" in issue1.title:	# 저장소 제목이 날짜 발열 테스트 라면 
        issue1.edit(state='closed')	# 이슈를 에디트 해서 상태를 닫기

# file = repo.get_file_contents("rank1.json")
	
# repo.delete_file('rank1.json', "commit message", sha = sha )
repo.update_file('rank1.json', "commit message", rank_json, rank_json)
	
print(f"-----------------------리그 순위표({today})-----------------------")

##########################################

change = [ "year", "leagueId", "teamId", "구단", "순위", "승점", "winCnt", "winNqty", "winEqty", "winTKqty", "tieCnt", "lossCnt", "gapCnt", "득점", "lossGoal", "경기", "homepage", "lang", "stadium", "recordType", "assignGameType", "game01", "game02", "game03", "game04", "game05", "game06" ]

print(f"-------------------------------------------------------------------------------------------")

for l1 in range(12) :
	rank['data']['league1'][l1] = dict(zip(change, list(rank['data']['league1'][l1].values())))
	del rank['data']['league1'][l1]['year']	# 년도
	del rank['data']['league1'][l1]['leagueId']	# 리그 아이디
	del rank['data']['league1'][l1]['teamId']	# 팀 아이디
	del rank['data']['league1'][l1]['winCnt']	# 승
	del rank['data']['league1'][l1]['winNqty']	# 모름
	del rank['data']['league1'][l1]['winEqty']	# 모름
	del rank['data']['league1'][l1]['winTKqty']	# 모름
	del rank['data']['league1'][l1]['tieCnt']	# 무
	del rank['data']['league1'][l1]['lossCnt']	# 패
	del rank['data']['league1'][l1]['gapCnt']	# 득실
	del rank['data']['league1'][l1]['lossGoal']	# 실점
	del rank['data']['league1'][l1]['homepage']	# 홈페이지
	del rank['data']['league1'][l1]['lang']	# 언어
	del rank['data']['league1'][l1]['stadium']	# 경기장
	del rank['data']['league1'][l1]['recordType']	# 타입
	del rank['data']['league1'][l1]['assignGameType']	# 모름
	del rank['data']['league1'][l1]['game01']	# 첫
	del rank['data']['league1'][l1]['game02']	# 둘
	del rank['data']['league1'][l1]['game03']	# 셋
	del rank['data']['league1'][l1]['game04']	# 넷
	del rank['data']['league1'][l1]['game05']	# 다
	del rank['data']['league1'][l1]['game06']	# 여
	# del rank['data']['league1'][l1]['teamName']	# 팀 이름
	# del rank['data']['league1'][l1]['rank']	# 팀 순위
	# del rank['data']['league1'][l1]['gainPoint']	# 승점
	# del rank['data']['league1'][l1]['gainGoal']	# 득점
	# del rank['data']['league1'][l1]['gameCount']	# 경기수
	
league1 = DataFrame(rank['data']['league1'])
display(league1)


print(f"-------------------------------------------------------------------------------------------")

for l2 in range(10) :
	rank['data']['league2'][l2] = dict(zip(change, list(rank['data']['league2'][l2].values())))
	del rank['data']['league2'][l2]['year']	# 년도
	del rank['data']['league2'][l2]['leagueId']	# 리그 아이디
	del rank['data']['league2'][l2]['teamId']	# 팀 아이디
	del rank['data']['league2'][l2]['winCnt']	# 승
	del rank['data']['league2'][l2]['winNqty']	# 모름
	del rank['data']['league2'][l2]['winEqty']	# 모름
	del rank['data']['league2'][l2]['winTKqty']	# 모름
	del rank['data']['league2'][l2]['tieCnt']	# 무
	del rank['data']['league2'][l2]['lossCnt']	# 패
	del rank['data']['league2'][l2]['gapCnt']	# 득실
	del rank['data']['league2'][l2]['lossGoal']	# 실점
	del rank['data']['league2'][l2]['homepage']	# 홈페이지
	del rank['data']['league2'][l2]['lang']	# 언어
	del rank['data']['league2'][l2]['stadium']	# 경기장
	del rank['data']['league2'][l2]['recordType']	# 타입
	del rank['data']['league2'][l2]['assignGameType']	# 모름
	del rank['data']['league2'][l2]['game01']	# 첫
	del rank['data']['league2'][l2]['game02']	# 둘
	del rank['data']['league2'][l2]['game03']	# 셋
	del rank['data']['league2'][l2]['game04']	# 넷
	del rank['data']['league2'][l2]['game05']	# 다
	del rank['data']['league2'][l2]['game06']	# 여
	# del rank['data']['league2'][l2]['teamName']	# 팀 이름
	# del rank['data']['league2'][l2]['rank']	# 팀 순위
	# del rank['data']['league2'][l2]['gainPoint']	# 승점
	# del rank['data']['league2'][l2]['gainGoal']	# 득점
	# del rank['data']['league2'][l2]['gameCount']	# 경기수
	
league2 = DataFrame(rank['data']['league2'])
display(league2)

print(f"-------------------------------------------------------------------------------------------")

#############################################

# repo.create_issue(title=issue_title, body=rank_json)  # 실행가능 
# repo.create_file('rank.json', "commit message", rank_json) # 실행가능

'''
with open (os.path.join(BASE_DIR, 'rank.json'), "r", encoding="utf-8") as f:
    reg = json.load(f)
print(reg)
'''

# https://github.com/Piorosen/github-Action-HangKik 이슈 자동 생성 및 삭제
# https://light-tree.tistory.com/236
# https://www.rdocumentation.org/ 검색 get_file()
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

def delete_github_issue(repo):
    issues = repo.get_issues(state='open')	# 저장소의 이슈를 받아와서 상태를 열기
    for issue in issues:
        if "날짜 발열 테스트" in issue.title:	# 저장소 제목이 날짜 발열 테스트 라면 
            issue.edit(state='closed')	# 이슈를 에디트 해서 상태를 닫기
            print(issue.title)	# 이슈 제목을 프린트


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

if githubCall:
    repo = get_github_repo(access_token, repository_name)
    delete_github_issue(repo)
        
    title = f"날짜 발열 테스트 : ({today_data})"
    body = makeBody(students)
    upload_github_issue(repo, title, body)
'''
