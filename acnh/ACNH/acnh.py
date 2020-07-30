import flask
import requests
import json


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    response = requests.get("home.html")
    # where x is information gathered from user to complete the api call
    






app.run()
