from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>welcome to flask leaning path</h1>"

@app.route("/login")
def login():
    return "this is the login page"

@app.route('/<name>')
def name(name):
    return f"Hello {name}!"

@app.route('/siri')
def siri():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
