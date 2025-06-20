from flask import Flask,redirect,url_for,render_template


#Creates a Flask application instance named app.
app=Flask(__name__)

#his is a route decorator.
#It maps the URL path / (home page) to the home() function.

@app.route("/<name>")

#This is the function that gets called when someone visits /.
#It returns a plain string that is shown in the browser.

def home(home):
    return render_template("home.html",name=pushpasri)

#This block checks if the script is being run directly (not imported).
#If true, it starts the Flask development server.

if __name__=="__main__":
    app.run()