
from flask import Flask, render_template, request, session, redirect, url_for, g
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as ' + session['username'] + '<br>' + \
               "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + \
           "click here to log in</b></a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.execute('SELECT * FROM users WHERE username = ? AND password = ?', [username, password])
        user = cursor.fetchone()
        if user:
            session['username'] = user['username']
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        db.execute('INSERT INTO users (username, password) VALUES (?, ?)', [username, password])
        db.commit()
        session['username'] = username
        return redirect(url_for('index'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
