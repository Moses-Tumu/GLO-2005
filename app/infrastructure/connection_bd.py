from mysql.connector import connect


class UserRepository:
    MYSQL_URI = "db"
    PORT = "3306"
    USERNAME = "root"
    PASSWORD = None
    DATABASE_NAME = "universite"

    def __init__(self):
        self.connector = connect(host=self.MYSQL_URI, port=self.PORT, user=self.USERNAME, password=self.PASSWORD)

    def getusers(self):
        query = "SELECT * FROM users"

        cursor = self.connector()
        cursor.execute(query)

        return [{'lastName': user[1], 'firstName': user[0]} for user in cursor]
