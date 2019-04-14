from mysql.connector import connect


class UserRepository:
    MYSQL_URI = 'db'
    PORT = '3306'
    USERNAME = 'root'
    PASSWORD = None
    DATABASE_NAME = 'universite'

# TODO: Modifier les elements de retour pour retourner les bons éléments.
    def __init__(self):
        self.connector = connect(host=self.MYSQL_URI, port=self.PORT, user=self.USERNAME, password=self.PASSWORD, database=self.DATABASE_NAME)

    def getusers(self):
        query = "SELECT * FROM users"

        cursor = self.connector.cursor()
        cursor.execute(query)

        return [{'lastName': user[1], 'firstName': user[0]} for user in cursor]

    def getmovies(self):
        query = "SELECT * FROM movies"

        cursor = self.connector.cursor()
        cursor.execute(query)

        return [{'lastName': movie[1], 'firstName': movie[0]} for movie in cursor]

    def getmovies(self, type):
        query = "SELECT * FROM movies WHERE type = %s"
        query_values = type

        cursor = self.connector.cursor()
        cursor.execute(query, query_values)

        return [{'lastName': movie[1], 'firstName': movie[0]} for movie in cursor]

    def gettvshows(self):
        query = "SELECT * FROM tvshows"

        cursor = self.connector.cursor()
        cursor.execute(query)

        return [{'lastName': tvshow[1], 'firstName': tvshow[0]} for tvshow in cursor]

    def gettvshows(self, type):
        query = "SELECT * FROM tvshows WHERE type = %s"
        query_values = type

        cursor = self.connector.cursor()
        cursor.execute(query, query_values);

        return [{'lastName': tvshow[1], 'firstName': tvshow[0]} for tvshow in cursor]

    def gettvshowstype(self):
        query = "SELECT * FROM tvshows WHERE type = %s"
        query_values = type

        cursor = self.connector.cursor()
        cursor.execute(query, query_values);

        return [{'lastName': tvshow[1], 'firstName': tvshow[0]} for tvshow in cursor]

    def getmoviestype(self):
        query = "SELECT * FROM tvshows WHERE type = %s"
        query_values = type

        cursor = self.connector.cursor()
        cursor.execute(query, query_values);

        return [{'lastName': tvshow[1], 'firstName': tvshow[0]} for tvshow in cursor]
