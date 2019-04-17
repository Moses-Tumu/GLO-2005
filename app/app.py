from flask import Flask, render_template, request, redirect
from flask_login import LoginManager,current_user, login_user, logout_user, login_required, UserMixin, AnonymousUserMixin
from collections import defaultdict
import random
from infrastructure import DatabaseManager
import json
from hashlib import sha256

application = Flask('GLO-2005')
login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = ''
application.config['SECRET_KEY'] = "justsomecasualsecretkeyveryuniqueandsecret"
database = DatabaseManager()


class User(UserMixin):
    def __init__(self, id):
        self.id = id


class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

tvshowCard=[
        {
         'type':'Drama',
         'description':"This is Us, Grey's Anatomy, Breaking Bad, The Walking Dead",
         'textInButton':"See Drama TV Show",
         'image':'https://img.seriebox.com/series/8/8478/400_200/this-is-us_1485465699.jpg'
        },
        {
         'type':'Crime',
         'description':'Scandal, Quantico, S.W.A.T, Rookie Blue, Dexter, Blindspot',
         'textInButton':"See Crime TV Show",
         'image':'https://tvisjustabox.files.wordpress.com/2017/03/scandal-promo.jpg?w=400&h=200&crop=1'
        },
        {
         'type':'Fantasy',
         'description':'The Walking Dead, The 100, The Flash, Supergirl, The Punisher, Gotham',
         'textInButton':"See Fantasy TV Show",
         'image':'https://i.pinimg.com/736x/36/37/db/3637db783717d4c2e1ae6d07cb81db8f--the-zombies-the-walking-dead.jpg'
        },
        {
         'type':'Action',
         'description':"Game of Thrones, Arrow, The Punisher, Vikings, Blindspot, The Flash",
         'textInButton':"See Action TV Show",
         'image':'https://www.lavieeco.com/wp-content/uploads/2015/10/GAME-OF-THRONES-2014-10-30.jpg'
        },
        {
         'type':'Comedy',
         'description':"Brooklyn Nine-Nine, The Office, Schitt's Creek, The Good Place, Silicon Valley, Young Sheldon",
         'textInButton':"See Comedy TV Show",
         'image':'https://thephoenixremix.files.wordpress.com/2017/12/15137.jpg?w=400&h=200&crop=1'
        },
        {
         'type':'Thriller',
         'description':"The Walking Dead, Gotham, American Horror Story, Supernatural, The OA, The Sinner",
         'textInButton':"See Thriller Show",
         'image':'https://thefangirl3rs.files.wordpress.com/2015/12/gotham-wallpaper.jpg?w=400&h=200&crop=1'
        }
]

movieCard=[
        {
         'type':'Action',
         'description':"Avengers, The Lord of the Rings, Indiana Jones, Rambo, Iron Man, The Hunger Games",
         'textInButton':"See Action",
         'image':'https://cinemafrenzy.files.wordpress.com/2014/03/star_wars_episode_i___the_phantom_menace_by_1darthvader-d6ieq34.jpg?w=400&h=200&crop=1'
        },
        {
         'type':'Classics',
         'description':'SchindlersList, Back to the Future, E.T, Forrest Gump, Indiana Jones',
         'textInButton':"See Classics",
         'image':'https://moviecriticjournal.files.wordpress.com/2017/12/pulp-fiction-640x360-qd0o64.jpg?w=400&h=200&crop=1'
        },
        {
         'type':'Comedy',
         'description':'Hot Fuzz, Bon Cop Bad Cop 2, 22 Jump Street, Grown Up 2, Scary Movie 4, Game Night',
         'textInButton':"See Comedy",
         'image':'https://ragingfilm.files.wordpress.com/2014/06/22_jump_street-wide.jpg?w=400&h=200&crop=1'
        },
        {
         'type':'Fantasy',
         'description':"Chappie, Ex Machina, Men In Black, The Matrix",
         'textInButton':"See Fantasy",
         'image':'https://movlash.files.wordpress.com/2015/03/chappie.jpg?w=400&h=200&crop=1'
        },
        {
         'type':'Thriller',
         'description':"A Quiet Place, The Girl on the Train, Jaws, Get Out, Hush, The Call",
         'textInButton':"See Thriller",
         'image':'https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F51449083%2F31016718777%2F1%2Foriginal.jpg?h=200&w=450&auto=compress&rect=0%2C0%2C800%2C400&s=aa335998344a7612b34b8efef4892a78'
        },
        {
         'type':'Cartoon',
         'description':"Christopher Robin, Harry Potter and the Philosopher's Stone, Charlie and the Chocolate Factory,"
                       " Monster House, Over the Hedge, Big Hero 6",
         'textInButton':"See Kids",
         'image':'https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F51771189%2F1310101965%2F1%2Foriginal.jpg?h=200&w=450&auto=compress&rect=0%2C162%2C1294%2C647&s=065eb7529493eb5496c71302133a36e6'
        }
]


