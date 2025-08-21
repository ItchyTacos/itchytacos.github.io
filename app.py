from flask import Flask


app = Flask(__name__)

@app.route("/")
def get():
    with open("index.html") as file:
        return file