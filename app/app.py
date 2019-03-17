from flask import Flask, render_template
from collections import defaultdict
application = Flask('FlaskTest')


linkMovie={"KillBill":"https://www.youtube.com/embed/7kSuas6mRpk","TheMatrix":"https://www.youtube.com/embed/m8e-FF8MsqU",
           "PulpFiction":"https://www.youtube.com/embed/s7EdQ4FqbhY","ForrestGump":"https://www.youtube.com/embed/uPIEn0M8su0",
           "HotFuzz":"https://www.youtube.com/embed/ayTnvVpj9t4","22JumpStreet":"https://www.youtube.com/embed/v9S_dYuq0vE",
            "ScaryMovie4":"https://www.youtube.com/embed/JxQNmNtCg0I","GameNight":"https://www.youtube.com/embed/fNtLIcyjsnI",
           "ExMachina":"https://www.youtube.com/embed/EoQuVnKhxaM","Chappie":"https://www.youtube.com/embed/lyy7y0QOK-0",
           "MenInBlack":"https://www.youtube.com/embed/HYUd7AOw_lk"}

#fantasyMovie={}

#actionMovie={}

@application.route('/')
@application.route('/home')
def index():
    return render_template('home.html', title="Un Titre")

@application.route('/movie')
def movie():
    return render_template('movie.html', title='Movie')

@application.route('/tvshow')
def tvshow():
    return render_template('tvshow.html', title='TV Show')

@application.route('/action')
def action():
    return render_template('action.html', title='Action')

@application.route('/fantasy')
def fantasy():
    return render_template('fantasy.html', title='Fantasy')

@application.route('/comedy')
def comedy():
    return render_template('comedy.html', title='Comedy')

@application.route('/classics')
def classics():
    return render_template('classics.html', title='Classics')

#@application.route('/movie/<string:movieType>')
#def movieType(movieType):
# return render_template('movieType.html',title=movieType)


@application.route('/moviePage')
@application.route('/<string:typeMovie>/<string:movieName>')
def moviePage(typeMovie,movieName):
    theMovie = linkMovie.get(movieName)
    return render_template('moviePage.html', title= movieName, linkMovie=theMovie)

application.run('127.0.0.1', 8000)