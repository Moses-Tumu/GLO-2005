from mysql.connector import connect


class UserRepository:
    MYSQL_URI = "localhost"
    PORT = "1337"
    USERNAME = "root"
    PASSWORD = None
    DATABASE_NAME = "what_is_it"

    def __init__(self):
        self.connector = connect(host=self.MYSQL_URI, port=self.PORT, user=self.USERNAME, password=self.PASSWORD, database=self.DATABASE_NAME)

    def getUsers(self):
        query = "SELECT * FROM users"

        cursor = self.connector()
        cursor.execute(query)

        return [{'lastName': user[1], 'firstName': user[0]} for user in cursor]
