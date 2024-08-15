from flask import Flask, render_template, request, redirect, url_for, jsonify

herodata = [{
    "name": "Spider-Man",
    "realName": "Peter Parker",
    "since": 1962,
    "powers": [
        "wall crawling",
        "web shooters",
        "spider senses",
        "super human strength & agility"
    ]
}]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("nm"):
            user = request.form.get("nm")
        else:
            user = "defaultuser"
        return redirect(url_for("success", name = user))

    return render_template("postmaker.html")

@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}!"

@app.route("/api")
def index():
    return jsonify(herodata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)