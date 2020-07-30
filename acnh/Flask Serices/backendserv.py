import flask
import os
import requests
from flask import Flask, render_template, jsonify, url_for, json, request


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
@app.route("/home.html")
@app.route("/home")
def home():
    fishes = loadJson("fishes.json")
    bugs = loadJson("bugs.json")
    sea_creatures = loadJson("sea_creatures.json")
    return render_template('home.html', fishes=fishes, bugs=bugs, sea_creatures=sea_creatures)

def loadJson(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

@app.route("/item")
def item():
    id = request.args['id']
    type = request.args['type']
    r = requests.get('http://acnhapi.com/v1/'+type+'/'+ id)
    item = json.loads(r.content)
    return render_template('item-template.html', item=item)





if __name__ == '__main__':
    app.run(debug=True)
