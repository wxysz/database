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

url = 'https://kleague.com/api/clubRank.do'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
rank = json.loads(soup.text)

access_token = os.environ['MY_GITHUB_TOKEN']
repository_name = "database" # 내 저장소 이름 필수로 바꿔야함 

repo = Github(access_token).get_user().get_repo(repository_name)

issue_title = f"리그 순위표({today_date})"

print(today_date)

with open(os.path.join(BASE_DIR, './rank.json'), 'w+', encoding="utf-8") as make_file:
    reg = json.dump(rank, make_file, ensure_ascii = False, indent="\t")

'''
with open (os.path.join(BASE_DIR, 'rank.json'), "r", encoding="utf-8") as f:
    reg = json.load(f)
print(reg)
'''

print('뉴스기사 스크래핑 시작')

req = requests.get('https://www.yna.co.kr/safe/news')
req.encoding= None
html = req.content
soup = BeautifulSoup(html, 'html.parser')
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

print('뉴스기사 스크래핑 끝')


student_data = {
    "1.FirstName": "Gildong",
    "2.LastName": "Hong",
    "3.Age": 20, 
    "4.University": "Yonsei University",
    "5.Courses": [
        {
            "Major": "Statistics", 
            "Classes": ["Probability", 
                        "Generalized Linear Model", 
                        "Categorical Data Analysis"]
        }, 
        {
            "Minor": "ComputerScience", 
            "Classes": ["Data Structure", 
                        "Programming", 
                        "Algorithms"]
        }
    ]
} 

st_json = json.dumps(student_data, encoding="utf-8", indent=2)

print(st_json)

'''
if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "mffdb.github.io" # 내 저장소 이름 필수로 바꿔야함 

    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")

    yes24_it_new_product_url = "http://www.yes24.com/24/Category/NewProductList/001001003?sumGb=01"

#    soup = parsing_beautifulsoup(yes24_it_new_product_url)

    data = requests.get(yes24_it_new_product_url)
    html = data.text
    soup = BeautifulSoup(html, 'html.parser')

#    upload_contents = extract_book_data(soup)

    upload_contents = ''
    new_books = soup.select(".goodsTxtInfo")	# 새 함수 선언 예스24 사이트 goodsTxtInfo 클래스 안에 내용
    url_prefix = "http://www.yes24.com"

    for new_book in new_books:
        book_name = new_book.select("a")[0].text
        url_suffix = new_book.select("a")[1].attrs['href']
        url = url_prefix + url_suffix
        price = new_book.select(".priceB")[0].text

        content = f"<a href={url}>" + book_name + "</a>" + ", " + price + "<br/>\n"
        upload_contents += content

#    repo = get_github_repo(access_token, repository_name)

    g = Github(access_token)
    repo = g.get_user().get_repo(repository_name)

    issue_title = f"YES24 IT 신간 도서 알림({today_date})"

    
#    upload_github_issue(repo, issue_title, upload_contents)

    repo.create_issue(title=issue_title, body=upload_contents)
    #repo.create_file("/rank.json", "commit message", upload_contents)
       
    print("Upload Github Issue Success!")
'''
