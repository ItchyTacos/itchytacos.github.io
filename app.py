from flask import Flask, request, render_template
from markupsafe import escape
from werkzeug.security import check_password_hash

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/login")
def login():
    ADMIN_KEY = "fortnite"
    username = request.args.get("username", "Flask")
    password = request.args.get("password", "")
    if check_password_hash(ADMIN_KEY, password):

        return render_template("error.html",username = escape(username))
    else:
        return render_template("error.html")