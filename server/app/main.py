from flask import Flask
from db import DB

app = Flask(__name__)
db = DB()

@app.route("/")
def hello():
    return "Hello, World!"