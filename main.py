import json

col = { 'category': 'food', 'name': 'mcdonalds', 'price': '1000' }
row= { 'category': 'food', 'name': 'lotteria', 'price': '1500' }

json_dict = [col, row]

json_db = json.loads(json.dumps(json_dict, ensure_ascii=False, indent="\t"))
print (json_db)
