import sqlite3

db = sqlite3.connect("books-collection.db") # connection to new database

cursor = db.cursor()

# create table - name: books, followed by column headings
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, \
#                     title varchar(250) NOT NULL UNIQUE, \
#                     author varchar(250) NOT NULL, \
#                     rating FLOAT NOT NULL)")

# insert into table called 'books' with values (id, title, author, rating)
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K Rowling', '9.3')") 
db.commit()                  
