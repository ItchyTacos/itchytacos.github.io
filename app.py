from flask import Flask, request, render_template, abort
from markupsafe import escape
from werkzeug.security import check_password_hash
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv(".env")
ADMIN_KEY = str(os.environ.get("ADMIN_KEY"))


def check_ip(ip):
    return ip.startswith("10.8.")

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/login")
def login():
    client_ip = request.remote_addr
    print(client_ip)
    #Check to see if this works when moving it to server
    #YOU HAVE TO MAKE SURE WG WORKS FIRST
    # if check_ip:
    #     abort(403)
    username = request.args.get("username", "Flask")
    password = request.args.get("password", "")
    if check_password_hash(ADMIN_KEY, password):

        return render_template("error.html",username = escape(username))
    else:
        return render_template("error.html")
    
@app.errorhandler(404)
def errorroute(e):
    username = request.args.get("username", "Unknown User")
    return render_template("error.html",username=username)

@app.route("/test")
def test():
    password = str(request.args.get("password"))
    return str(check_password_hash(ADMIN_KEY,password))

