from flask import Flask, render_template

application = Flask('FlaskTest')


@application.route('/')
def index():
    return render_template('index.html', title="Un Titre")


application.run('127.0.0.1', 8000)
