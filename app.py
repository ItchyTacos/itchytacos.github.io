from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    argname = request.args.get("name", "Flask")
    return render_template("index.html", name = argname)
    

@app.route("/login")
def login():
    return render_template("error.html")