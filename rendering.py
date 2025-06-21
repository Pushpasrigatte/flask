from flask import Flask, render_template,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html",content=["ml","dev","ai","sql","python"])

if __name__ == "__main__":
    app.run(debug=True)
