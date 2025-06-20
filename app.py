# Importing necessary functions and classes from the Flask library
from flask import Flask, redirect, url_for

# Creating an instance of the Flask application
# '__name__' tells Flask where to look for templates, static files, etc.
app = Flask(__name__)

# Defining a route for the home page using the route decorator
# When the user visits the root URL ("/"), the 'home' function will be called
@app.route("/")
def home():
    # Returning a simple message as a string, which will be displayed in the browser
    return "Hello! this is the main page <h1>pushpasri</h1>"

# Defining a dynamic route that takes a variable 'name' from the URL
# For example, visiting /pushpasri will call this function with name="pushpasri"
@app.route("/<name>")
def user(name):
    # Returning a personalized greeting using the name passed in the URL
    return f"Hello {name}!"

# Defining a route for '/admin'
# When someone visits /admin, they will be redirected to the user() function with name="Admin!"
@app.route("/admin")
def admin():
    # 'url_for' generates the URL for the 'user' function with the parameter name="Admin!"
    # 'redirect' sends the user to that generated URL, which is '/Admin!'
    return redirect(url_for("user", name="Admin!"))

# This block ensures the app runs only when this script is executed directly (not when imported)
if __name__ == "__main__":
    # Starting the Flask development server on default localhost:5000
    # The server will keep running and listen for web requests
    app.run()
