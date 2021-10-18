import requests
from bs4 import BeautifulSoup
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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

with open(os.path.join(BASE_DIR, 'rank.json'), 'w+',encoding='utf-8') as write_file:
    json.dump(rank_zip, write_file, ensure_ascii = False, indent='\t')

repo.create_issue()

'''
for league_ranking in rank_zip:
    json.dumps(league_ranking, ensure_ascii=False, indent="\t")
    print(json.dumps(league_ranking, ensure_ascii=False, indent="\t"))

# with open(os.path.join(BASE_DIR, 'rank.json'), "r") as modify_json:
#    rank_zip
        
with open(os.path.join(BASE_DIR, 'rank.json'), 'w+',encoding='utf-8') as write_file:
    json.dump(rank_zip, write_file, ensure_ascii = False, indent='\t')
    print(json.dump(league_ranking, write_file, ensure_ascii = False, indent='\t'))
'''
