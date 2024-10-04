from flask import Flask, render_template, request, redirect, url_for, sessions
import db

app = Flask(__name__)




@app.route("/")
def signup():
    return render_template("index.html")
def home():
    return render_template("login.html")

@app.route("/signup", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        email = request.form.get("email")
        name = request.form.get("user")
        password = request.form.get("pass")
        db.signup(email, name, password)
        return redirect("/")


if __name__ == "__main__":
    
    app.run(debug=True)