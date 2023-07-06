import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

def establish_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="GaganGagan@@1211",
        database="gagandb1"
    )
    return connection

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = establish_connection()
        cursor = connection.cursor()

        # Check if the users table exists, if not create it
        cursor.execute("SHOW TABLES LIKE 'users'")
        table_exists = cursor.fetchone()
        if not table_exists:
            cursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL)")

        # Query the database to check username and password
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))

        user = cursor.fetchone()

        if user:
            return 'Login successful'
        else:
            return 'Login failed'
    else:
        return render_template('index.html')

@app.route('/insert', methods=['POST'])
def insert_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = establish_connection()
        cursor = connection.cursor()

        # Insert user into the users table
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        connection.commit()

        return 'User inserted successfully'

    return 'Invalid request'

if __name__ == '__main__':
    app.run(debug=True)
