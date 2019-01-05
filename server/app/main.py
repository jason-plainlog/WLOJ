from flask import Flask
from db import DB

app = Flask(__name__)
db = DB()

@app.route("/")
def hello():
    db.connect()
    return db.client.server_info()

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)