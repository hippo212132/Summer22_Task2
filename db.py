import sqlite3, hashlib
from user import user

con = sqlite3.connect("database.db", check_same_thread=False)

cur = con.cursor()

def hash(phrase): #This is a function used to hash a new password
 
    object = hashlib.md5(phrase.encode())
    object = object.hexdigest()
 
    return object


def create_user(type, first_name, last_name, email, password):
    print("before user")
    password = hash(password)

    cur.execute("INSERT INTO users (type, last_name, email, name, password) VALUES (?,?,?,?,?)", (type, email, first_name, last_name, password,))
    con.commit()
    print("after daddy")


    id = cur.lastrowid 

    return user(id, type, first_name, last_name, email, password)

def check_email(email):

    cur.execute("SELECT * FROM users WHERE email = ?", (email,))

    return cur.fetchone()


def check_user(email, password):

    password = hash(password)

    cur.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password,))

    

    return cur.fetchone()