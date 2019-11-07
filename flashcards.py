from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to my Flash Cards application!"

# Please add: A page that shows how many times it has been viewed

@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())