@application.route('/')
@application.route('/home')
def index():
    movies = database.getsomemovies()
    return render_template('home.html', title="Un Titre", homePageImage=movies)


@application.route('/movie')
def movie():
    return render_template('movie.html', title='Movie', movieCard=movieCard)


@application.route('/tvshow')
def tvshow():
    return render_template('tvshow.html', title='TV Show', tvshowCard=tvshowCard)


@application.route('/tvshows/<string:typeTvShow>')
def tvshowType(typeTvShow):
    tvshow =database.getTvshowsByType(typeTvShow)
    return render_template('tvshowType.html', titleType=typeTvShow, tvshows=tvshow)

@application.route('/tvshow/<string:showId>')
def tvshowPage(showId):
    thisTvShow = database.getTvShowById(showId)
    return render_template('tvshowPage.html', tvshow=thisTvShow)

# type page
@application.route('/movies/<string:typeMovie>')
def movieType(typeMovie):
    movies = database.getmoviesbytype(typeMovie)
    return render_template('movieType.html', titleType=typeMovie, movies=movies)


# template for movie trailer
@application.route('/movie/<string:movieid>')
def moviePage(movieid):
    thismovie = database.getmoviebyid(movieid)

    if thismovie is not None:
        return render_template('moviePage.html', movie=thismovie)

    return redirect('/home')


@application.route('/login', methods=["GET"])
def login():
    return render_template('login.html', title='Login Page')


@application.route('/login', methods=["POST"])
def log_user():
    username = request.form['username']
    password = request.form['password']

    user = database.getuser(username)

    if user['password'] == sha256(password.encode()).hexdigest():
        user = load_user(user['id'])
        login_user(user)
        return redirect('/home')
    else:
        return render_template('login.html', title='Login Page')


@application.route('/logout')
def logout():
    logout_user()
    return redirect('/home')


@application.route('/createaccount')
def createaccount():
    return render_template('createAccount.html', title='Create Account')


@application.route('/createaccount', methods=["POST"])
def createuser():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    username = request.form['username']
    password = request.form['password']

    hashpwd = sha256(password.encode()).hexdigest()

    database.createuser(firstname, lastname, username, hashpwd)
    connecteduser = database.getuser(username)

    login_user(User(connecteduser['id']))

    return redirect('/home')


@application.route('/list')
def list():
    return render_template('list.html', title='List')


@application.route('/favorite')
@login_required
def favorite():
    favorite_movies = database.getfavoritemovie(current_user.id)
    favorite_shows = database.getfavoriteshows(current_user.id)
    return render_template('favorite.html', title='Favorite', movies=favorite_movies, shows=favorite_shows)


@application.route('/addfavorite/<string:movieid>')
def addfavorite(movieid):
    if current_user.is_authenticated:
        database.addToFavorite(current_user.id, movieid)

        link = '/movie/' + movieid
        return redirect(link)

    return redirect('/login')


@application.route('/addfavoriteshow/<string:showid>')
def addfavoriteshow(showid):
    if current_user.is_authenticated:
        database.addToFavoriteShow(current_user.id, showid)

        link = '/tvshow/' + showid
        return redirect(link)

    return redirect('/login')


@application.route('/protected')
@login_required
def protected():
    return "protected"


# @application.route('/action')
# def action():
#     return render_template('action.html', title='Action')
# @application.route('/fantasy')
# def fantasy():
#     return render_template('fantasy.html', title='Fantasy')
# @application.route('/comedy')
# def comedy():
#     return render_template('comedy.html', title='Comedy')

# @application.route('/classics')
# def classics():
#     return render_template('classics.html', title='Classics')

#
# @application.route('/movies')
# def movies():
#     return "Great list of all movies"
#
#
# @application.route('/shows')
# def shows():
#     return "Great list of all shows"
#
#
# @application.route('/')
# def ok():
#     return "something Else"


application.run('0.0.0.0', 5000)
# application.run('127.0.0.1', 5000)
