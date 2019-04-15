import mysql.connector
import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="GLO2005"
)

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
mycursor = mydb.cursor()
sql = "INSERT INTO Movie (Title, GenreId, Synopsis, Length, Year, Country, MaturityRating, ImageUrl) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
for x in range (0, 150):
  val = (movies[random.randint(0, 84)], 0, synopsis[random.randint(0, 92)], str(random.randint(0, 10)), str(random.randint(1990, 2015)), countrys[random.randint(0, 99)], str(random.randint(7, 18)), images[random.randint(0, 15)])
  mycursor.execute(sql, val)

mydb.commit()