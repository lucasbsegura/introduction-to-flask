from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid user'
    return render_template('login.html', error=error)

def valid_login(username, password):
    return True

def log_the_user_in(username):
    return username

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)