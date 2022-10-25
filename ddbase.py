import sqlite3

conn = sqlite3.connect("studiz.sqlite")

cursor = conn.cursor()

sq_query = """CREATE TABLE student(
    id int NOT NULL AUTO_INCREMENT,
    name text NOT NULL,
    age int NOT NULL,
    course text NOT NULL,
    PRIMARY KEY(id)
)"""

cursor.execute(sq_query)