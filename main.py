# import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("books-collection.db") # connection to new database

# cursor = db.cursor() #cursor to control our database

# # create table - name: books, followed by column headings
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, \
# #                     title varchar(250) NOT NULL UNIQUE, \
# #                     author varchar(250) NOT NULL, \
# #                     rating FLOAT NOT NULL)")

# # insert into table called 'books' with values (id, title, author, rating)
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K Rowling', '9.3')") 
# db.commit()                  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app=app)

class Book(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    title   = db.Column(db.String(250), unique=True, nullable=False)
    author  = db.Column(db.String(250), nullable=False)
    review  = db.Column(db.Float, nullable=False)

db.create_all()

# id field is optional - if left out it will be auto-generated
new_book = Book(id=1, title="Harry Potter", author="J.K Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()

# CRUD - Create Read Update Delete
