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


imageMovieCatergory={"Action":"https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Star_Wars_Logo.svg/1280px-Star_Wars_Logo.svg.png",
            "Classics":"https://upload.wikimedia.org/wikipedia/commons/b/bc/Pulp_Fiction_Logo.png",
            "Comedy":"https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/21_Jump_Street.svg/1280px-21_Jump_Street.svg.png",
            "Fantasy":"https://c1.staticflickr.com/8/7774/18027452780_f715b6cdf2_b.jpg"}

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

tvshowLink =[
        {
          'title':'Quantico',
          'type':'Crime',
          'link':['https://www.youtube.com/embed/wJp-BZpVBPA'],
          'numberOfSeason':'1'
        },
        {
          'title':'Quantico',
          'type':'Crime',
          'link':['https://www.youtube.com/embed/hywZueVX1ME'],
          'numberOfSeason':'2'
        },
        {
          'title':'Quantico',
          'type':'Crime',
          'link':['https://www.youtube.com/embed/uA7HHoOYSv4'],
          'numberOfSeason':'3'
        },
        {
          'title':'Scandal',
          'type':'Crime',
          'link':'https://www.youtube.com/embed/PhOR6DIS_Ho',
          'numberOfSeason':'1'
        },
        {
          'title':'Scandal',
          'type':'Crime',
          'link':'https://www.youtube.com/watch?v=ccFcQXS0k_o',
          'numberOfSeason':'2'
        },
        {
          'title':'Scandal',
          'type':'Crime',
          'link':'https://www.youtube.com/watch?v=r7OIfKg5XRQ',
          'numberOfSeason':'3'
        },
                {
          'title':'Scandal',
          'type':'Crime',
          'link':'https://www.youtube.com/watch?v=CaYsx1eAFdM',
          'numberOfSeason':'4'
        },
        {
          'title':'Scandal',
          'type':'Crime',
          'link':'https://www.youtube.com/watch?v=HhUscmYpRcY',
          'numberOfSeason':'5'
        },
        {
          'title':'Scandal',
          'type':'Crime',
          'link':'https://www.youtube.com/watch?v=OWOB1kuGJsQ',
          'numberOfSeason':'6'
        },
        {
          'title':'RookieBlue',
          'type':'Crime',
          'link':['https://www.youtube.com/watch?v=AI44Mhp02Ps','https://www.youtube.com/watch?v=JK_geMqHGjA',
                  'https://www.youtube.com/watch?v=IIy1nKDbWrY'],
          'numberOfSeason':'3'
        },
        {
          'title':'SWAT',
          'type':'Crime',
          'link':['https://www.youtube.com/watch?v=LjN0p1xAZJY','https://www.youtube.com/watch?v=gZVm5D3_xws'],
          'numberOfSeason':'2'
        },
        {
          'title':'Dexter',
          'type':'Crime',
          'link':['https://www.youtube.com/watch?v=YQeUmSD1c3g','https://www.youtube.com/watch?v=0o3l6eHWRn4',
                  'https://www.youtube.com/watch?v=T8bB6-BesqA'],
          'numberOfSeason':'3'
        }
]


