from flask import Flask, render_template, request, redirect, url_for, sessions



from cs50 import SQL

import hashlib

db = SQL("sqlite:///C:/Users/337909/OneDrive - Milton Keynes College O365/Task 1/Flask/database.db")

app = Flask(__name__)

def hash(phrase): #This is a function used to hash a new password
 
    object = hashlib.md5(phrase.encode())
    object = object.hexdigest()
 
    return object


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")



@app.route("/signup", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        #Checking is method is POST or Get
        action = request.form['action']
        #When the Button on HTML form is pressed
        if action == 'register':
            #When the button value == register
            email = request.form.get("email")
            name = request.form.get("name")
            password = request.form.get("password")
            #gathers information submitted via the form
            if email == '' or name == '' or password == '':
                return redirect("/signup")
            #error handling - if each box = nothing will refresh page.
            
            else:

                hash(password)
                #hashing

                db.execute("INSERT INTO users (email, name, password) VALUES (?)", (email, name, password))
                #inserts form inputted values into the database with hashes password
                return redirect("/login")
                #sends to login once inserted into database
            
    return render_template("signup.html")

##redirect is used when a @route is made


if __name__ == "__main__":
    
    app.run(debug=True)