import json

json_dict = { 'category': 'food', 'name': 'mcdonalds', 'price': '1000' }
add = { 'category': 'food', 'name': 'lotteria', 'price': '1500' }

json_dict = [json_dict, add]

json_dict.update(add)

json_dict = json.loads(json.dumps(json_dict, ensure_ascii=False, indent="\t"))
print (json_dict)

