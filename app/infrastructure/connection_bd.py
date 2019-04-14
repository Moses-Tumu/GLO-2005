from mysql.connector import connect
from hashlib import sha256
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

        with open('/app/users.csv', newline='') as csvFile:
            reader = csv.reader(csvFile, )
            for user in reader:
                firstName = user[0]
                lastName = user[1]
                userName = user[3]
                password = user[4]
                mdpHache = sha256(password).hexdigest()

                select_query = ("SELECT Username FROM Users WHERE Username = %s")
                select_value = userName
                cursor.execute(select_query, select_value)

                founduser = [{'UserName': users[0]} for users in cursor]

                if len(founduser) < 1:
                    query = ("INSERT INTO User (FirstName, LastName, Username, Password)"
                             "VALUES (%s,%s,%s,%s)")
                    values = (firstName, lastName, userName, mdpHache)
                    cursor.execute(query, values)

        csvFile.close()

    def getusers(self):
        query = "SELECT * FROM User"

        cursor = self.connector.cursor()
        cursor.execute(query)

        return [{'LastName': user[2], 'FirstName': user[1], 'UserName':user[2]} for user in cursor]

    def getmovies(self):
        query = "SELECT * FROM Movie"

        cursor = self.connector.cursor()
        cursor.execute(query)

        return [{'Title': movie[1], 'Synopsis': movie[2], 'Length': movie[3], 'Year': movie[4],
                 'Country': movie[5], 'MaturityRating': movie[6], 'ImageUrl': movie[7]} for movie in cursor]

    def getmovies(self, type):
        query = ("SELECT * FROM Movie "
                 "JOIN Genre ON Genre.GenreId = Movie.GenreId"
                 "WHERE Genre.Name = %s")
        query_values = type

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

    def gettvshows(self, type):
        query = ("SELECT * FROM TvShow "
                 "JOIN Genre ON Genre.GenreId = TvShow.GenreId"
                 "WHERE Genre.Name = %s")
        query_values = type

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
