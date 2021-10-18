import json

json_dict = { 'category': 'food', 'name': 'mcdonalds', 'price': '1000' }



json_db = json.loads(json.dumps(json_dict, ensure_ascii=False, indent="\t"))
print (json_db)
