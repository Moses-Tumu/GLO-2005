from flask import Flask, render_template
from collections import defaultdict
import random
application = Flask('FlaskTest')


## linkMovie={"KillBill":"","TheMatrix":"",
##            "PulpFiction":"https://www.youtube.com/embed/s7EdQ4FqbhY","ForrestGump":"https://www.youtube.com/embed/uPIEn0M8su0",
##            "HotFuzz":"https://www.youtube.com/embed/ayTnvVpj9t4","22JumpStreet":"https://www.youtube.com/embed/v9S_dYuq0vE",
##             "ScaryMovie4":"https://www.youtube.com/embed/JxQNmNtCg0I","GameNight":"https://www.youtube.com/embed/fNtLIcyjsnI",
##            "ExMachina":"","Chappie":"",
##            "MenInBlack":""}

homePageImage ={"https://streamondemandathome.com/wp-content/uploads/2016/08/Matrix-poster.jpg",
                "https://stmed.net/sites/default/files/star-wars-episode-i%3A-the-phantom-menace-wallpapers-29924-6761173.jpg",
                "https://hdqwalls.com/download/chappie-movie-hd-1024x768.jpg",
                "https://gunaxin.com/wp-content/uploads/2012/06/Pulp-Fiction-pulp-fiction-8900005-1024-768.jpg",
                "http://images1.fanpop.com/images/image_uploads/forest-forest-forrest-gump-1216093_1024_768.jpg",
                "http://img.over-blog-kiwi.com/0/71/40/63/obpicJXkNax.jpeg",
                "https://tylerroymediablog.files.wordpress.com/2016/04/22-js.jpg?w=1200&h=900",
                "https://www.superiorpics.com/wallpaper/file/Anna_Faris_in_Scary_Movie_4_Wallpaper_1_1024.jpg",
                "http://statelywallpaper.com/wp-content/uploads/2018/02/Game-Night-2018-1024x768.jpg",
                "https://d13ezvd6yrslxm.cloudfront.net/wp/wp-content/images/ex-machina-vikander.jpg",
                "https://cdn.kinepolis.com/fr/sites/kinepolis.be.fr/files/downloads/killbilluma1024x768.jpg",
                "http://cdn3.momes.net/var/momes/storage/images/culture/films-pour-enfants/science-fiction/men-in-black/741848-4-fre-FR/Men-in-black.jpg"}



imageTvShows={"ThisIsUs":"https://orig00.deviantart.net/52a6/f/2017/263/c/b/this_is_us___folder_icon_by_wes_hillebrand-dbo07ji.png",
              "GreysAnatomy":"https://farm4.staticflickr.com/3142/2935511760_3717349205_b.jpg",
              "BrooklynNineNine":"https://upload.wikimedia.org/wikipedia/commons/8/8a/Brooklyn_Nine-Nine_Logo.png",
              "Friends":"https://farm1.staticflickr.com/7/11103892_f57d05a21e.jpg",
              "SharkTank":"https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Shark_Tank_TV_logo.svg/1280px-Shark_Tank_TV_logo.svg.png"}

imageMovieCatergory={"Action":"https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Star_Wars_Logo.svg/1280px-Star_Wars_Logo.svg.png",
            "Classics":"https://upload.wikimedia.org/wikipedia/commons/b/bc/Pulp_Fiction_Logo.png",
            "Comedy":"https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/21_Jump_Street.svg/1280px-21_Jump_Street.svg.png",
            "Fantasy":"https://c1.staticflickr.com/8/7774/18027452780_f715b6cdf2_b.jpg"}