tvshows = [
        {
        'type':'Drama',
        'image':'https://img.seriebox.com/series/8/8478/400_200/this-is-us_1485465699.jpg',
        'title':'ThisIsUs',
        'numberOfSeason':'2'
        },
        {
        'type':'Drama',
        'image':'https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F52972323%2F252199710088%2F1%2Foriginal.jpg?h=200&w=450&auto=compress&rect=0%2C19%2C684%2C342&s=8d8a2957488a7f7f75a6985aef5c0cad',
        'title':'GreysAnatomy',
        'numberOfSeason':'14'
        },
        {
        'type':'Drama',
        'image':'https://img.seriebox.com/series/0/233/_thumbs/400_200/breaking-bad_1.png',
        'title':'BreakingBag',
        'numberOfSeason':'5'
        },
        {
        'type':'Drama',
        'image':'https://i.pinimg.com/736x/36/37/db/3637db783717d4c2e1ae6d07cb81db8f--the-zombies-the-walking-dead.jpg',
        'title':'TheWalkingDead',
        'numberOfSeason':'7'
        },
        {
        'type':'Drama',
        'image':'https://tvisjustabox.files.wordpress.com/2017/03/scandal-promo.jpg?w=400&h=200&crop=1',
        'title':'Scandal',
        'numberOfSeason':'6'
        },
        {
        'type':'Drama',
        'image':'https://img.seriebox.com/series/2/2436/_thumbs/400_200/homeland_5.jpg',
        'title':'Homeland',
        'numberOfSeason':'6'
        },
        {
        'type':'Fantasy',
        'image':'https://i.pinimg.com/736x/36/37/db/3637db783717d4c2e1ae6d07cb81db8f--the-zombies-the-walking-dead.jpg',
        'title':'TheWalkingDead',
        'numberOfSeason':'7'
        },
        {
        'type':'Fantasy',
        'image':'https://img.seriebox.com/series/4/4542/_thumbs/400_200/the-100_5.jpg',
        'title':'The100',
        'numberOfSeason':'5'
        },
        {
        'type':'Fantasy',
        'image':'https://img.seriebox.com/series/5/5614/400_200/the-flash-2014_1.jpg',
        'title':'TheFlash',
        'numberOfSeason':'5'
        },
        {
        'type':'Fantasy',
        'image':'https://img.seriebox.com/series/6/6900/400_200/supergirl_1476342732.jpg',
        'title':'Supergirl',
        'numberOfSeason':'3'
        },
        {
        'type':'Fantasy',
        'image':'https://img.seriebox.com/series/8/8420/400_200/marvel-s-the-punisher_1511106277.jpg',
        'title':'ThePunisher',
        'numberOfSeason':'1'
        },
        {
        'type':'Fantasy',
        'image':'https://img.seriebox.com/series/5/5362/gotham_1515609987.jpg',
        'title':'Gotham',
        'numberOfSeason':'3'
        },
        {
        'type':'Crime',
        'image':'https://tvisjustabox.files.wordpress.com/2017/03/scandal-promo.jpg?w=400&h=200&crop=1',
        'title':'Scandal',
        'numberOfSeason':'6'
        },
        {
        'type':'Crime',
        'image':'https://img.seriebox.com/series/6/6922/400_200/quantico_1543842423.jpg',
        'title':'Quantico',
        'numberOfSeason':'3'
        },
        {
        'type':'Crime',
        'image':'https://img.seriebox.com/series/10/10203/400_200/swat-2017_1495185345.jpg',
        'title':'SWAT',
        'numberOfSeason':'2'
        },
        {
        'type':'Crime',
        'image':'https://img.seriebox.com/serimage/1781_7926.jpg',
        'title':'RookieBlue',
        'numberOfSeason':'3'
        },
        {
        'type':'Crime',
        'image':'https://livelyindepthmusicentertainment.files.wordpress.com/2013/01/dexter.jpg',
        'title':'Dexter',
        'numberOfSeason':'5'
        },
        {
        'type':'Crime',
        'image':'https://i1.wp.com/www.aht.li/2785986/rie2.jpg',
        'title':'Blindspot',
        'numberOfSeason':'3'
        },
        {
        'type':'Comedy',
        'image':'https://thephoenixremix.files.wordpress.com/2017/12/15137.jpg?w=400&h=200&crop=1',
        'title':'BrooklynNineNine',
        'numberOfSeason':'3'
        },
        {
        'type':'Comedy',
        'image':'http://www.spectralhues.com/wp-content/uploads/2016/07/49-3.jpg',
        'title':'SiliconValley',
        'numberOfSeason':'4'
        },
        {
        'type':'Comedy',
        'image':'https://studentedgeapplication.azureedge.net/articles/012439ae-600f-4230-b423-0153fc2b8132.jpg',
        'title':'YoungSheldon',
        'numberOfSeason':'2'
        },
        {
        'type':'Comedy',
        'image':'https://img.seriebox.com/series/8/8480/400_200/the-good-place_1476035626.jpg',
        'title':'TheGoodPlace',
        'numberOfSeason':'3'
        },
        {
        'type':'Comedy',
        'image':'https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F48994787%2F223196180676%2F1%2Foriginal.jpg?h=200&w=450&auto=compress&rect=4%2C0%2C580%2C290&s=f7705f553d8dee7d7b70d88e959211f2',
        'title':'TheOffice',
        'numberOfSeason':'9'
        },
        {
        'type':'Comedy',
        'image':'https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F54838007%2F163226294571%2F1%2Foriginal.20190109-033151?h=200&w=450&auto=compress&rect=130%2C104%2C1756%2C878&s=32a182bb1347a64c926b96f2305f6dbf',
        'title':'SchittsCreek',
        'numberOfSeason':'5'
        },
         {
        'type':'Action',
        'image':'https://www.lavieeco.com/wp-content/uploads/2015/10/GAME-OF-THRONES-2014-10-30.jpg',
        'title':'GameOfThrones',
        'numberOfSeason':''
        },
        {
        'type':'Action',
        'image':'https://img.seriebox.com/series/3/3410/400_200/arrow_1489239281.png',
        'title':'Arrow',
        'numberOfSeason':'4'
        },
        {
        'type':'Action',
        'image':'https://img.seriebox.com/series/8/8420/400_200/marvel-s-the-punisher_1511106277.jpg',
        'title':'ThePunisher',
        'numberOfSeason':'1'
        },
        {
        'type':'Action',
        'image':'https://deathmetalflorist.files.wordpress.com/2016/01/vikings.jpg?w=400&h=200&crop=1',
        'title':'Vikings',
        'numberOfSeason':'3'
        },
        {
        'type':'Action',
        'image':'https://i1.wp.com/www.aht.li/2785986/rie2.jpg',
        'title':'Blindspot',
        'numberOfSeason':'3'
        },
        {
        'type':'Action',
        'image':'https://img.seriebox.com/series/5/5614/400_200/the-flash-2014_1.jpg',
        'title':'TheFlash',
        'numberOfSeason':'5'
        },
        {
        'type':'Thriller',
        'image':'https://thefangirl3rs.files.wordpress.com/2015/12/gotham-wallpaper.jpg?w=400&h=200&crop=1',
        'title':'Gotham',
        'numberOfSeason':''
        },
         {
        'type':'Thriller',
        'image':'https://i.pinimg.com/736x/36/37/db/3637db783717d4c2e1ae6d07cb81db8f--the-zombies-the-walking-dead.jpg',
        'title':'TheWalkingDead',
        'numberOfSeason':'7'
        },
        {
        'type':'Thriller',
        'image':'https://img.seriebox.com/series/2/2772/american-horror-story_1474058555.jpg',
        'title':'AmericanHorrorStory',
        'numberOfSeason':''
        },
        {
        'type':'Thriller',
        'image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt2jHRPUCPh6I7g8sCwDLkiWO7CyzKBNR-d5Fg0nryd9yDuRexbQ',
        'title':'Supernatural',
        'numberOfSeason':''
        },
        {
        'type':'Thriller',
        'image':'https://img.seriebox.com/series/9/9481/400_200/the-oa_1481645287.jpg',
        'title':'TheOA',
        'numberOfSeason':''
        },
        {
        'type':'Thriller',
        'image':'https://img.seriebox.com/series/10/10372/400_200/the-sinner_1497111252.jpg',
        'title':'TheSinner',
        'numberOfSeason':''
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
         'type':'Kids',
         'description':"Christopher Robin, Harry Potter and the Philosopher's Stone, Charlie and the Chocolate Factory,"
                       " Monster House, Over the Hedge, Big Hero 6",
         'textInButton':"See Kids",
         'image':'https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F51771189%2F1310101965%2F1%2Foriginal.jpg?h=200&w=450&auto=compress&rect=0%2C162%2C1294%2C647&s=065eb7529493eb5496c71302133a36e6'
        }
]

