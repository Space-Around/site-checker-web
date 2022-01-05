import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<img src='screenshots/1234.png' />"