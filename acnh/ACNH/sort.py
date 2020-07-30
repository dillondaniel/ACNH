import json

f = open('fossils.txt', 'r')
for x in f:
    link =  "<a href=\"bugs\">{}</a>".format(x)

    print(link)
