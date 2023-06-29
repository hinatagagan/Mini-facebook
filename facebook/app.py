from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check username and password against your database
        # Replace this with your actual database check

        # Assuming a hardcoded username and password for simplicity
        if username == 'admin' and password == 'password':
            return 'Login successful'
        else:
            return 'Login failed'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
