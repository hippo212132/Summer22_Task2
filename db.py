import sqlite3 

db = sqlite3.connect("./database.db", check_same_thread=False)



def signup(email, user, password):
    db.execute(f"INSERT INTO users (email, name,pass) VALUES ('{email}','{user}', '{password}')")
    db.commit()