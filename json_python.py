import json_python
import json

json_dict = { 'category': 'food', 'name': 'mcdonalds', 'price': '1000' }

json_dict = json.loads(json.dumps(json_python.json_dict))
print (json_dict)