movies = [
        {
        'type':'Comedy',
        'image':'http://img.wfrcdn.com/lf/49/hash/42871/41319165/1/1/1.jpg',
        'title':'HotFuzz',
        'link':'https://www.youtube.com/embed/ayTnvVpj9t4'
        },
        {
        'type':'Comedy',
        'image':'https://jcsatanas.fr/wp-content/uploads/2016/07/22-jump-street.jpg',
        'title':'22JumpStreet',
        'link':'https://www.youtube.com/embed/v9S_dYuq0vE'
        },
        {
        'type':'Comedy',
        'image':'https://cps-static.rovicorp.com/3/JPG_400/MI0000/626/MI0000626989.jpg?partner=allrovi.com',
        'title':'ScaryMovie4',
        'link':'https://www.youtube.com/embed/JxQNmNtCg0I'
        },
        {
        'type':'Comedy',
        'image':'https://images.fandango.com/ImageRenderer/400/0/redesign/static/img/default_poster.png/0/images/masterrepository/fandango/207452/GameNight-4K-1000x1000.jpg',
        'title':'GameNight',
        'link':'https://www.youtube.com/embed/fNtLIcyjsnI'
        },
        {
        'type':'Action',
        'image':'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Star_Wars_Logo.svg/1280px-Star_Wars_Logo.svg.png',
        'title':'StarWarsEpisode1',
        'link':'https://www.youtube.com/embed/uMoSnrd7i5c'
        },
        {
        'type':'Action',
        'image':'https://farm6.staticflickr.com/5587/15230985546_bba3df28a2_b.jpg',
        'title':'TheHungerGamesPart1',
        'link':'https://www.youtube.com/embed/hXVZWe97Lxs'
        },
        {
        'type':'Action',
        'image':'https://farm4.staticflickr.com/3135/2918729352_7d96b32c75_b.jpg',
        'title':'RamboFirstBloodPartII',
        'link':'https://www.youtube.com/embed/IAqLKlxY3Eo'
        },
        {
        'type':'Action',
        'image':'https://upload.wikimedia.org/wikipedia/commons/9/95/Avengers_Endgame_Other_Logo.png',
        'title':'Avengers',
        'link':'https://www.youtube.com/embed/eOrNdBpGMv8'
        },
        {
        'type':'Classics',
        'image':'https://upload.wikimedia.org/wikipedia/commons/b/bc/Pulp_Fiction_Logo.png',
        'title':'PulpFiction',
        'link':'https://www.youtube.com/embed/s7EdQ4FqbhY'
        },
        {
        'type':'Classics',
        'image':'https://farm5.staticflickr.com/4081/4783233826_08db35ee56_b.jpg',
        'title':'ForrestGump',
        'link':'https://www.youtube.com/embed/XHhAG-YLdk8'
        },
        {
        'type':'Classics',
        'image':'https://farm9.staticflickr.com/8819/17072638696_f871731849_b.jpg',
        'title':'TheMatrix',
        'link':'https://www.youtube.com/embed/m8e-FF8MsqU'
        },
        {
        'type':'Classics',
        'image':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Killbill-vol1-logo.svg/724px-Killbill-vol1-logo.svg.png',
        'title':'KillBill',
        'link':'https://www.youtube.com/embed/7kSuas6mRpk'
        },
        {
        'type':'Fantasy',
        'image':'http://www.aveleyman.com/Gallery/2017/Misc/9592ace9-64f2-4323-a9b2-1a3736758933.jpg',
        'title':'ExMachina',
        'link':'https://www.youtube.com/embed/EoQuVnKhxaM'
        },
        {
        'type':'Fantasy',
        'image':'https://images-na.ssl-images-amazon.com/images/I/51v-peTRowL.jpg',
        'title':'Chappie',
        'link':'https://www.youtube.com/embed/lyy7y0QOK-0'
        },
        {
        'type':'Fantasy',
        'image':'https://thmbs.baklol.com/6_jpeg42269fc55ff2b8b228eeffcf17e7412b.jpeg',
        'title':'MenInBlack',
        'link':'https://www.youtube.com/embed/HYUd7AOw_lk'
        },
        {
        'type':'Fantasy',
        'image':'https://farm9.staticflickr.com/8819/17072638696_f871731849_b.jpg',
        'title':'TheMatrix',
        'link':'https://www.youtube.com/embed/m8e-FF8MsqU'
        }
    ]


@application.route('/')
@application.route('/home')
def index():
   #imageOne =random(homePageImage)
   #imageTwo=random(homePageImage)
   return render_template('home.html', title="Un Titre")

@application.route('/movie')
def movie():
    return render_template('movie.html', title='Movie')

@application.route('/tvshow')
def tvshow():
    return render_template('tvshow.html', title='TV Show')

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

#type page
@application.route('/movie/<string:typeMovie>')
def movieType(typeMovie):
    return render_template('movieType.html', titleType=typeMovie, movies=movies)

#template for movie trailer
@application.route('/movie/<string:typeMovie>/<string:movieName>')
def moviePage(typeMovie,movieName):
    return render_template('moviePage.html', titleName=movieName, titleType=typeMovie, movies=movies)


#@application.route('/<string:typeTvShow>/<string:tvShowName>')
#def moviePage(typeMovie,movieName):
  # theMovie = linkMovie.get(movieName)
   # return render_template('moviePage.html', title= movieName, linkMovie=theMovie)




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