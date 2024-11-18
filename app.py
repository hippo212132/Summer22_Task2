from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
import db




app = Flask(__name__)



app.config["SESSION_TYPE"] = (
    "filesystem"
)

Session(app)





@app.route("/")
def index():
    if session.get("user"):
        return render_template("index.html", user=session["user"]) #If user is logged in, send user to index
    else:
        return render_template("index.html")





@app.route("/signup", methods = ["GET", "POST"])
def home():
    if session.get("user"):
        return redirect("/")
    
    if request.method == "POST":  #Checking is method is POST or Get

        type = "student" #Class = Student

        first_name = request.form.get("name")
        last_name = request.form.get("lastname")
        email = request.form.get("email")
        if db.check_email(email):
            return redirect("login.html")
        password = request.form.get("password")
        cpass = request.form.get("cpass")
        
        #gathers information submitted via the form



        if password != cpass:
            print("render temp")
            return render_template("signup.html", error="Passwords Don't MATCH") #Checks if Password = CPASS
        
        else:
            print("crreate user")
            user = db.create_user(type, email, first_name, last_name, password) 
            #Uses the function from db.py to create new user and hash password
            session["user"] = user #identifing the user as logged in

            return redirect("/")
    else:
                 
            
        

        return render_template("signup.html")

##redirect is used when a @route is made





@app.route("/login", methods = ["GET", "POST"])
def login():
    
    if not session.get("user"):

        return redirect("/")
    
    elif request.method == "POST":
            
            username = request.form.get["name"]

            email = request.form.get["email"]

            

            password = request.form.get["password"] 



            db.execute("SELECT * FROM users WHERE email = ? AND name = ? AND password = ? VALUES (?)"  , (email, username, password)) 
            return redirect("/login") 
        
       
    else:
        return render_template("login.html", error="Credentials didnt match")
    
    


if __name__ == "__main__":
    
    app.run(debug=True)