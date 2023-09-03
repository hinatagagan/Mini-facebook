# Import necessary libraries/modules
import mysql.connector  # Import the MySQL connector library for database connection
from flask import Flask, render_template, request  # Import Flask and related modules

# Create a Flask application instance
app = Flask(__name__)

# Define a function to establish a database connection
def establish_connection():
    # Connect to the MySQL database with specified credentials
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="GaganGagan@@1211",
        database="gagandb1"
    )
    
    cursor = connection.cursor()  # Create a cursor object to interact with the database
    
    # Create the 'users' table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL, email VARCHAR(100) NOT NULL, bio TEXT)")
    return connection  # Return the database connection object


# Define a route for the root URL ('/') and handle both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # Check if the request method is POST (form submission)
        username = request.form['username']  # Get the 'username' input value from the form
        password = request.form['password']  # Get the 'password' input value from the form

        connection = establish_connection()  # Establish a database connection
        cursor = connection.cursor()  # Create a cursor object

        # Check if the 'users' table exists, if not, create it
        cursor.execute("SHOW TABLES LIKE 'users'")
        table_exists = cursor.fetchone()
        if not table_exists:
            cursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL)")

        # Query the database to check if the provided username and password match
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))

        user = cursor.fetchone()  # Retrieve the user data if a match is found

        if user:  # If user data is found, create a profile_data dictionary
            profile_data = {
                'username': user[1],
                'name': user[2],
                'email': user[3],
                'bio': user[4],
                # Add more profile data as needed
            }
            return render_template('profile.html', **profile_data)  # Render the 'profile.html' template with user data
        else:
            return 'Login failed'  # Display a message for failed login attempts
    else:
        return render_template('index.html')  # Render the 'index.html' template for GET requests


# Define a route for user registration ('/register') and handle POST requests
@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        print("Received a POST request to /register")  # Add this line
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        bio = request.form['bio']

        connection = establish_connection()
        cursor = connection.cursor()

        query = "INSERT INTO users (username, password, email, bio) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (username, password, email, bio))
        connection.commit()

        return 'Registration successful'
    else:
        print("Received a GET request to /register")  # Add this line
        return 'Invalid request'


# Define a route for user insertion ('/insert') and handle POST requests
@app.route('/insert', methods=['POST'])
def insert_user():
    if request.method == 'POST':  # Check if the request method is POST
        username = request.form['username']  # Get 'username' input from the form
        password = request.form['password']  # Get 'password' input from the form

        connection = establish_connection()  # Establish a database connection
        cursor = connection.cursor()  # Create a cursor object

        # Insert user data into the 'users' table
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        connection.commit()  # Commit the changes to the database

        return 'User inserted successfully'  # Display a success message after user insertion

    return 'Invalid request'  # Display an error message for invalid requests


# Define a route for user profiles ('/profile/<username>') and handle GET requests
@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    connection = establish_connection()  # Establish a database connection
    cursor = connection.cursor()  # Create a cursor object

    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()  # Retrieve user data based on the provided username

    if user:  # If user data is found, create a profile_data dictionary
        profile_data = {
            'username': user[1],
            'name': user[2],
            'email': user[3],
            'bio': user[4],
            # Add more profile data as needed
        }
        return render_template('profile.html', **profile_data)  # Render the 'profile.html' template with user data
    else:
        return 'User not found'  # Display a message if the user is not found in the database

# Run the Flask app in debug mode if this script is the main program
if __name__ == '__main__':
    app.run(debug=True)
