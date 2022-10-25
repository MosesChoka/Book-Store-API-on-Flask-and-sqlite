import sqlite3

#create a connection
conn = sqlite3.connect("books.sqlite")

#create a table - Using cursor object
cursor = conn.cursor()
sql_query = """ CREATE TABLE book(
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
)"""

# execute query
cursor.execute(sql_query)

