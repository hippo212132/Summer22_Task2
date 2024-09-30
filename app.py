from flask import Flask, render_template, request

app = Flask(__name__)




@app.route("/")
def signup():
    return render_template("signup.html")

@app.route("/home")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)