movies = [
        {
        'type':'Comedy',
        'image':'http://img.wfrcdn.com/lf/49/hash/42871/41319165/1/1/1.jpg',
        'title':'HotFuzz',
        'movie':'Hot Fuzz',
        'link':'https://www.youtube.com/embed/ayTnvVpj9t4'
        },
        {
        'type':'Comedy',
        'image':'https://jcsatanas.fr/wp-content/uploads/2016/07/22-jump-street.jpg',
        'title':'22JumpStreet',
        'movie':'22 Jump Street',
        'link':'https://www.youtube.com/embed/v9S_dYuq0vE'
        },
        {
        'type':'Comedy',
        'image':'http://img4.bdbphotos.com/images/400x400/3/z/3zw4zo09b7it4izt.jpg?skj2io4l',
        'title':'GrownUp2',
        'movie':'Grown Up 2',
        'link':'https://www.youtube.com/embed/a_c3hW0Uyvc'
        },
        {
        'type':'Comedy',
        'image':'https://filmachatboutique.com/boutique/image/cache/catalog/Films%20/Com%C3%A9die/Bon%20cop%20bad%20cop%202-comedie-10-10-17-400x400.jpg',
        'title':'BonCopBadCop2',
        'movie':'Bon Cop Bad Cop 2',
        'link':'https://www.youtube.com/embed/oFwBOvlQpU4'
        },
        {
        'type':'Comedy',
        'image':'https://cps-static.rovicorp.com/3/JPG_400/MI0000/626/MI0000626989.jpg?partner=allrovi.com',
        'title':'ScaryMovie4',
        'movie':'Scary Movie 4',
        'link':'https://www.youtube.com/embed/JxQNmNtCg0I'
        },
        {
        'type':'Comedy',
        'image':'https://images.fandango.com/ImageRenderer/400/0/redesign/static/img/default_poster.png/0/images/masterrepository/fandango/207452/GameNight-4K-1000x1000.jpg',
        'title':'GameNight',
        'movie':'Game Night',
        'link':'https://www.youtube.com/embed/fNtLIcyjsnI'
        },
        {
        'type':'Action',
        'image':'https://starsunfolded.com/wp-content/uploads/2018/06/Star-Wars-Episode-I-The-Phantom-Menace-1999.jpg',
        'title':'StarWarsEpisode1',
        'movie':'Star Wars: Episode 1-The Phantom Menace',
        'link':'https://www.youtube.com/embed/uMoSnrd7i5c'
        },
        {
        'type':'Action',
        'image':'https://cdn.shopify.com/s/files/1/2036/5517/products/MUS000425215_600x.jpg?v=1510590312',
        'title':'TheHungerGames',
        'movie':'The Hunger Games',
        'link':'https://www.youtube.com/embed/hXVZWe97Lxs'
        },
        {
        'type':'Action',
        'image':'https://i.ebayimg.com/images/g/-ksAAOSw8cNUOSJA/s-l400.jpg',
        'title':'RamboFirstBloodPartII',
        'movie':'Rambo First Blooe Part II',
        'link':'https://www.youtube.com/embed/IAqLKlxY3Eo'
        },
        {
        'type':'Action',
        'image':'http://www.ost-center.com/contenu/jaquettes/film/18511-01.jpg',
        'title':'Avengers',
        'movie':'Avengers',
        'link':'https://www.youtube.com/embed/eOrNdBpGMv8'
        },
        {
        'type':'Action',
        'image':'https://moviemusicuk.files.wordpress.com/2010/11/lordoftherings1cover.jpg',
        'title':'TheLordOfTheRings',
        'movie':'The Lord of The Rings',
        'link':'https://www.youtube.com/embed/V75dMMIW2B4'
        },
        {
        'type':'Action',
        'image':'https://www.tanikal.com/wp-content/uploads/2017/10/eac67ff3c526.jpg',
        'title':'IndianaJones',
        'movie':'Indiana Jones and the Raiders of the Lost Ark',
        'link':'https://www.youtube.com/embed/Rh_BJXG1-44'
        },
        {
        'type':'Classics',
        'image':'https://static.fnac-static.com/multimedia/0/Images/BE/NR/42/17/6c/7083842/1507-1/tsp20150505215506/Pulp-Fiction-Collector-s-Edition-.jpg',
        'title':'PulpFiction',
        'movie':'Pulp Fiction',
        'link':'https://www.youtube.com/embed/s7EdQ4FqbhY'
        },
        {
        'type':'Classics',
        'image':'https://www.jbhifi.com.au/FileLibrary/ProductResources/Images/139932-L-LO.jpg',
        'title':'ForrestGump',
        'movie':'Forrest Gump',
        'link':'https://www.youtube.com/embed/XHhAG-YLdk8'
        },
        {
        'type':'Classics',
        'image':'https://i.skyrock.net/7050/14527050/pics/408621735_small.jpg',
        'title':'TheMatrix',
        'movie':'The Matrix',
        'link':'https://www.youtube.com/embed/m8e-FF8MsqU'
        },
        {
        'type':'Classics',
        'image':'https://www.jbhifi.com.au/FileLibrary/ProductResources/Images/159535-L-LO.jpg',
        'title':'KillBill',
        'movie':'Kill Bill',
        'link':'https://www.youtube.com/embed/7kSuas6mRpk'
        },
        {
        'type':'Classics',
        'image':'https://www.cinezik.org/critiques/jaquettes/et_extraterrestre.jpg',
        'title':'ET',
        'movie':'E.T',
        'link':'https://www.youtube.com/embed/DSx8Jobx-Gs'
        },
        {
        'type':'Classics',
        'image':'http://picplus.ru/img/1812/12/77b43523.jpg',
        'title':'SchindlersList',
        'movie':"Schindler's List",
        'link':'https://www.youtube.com/embed/gG22XNhtnoY'
        },
        {
        'type':'Classics',
        'image':'https://lh6.googleusercontent.com/3Bf4bT3bpB7BExOa5aIJE8GzUSpw729Wl8z_kjuHIFeHA1x8buQl4zU5oRv25M8MUIhGwg6--LjpxocMRLDRGamZ9W0NPXFrdnnPBuX3tySHq00hpIXEdLB3gZDcBChwtg=s412',
        'title':'BackToTheFuture',
        'movie':"Back To The Future",
        'link':'https://www.youtube.com/embed/qvsgGtivCgs'
        },
        {
        'type':'Fantasy',
        'image':'https://i.pinimg.com/originals/49/5c/5e/495c5eed9c976950794569cd146818e3.jpg',
        'title':'ExMachina',
        'movie':'Ex Machina',
        'link':'https://www.youtube.com/embed/EoQuVnKhxaM'
        },
        {
        'type':'Fantasy',
        'image':'https://cdna.artstation.com/p/assets/covers/images/007/960/416/smaller_square/ben-mauro-ben-mauro-chappie-4b.jpg?1509574359',
        'title':'Chappie',
        'movie':'Chappie',
        'link':'https://www.youtube.com/embed/lyy7y0QOK-0'
        },
        {
        'type':'Fantasy',
        'image':'https://moviemusicuk.files.wordpress.com/2010/11/lordoftherings1cover.jpg',
        'title':'TheLordOfTheRings',
        'movie':'The Lord of The Rings',
        'link':'https://www.youtube.com/embed/HYUd7AOw_lk'
        },
        {
        'type':'Fantasy',
        'image':'https://farm9.staticflickr.com/8819/17072638696_f871731849_b.jpg',
        'title':'TheMatrix',
        'movie':'The Matrix',
        'link':'https://www.youtube.com/embed/m8e-FF8MsqU'
        },
        {
        'type':'Fantasy',
        'image':'https://i.pinimg.com/originals/31/c3/35/31c3351668eb8da5133c37ba9e5e5246.jpg',
        'title':'HarryPotterAndThePhilosopherStone',
        'movie':'Harry Potter and the Philosopher Stone',
        'link':'https://www.youtube.com/embed/VyHV0BRtdxo'
        },
        {
        'type':'Fantasy',
        'image':'https://vignette.wikia.nocookie.net/batman/images/a/ac/DarkKnightSoundtrk.jpg/revision/latest?cb=20080717155634',
        'title':'TheDarkKnight',
        'movie':'The Dark Knight',
        'link':'https://www.youtube.com/embed/EXeTwQWrcwY'
        },
        {
        'type':'Thriller',
        'image':'https://secure.meetupstatic.com/photos/event/b/a/0/1/600_470027617.jpeg',
        'title':'AQuietPlace',
        'movie':'A Quiet Place',
        'link':'https://www.youtube.com/embed/WR7cc5t7tv8'
        },
        {
        'type':'Thriller',
        'image':'https://www.easons.com/globalassets/5637150827/all/books/fiction/crime-fiction/9781473542075.jpg',
        'title':'TheGirlOnTheTrain',
        'movie':'The Girl on The Train',
        'link':'https://www.youtube.com/embed/KkoEE1i0CX8'
        },
        {
        'type':'Thriller',
        'image':'https://images.blogthings.com/whatscarymovieareyouquiz/jaws.jpg',
        'title':'Jaws',
        'movie':'Jaws',
        'link':'https://www.youtube.com/embed/U1fu_sA7XhE'
        },
        {
        'type':'Thriller',
        'image':'https://images.fandango.com/ImageRenderer/400/0/redesign/static/img/default_poster.png/0/images/masterrepository/fandango/196665/FacebookSquareAds-February2018-GetOut.jpg',
        'title':'GetOut',
        'movie':'Get Out',
        'link':'https://www.youtube.com/embed/DzfpyUB60YY'
        },
        {
        'type':'Thriller',
        'image':'https://www.music-bazaar.com/album-images/vol31/1134/1134109/3001159-big/Hush-Original-Soundtrack-cover.jpg',
        'title':'Hush',
        'movie':'Hush',
        'link':'https://www.youtube.com/embed/Q_P8WCbhC6s'
        },
        {
        'type':'Thriller',
        'image':'https://www.cinezik.org/critiques/jaquettes/dont-breathe.jpg',
        'title':'DontBreath',
        'movie':"Don't Breath",
        'link':'https://www.youtube.com/embed/76yBTNDB6vU'
        },
               {
        'type':'Kids',
        'image':'https://lumiere-a.akamaihd.net/v1/images/pr_christopherrobin_digital_c182fa7b.png?region=0%2C0%2C400%2C400',
        'title':'ChristopherRobin',
        'movie':'Christopher Robin',
        'link':'https://www.youtube.com/embed/0URpDxIjZrQ'
        },
        {
        'type':'Kids',
        'image':'https://i.pinimg.com/originals/31/c3/35/31c3351668eb8da5133c37ba9e5e5246.jpg',
        'title':'HarryPotterAndThePhilosopherStone',
        'movie':'Harry Potter and the Philosopher Stone',
        'link':'https://www.youtube.com/embed/VyHV0BRtdxo'
        },
        {
        'type':'Kids',
        'image':'https://www.aventrix-static.com/images/mIKzLjngnyV.jpg',
        'title':'CharlieAndTheChocolateFactory',
        'movie':'Charlie and The Chocolate Factory',
        'link':'https://www.youtube.com/embed/OFVGCUIXJls'
        },
        {
        'type':'Kids',
        'image':'https://static.fnac-static.com/multimedia/images_produits/ZoomPE/5/2/6/4005939674625/tsp20130828142031/Monster-house.jpg',
        'title':'MonsterHouse',
        'movie':'Monster House',
        'link':'https://www.youtube.com/embed/XEkeZhWbW7U'
        },
        {
        'type':'Kids',
        'image':'https://img.sheetmusic.direct/catalogue/product/smd_130353/large.jpg',
        'title':'OverTheHedge',
        'movie':'Over The Hedge',
        'link':'https://www.youtube.com/embed/kkrGBlvGK4I'
        },
        {
        'type':'Kids',
        'image':'https://www.jbhifi.com.au/FileLibrary/ProductResources/Images/198610-L-LO.jpg',
        'title':'BigHero6',
        'movie':"Big Hero 6",
        'link':'https://www.youtube.com/embed/z3biFxZIJOQ'
        }
    ]

