import requests

response = requests.get("http://acnhapi.com/v1/bugs/")
json_response = response.json()
file_name = json_response['file-name']['longitude']
latitude = json_response['iss_position']['latitude']
print('Longitude: ', longitude)
print('Latitude: ', latitude)

x = input("Please enter some ACNH thing: ")
