from flask import Flask, render_template
from infrastructure import UserRepository
application = Flask('FlaskTest')
user_repo = UserRepository()


@application.route('/')
def index():
    return render_template('index.html', title="Un Titre")


@application.route('/login')
def login():
    users = user_repo.getUsers()
    return users


application.run('0.0.0.0', 5000)
# application.run('127.0.0.1', 5000)
