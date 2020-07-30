import requests

category = int(input("Welcome, Let me know if you want to find information for any of the following: Fish(1), Bugs(2), Villagers(3) or Fossils(4)"))



def user_input(category):

    if category == 1:
        fish_name = input("What sort of fish? (lower-case please)")
        x = requests.get("http://acnhapi.com/v1/fish/"+)
        treysongs = x.json()
        #print(treysongs)
        file_name = treysongs['anchovy']['file-name']
        print(file_name)
        #pass
#    if category == int(2):
#        #pass
#    if category == int(3):
#        x.json() = requests.get("http://acnhapi.com/v1/villagers/")
#        #pass
#    if category == int(4):
#        x.json() = requests.get("http://acnhapi.com/v1/fossils/")
#        #pass
#
        #user_choice = input("Please enter what you are looking for, specifically: ")
user_input(category)
