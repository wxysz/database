import json

json_db = { 'category': 'food', 'name': 'mcdonalds', 'price': '1000' }

json_db = json.loads(json.dumps(main.json_db))
print (json_db)
