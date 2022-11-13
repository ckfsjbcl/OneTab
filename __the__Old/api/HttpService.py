from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    msg_0 = request.json
    return ''


