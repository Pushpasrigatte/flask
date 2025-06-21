from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():  # ✅ function name must be 'login'
    return render_template("login.html")

@app.route("/register")
def register():  # ✅ function name must be 'register'
    return render_template("registration.html")

if __name__ == "__main__":
    app.run(debug=True)
