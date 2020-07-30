import requests
import json

response = requests.get("http://acnhapi.com/v1/fish/1")
json_response = response.json()
dictionary = json.dumps(response.json(), sort_keys = True, indent = 4)
print(dictionary)
