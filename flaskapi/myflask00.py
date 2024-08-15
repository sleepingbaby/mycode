from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/start")
def start():
    return render_template("postmaker.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form.get("nm"):
            user = request.form.get("nm")
        else:
            user = "defaultuser"
    return redirect(url_for("success", name = user))
    
@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}\n"

@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<guesty>")
def hello_guest(guesty):
    return f"Hello {guesty} Guest"

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guesty=name))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)