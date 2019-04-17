from mysql.connector import connect
from hashlib import sha256
import random
import csv


class UserRepository:
    MYSQL_URI = 'db'
    PORT = '3306'
    USERNAME = 'root'
    PASSWORD = None
    DATABASE_NAME = 'GLO2005'

# TODO: Modifier les elements de retour pour retourner les bons éléments.
    def __init__(self):
        self.connector = connect(host=self.MYSQL_URI, port=self.PORT, user=self.USERNAME, password=self.PASSWORD, database=self.DATABASE_NAME)
        cursor = self.connector.cursor()

    # Ajoute des utilisateur fictive depuis un fichier csv
        with open('/app/users.csv') as csvFile:
            reader = csv.DictReader(csvFile)
            for user in reader:
                firstName = user['prenom']
                lastName = user['nom']
                userName = user['username']
                password = user['password']
                mdpHache = sha256(password.encode()).hexdigest()

                select_query = ("SELECT Username FROM User WHERE Username = %s")
                select_value = (userName,)
                cursor.execute(select_query, select_value)

                founduser = [{'UserName': users[0]} for users in cursor]

                if len(founduser) < 1:
                    query = ("INSERT INTO User (FirstName, LastName, Username, Password)"
                             "VALUES (%s,%s,%s,%s)")
                    values = (firstName, lastName, userName, mdpHache,)
                    cursor.execute(query, values)
                    self.connector.commit()

        csvFile.close()

    # Ajoute des films de manière aléatoire
        country = open("country.txt", "r")
        movie = open("movies.txt", "r")
        image = open("imageurl.txt", "r")
        syno = open("synopsis.txt", "r")

        countrys = []
        movies = []
        images = []
        synopsis = []

        for x in range(0, 100):
            countrys.append(country.readline())
        for x in range(0, 85):
            movies.append(movie.readline())
        for x in range(0, 17):
            images.append(image.readline())
        for x in range(0, 93):
            synopsis.append(syno.readline())
        sql = "INSERT INTO Movie (Title, GenreId, Synopsis, Length, Year, Country, MaturityRating, VideoUrl ,ImageUrl) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        for x in range(0, 150):
            val = (movies[random.randint(0, 84)], random.randint(1, 10), synopsis[random.randint(0, 92)], str(random.randint(0, 10)), str(random.randint(1990, 2015)), countrys[random.randint(0, 99)], str(random.randint(7, 18)), 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', images[random.randint(0, 15)])
            cursor.execute(sql, val)
            self.connector.commit()


    def getusers(self):
        query = "SELECT * FROM User"

        cursor = self.connector.cursor()
        cursor.execute(query)

        return [{'LastName': user[2], 'FirstName': user[1], 'UserName':user[2]} for user in cursor]

    def getuser(self, username):
        query = "SELECT * FROM User WHERE UserName = %s"
        value = (username,)

        cursor = self.connector.cursor()
        cursor.execute(query, value)
        user = cursor.fetchone()
        return {'id': user[0], 'firstname': user[1], 'lastname': user[2], 'username': user[3], 'password': user[4], }

    def getmovies(self):
        query = "SELECT * FROM Movie"

        cursor = self.connector.cursor()
        cursor.execute(query)

        return [{'Title': movie[1], 'Synopsis': movie[2], 'Length': movie[3], 'Year': movie[4],
                 'Country': movie[5], 'MaturityRating': movie[6], 'ImageUrl': movie[7]} for movie in cursor]

    def getMoviesByType(self, type):
        query = ("SELECT * FROM Movie "
                 "JOIN Genre ON Genre.GenreId = Movie.GenreId"
                 "WHERE Genre.Name = %s")
        query_values = (type,)

        cursor = self.connector.cursor()
        cursor.execute(query, query_values)

        return [{'Title': movie[1], 'Synopsis': movie[2], 'Length': movie[3], 'Year': movie[4],
                 'Country': movie[5], 'MaturityRating': movie[6], 'ImageUrl': movie[7]} for movie in cursor]

    def gettvshows(self):
        query = "SELECT * FROM Shows"

        cursor = self.connector.cursor()
        cursor.execute(query)

        return [{'Title': tvshow[1], 'Synopsis': tvshow[2], 'FromYear': tvshow[3], 'ToYear': tvshow[4],
                 'Country': tvshow[5], 'MaturityRating': tvshow[6], 'ImageUrl': tvshow[7]} for tvshow in cursor]

    def getTvshowsByType(self, type):
        query = ("SELECT * FROM TvShow "
                 "JOIN Genre ON Genre.GenreId = TvShow.GenreId"
                 "WHERE Genre.Name = %s")
        query_values = (type,)

        cursor = self.connector.cursor()
        cursor.execute(query, query_values)

        return [{'Title': tvshow[1], 'Synopsis': tvshow[2], 'FromYear': tvshow[3], 'ToYear': tvshow[4],
                 'Country': tvshow[5], 'MaturityRating': tvshow[6], 'ImageUrl': tvshow[7]} for tvshow in cursor]

    def getgenre(self):
        query = "SELECT * FROM Genre"
        query_values = type

        cursor = self.connector.cursor()
        cursor.execute(query, query_values)

        return [{'Name': genre[0]} for genre in cursor]

    def searchTvShow(self,title):
        query = ("SELECT * FROM TvShow"
                "WHERE TvShow.Title LIKE CONCAT('%', %s, '%')")

        query_values = (title,)

        cursor = self.connector.cursor()
        cursor.execute(query, query_values)

        return [{'Title': tvshow[1], 'Synopsis': tvshow[2], 'FromYear': tvshow[3], 'ToYear': tvshow[4],
                 'Country': tvshow[5], 'MaturityRating': tvshow[6], 'ImageUrl': tvshow[7]} for tvshow in cursor]

    def getTvShowById(self, showId):
        query = ("SELECT * FROM TvShow"
                "WHERE TvShow.showId = %s")
        values = (showId,)
        cursor = self.connector.cursor()
        cursor.execute(query, values)
        tvshow=cursor.fetchone()

        return {'id':tvshow[0],'title':tvshow[1],'genreId':tvshow[2],'synopsis':tvshow[3],'fromYear':tvshow[4],
                'toYear':tvshow[5],'country':tvshow[6],'maturityRating':tvshow[7],'imageUrl':tvshow[8],'videoUrl':tvshow[9]}
