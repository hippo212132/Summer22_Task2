from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from flask_login import login_manager, login_required, logout_user
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
    return redirect("/login")





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
            return render_template("signup.html", error="email already taken")
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

            return render_template("index.html", user=session["user"])
    else:
                 
            
        

        return render_template("signup.html")

##redirect is used when a @route is made





# @app.route("/login", methods = ["GET", "POST"])
# def login():
    
#     if session.get("user"):

#         return redirect("/")
    

#     if request.method == "GET":
#         print("HELLO")
#         type = "student"
            
#         first_name = request.form.get("name")

#         email = request.form.get("email")
            
#         print("HELLO 2")
#         last_name = request.form.get("lastname")

#         password = request.form.get("password")

#         user = db.check_user(type, email, first_name, last_name, password)

#         session["user"] = user
#         print("HELLO 3")
#         return render_template("index.html", user=session["user"])
        
#     else:
#         return render_template("login.html", error="Incorrect information")

@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("user"):
        return redirect("/")
    if request.method == "POST":
        type = "student"
        first_name = request.form.get("name")
        email = request.form.get("email")
        last_name = request.form.get("last_name")
        password = request.form.get("password")
        user = db.check_user(email, password)

        #  session["user"] = user #identifing the user as logged in

        #     return render_template("index.html", user=session["user"])
        
        if user:
            session["user"] = user
            return render_template("index.html", user=session["user"])
        else:
            return render_template("login.html", error="Incorrect information")
    
    return render_template("login.html")
 

           
        
       

    
@app.route("/logout")
def logout():

    session.clear()
   
    return redirect("/")

    
    
    


if __name__ == "__main__":
    
    app.run(debug=True)