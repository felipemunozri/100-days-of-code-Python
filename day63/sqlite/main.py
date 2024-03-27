# sqlite3 comes by default with python
import sqlite3

# To create a connection we simply use the sqlit3.connect() method passing the name of the database. The first time we
# execute this command if the database doesn't exist it creates it
db = sqlite3.connect("books-collection.db")

# To be able to manipulate our database we must create a cursor(). A cursor allows us to perform CRUD operations, among
# many others tasks
cursor = db.cursor()

# Once we have created a cursor we can use it to create our first table in our database. We only need to perform this
# once and after the first execution we must comment out this piece of code, so it doesn't get executed again and
# interfere with the following commands
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, "
#                "title varchar(250) NOT NULL UNIQUE, "
#                "author varchar(250) NOT NULL, "
#                "rating FLOAT NOT NULL)")

# To insert data in our table we use the execute() method again in conjunction with the commit() method. One caution is
# to have closed the database in whatever program we have used to open it (for example, DB Browser) because databases
# get locked while open
cursor.execute("INSERT INTO books VALUES(1, "
               "'Harry Potter', "
               "'J. K. Rowling', "
               "'9.3')")
db.commit()
