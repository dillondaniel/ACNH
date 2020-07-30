import json

with open('fossils.json') as json_file:
    data = json.load(json_file)
    for key in data.keys():
        print(key)
