from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)  # ✅ Define the app FIRST

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='first_frontend_backend_connection'
    )

# ✅ Now it's safe to define routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    connection.commit()
    cursor.close()
    connection.close()

    return f"<h3>✅ Thank you {name}, your data has been saved!</h3>"

@app.route('/users')
def show_users():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    
    html = "<h2>Registered Users:</h2><ul>"
    for user in data:
        html += f"<li>{user[1]} ({user[2]})</li>"
    html += "</ul>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
