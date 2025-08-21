from flask import Flask


app = Flask(__name__)

@app.route("/")
def get():
    return "<h1>fart</h1>"