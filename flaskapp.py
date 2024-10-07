import sqlite3
from flask import Flask, request, g, render_template, send_file

DATABASE_PATH = '/var/www/html/flaskapp/example.db'

app = Flask(_name_)
app.config.from_object(_name_)

def connect_to_database():
    return sqlite3.connect(app.config['DATABASE_PATH'])

def get_database():
    database = getattr(g, 'database', None)
    if database is None:
        database = g.database = connect_to_database()
    return database

@app.teardown_appcontext
def close_connection(exception):
    database = getattr(g, 'database', None)
    if database is not None:
        database.close()

def execute_query(query, args=()):
    cursor = get_database().execute(query, args)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def commit_changes():
    get_database().commit()

@app.route("/")
def index():
        execute_query("DROP TABLE IF EXISTS users")
        execute_query("CREATE TABLE users (Username text,Password text,firstname text, lastname text, email text, count integer)")
        return render_template('login.html')

@app.route('/registration', methods =['GET', 'POST'])
def registration():
    message = ''
    if request.method == 'POST' and str(request.form['usn']) !="" and str(request.form['pwd']) !="" and str(request.form['fn']) !="" and str(request.form['ln']) !="":
        username = str(request.form['usn'])
        password = str(request.form['pwd'])
        firstname = str(request.form['fn'])
        lastname = str(request.form['ln'])
        email = str(request.form['em'])

        result = execute_query("""SELECT *  FROM users WHERE Username  = (?)""", (username, ))
        if result:
            message = 'User has already registered!'
        else:
            execute_query("""INSERT INTO users (username, password, firstname, lastname, email) values (?, ?, ?, ?, ? )""", (username, password, firstname, lastname, email))
            commit_changes()
            result2 = execute_query("""SELECT firstname, lastname, email  FROM users WHERE Username  = (?) AND Password = (?)""", (username, password ))
            if result2:
                for row in result2:
                    return response_page(row[0], row[1], row[2])
    elif request.method == 'POST':
        message = 'Some of the fields are missing!'
    return render_template('registration.html', message = message)

@app.route('/login', methods =['POST', 'GET'])
def login():
    message = ''
    if request.method == 'POST' and str(request.form['usn']) !="" and str(request.form['pwd']) != "":
        username = str(request.form['usn'])
        password = str(request.form['pwd'])
        result = execute_query("""SELECT firstname, lastname, email  FROM users WHERE Username  = (?) AND Password = (?)""", (username, password ))
        if result:
            for row in result:
                return response_page(row[0], row[1], row[2])
        else:
            message = 'Invalid Credentials !'
    elif request.method == 'POST':
        message = 'Please enter Credentials'
    return render_template('login.html', message = message)

@app.route("/download")
def download():
    path = "Limerick.txt"
    return send_file(path, as_attachment=True)

def get_number_of_words(file):
    data = file.read()
    words = data.split()
    return str(len(words))

def response_page(firstname, lastname, email):
    return """User details <br><br> Name :  """ + str(firstname) + """ <br> Surname : """ + str(lastname) + """ <br> Email : """ + str(email)

if _name_ == '_main_':
  app.run()