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
            cpass = request.form.get("cpass")
            #gathers information submitted via the form


            if email == '' or name == '' or password == '':
                return redirect("/signup")
            if email != str(email) or name != str(name):
                return redirect("/signup", error="Invalid Credentials")
            if len(email) <= 1:
                return redirect("/signup", error="Please enter something idiot")
            


            #error handling - if each box = nothing will refresh page.
            elif cpass == password:
                hash(password)
                #hashing


                db.execute("INSERT INTO users (email, name, password) VALUES (?)", (email, name, password))
                #inserts form inputted values into the database with hashes password
                return redirect("/login")
                #sends to login once inserted into database


            else:
                return render_template("signup.html", error="Passwords did not match")
        
            
    return render_template("signup.html")

##redirect is used when a @route is made

@app.route("/login", methods = ["GET", "POST"])
def login():
    
    
    if request.method == "POST":
        if "email" in request.form   and "name" in request.form and "password" in request.form:
            username = request.form.get["name"]
            email = request.form.get["email"]
            password = request.form.get["password"] 



            db.execute("SELECT * FROM users WHERE email = ? AND name = ? AND password = ? VALUES (?)"  , (email, username, password))  
        
       
    else:
        return render_template("login.html", error="Credentials didnt match")

if __name__ == "__main__":
    
    app.run(debug=True)