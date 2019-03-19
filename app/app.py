from flask import Flask, render_template

application = Flask('FlaskTest')


@application.route('/')
def index():
    return render_template('index.html', title="Un Titre")


@application.route('/login')
def login():
    return "the login page"


@application.route('/movies')
def movies():
    return "Great list of all movies"


@application.route('/shows')
def shows():
    return "Great list of all shows"


@application.route('/')
def ok():
    return "something Else"


application.run('0.0.0.0', 5000)
# application.run('127.0.0.1', 5000)