favorite =[
         {
        'type':'',
        'image':'',
        'title':'',
        'movie':'',
        'link':''
        }
]

@application.route('/')
@application.route('/home')
def index():
   #imageOne =random(homePageImage)
   #imageTwo=random(homePageImage)
   return render_template('home.html', title="Un Titre", homePageImage=homePageImage)

@application.route('/movie')
def movie():
    return render_template('movie.html', title='Movie', movieCard=movieCard)

@application.route('/tvshow')
def tvshow():
    return render_template('tvshow.html', title='TV Show', tvshowCard=tvshowCard)

@application.route('/tvshow/<string:typeTvShow>')
def tvshowType(typeTvShow):
   return render_template('tvshowType.html', titleType=typeTvShow, tvshows=tvshows)

@application.route('/tvshow/<string:typeTvShow>/<string:tvShowName>')
def tvshowPage(typeTvShow,tvshowName):
   return render_template('tvshowPage.html', titleName=tvshowName, titleType=typeTvShow, tvshowLink=tvshowLink)



#type page
@application.route('/movie/<string:typeMovie>')
def movieType(typeMovie):
    return render_template('movieType.html', titleType=typeMovie, movies=movies)

#template for movie trailer
@application.route('/movie/<string:typeMovie>/<string:movieName>')
def moviePage(typeMovie,movieName):
    return render_template('moviePage.html', titleName=movieName, titleType=typeMovie, movies=movies)

@application.route('/login')
def login():
    return render_template('login.html', title='Login Page')

@application.route('/createaccount')
def createaccount():
    return render_template('createAccount.html', title='Create Account')

@application.route('/list')
def list():
    return  render_template('list.html', title='List')

@application.route('/favorite')
def favorite():
    return render_template('favorite.html', title='Favorite')

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