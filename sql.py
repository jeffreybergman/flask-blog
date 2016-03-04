# sql.py - Create a SQLite3 table and populate with data

import sqlite3

# create the database connection
with sqlite3.connect('blog.db') as connection:
    # create a cursor
    c = connection.cursor()

    # drop the table if exists
    c.execute('DROP TABLE IF EXISTS posts')
    # create the table
    c.execute('CREATE TABLE posts (title Text, post Text)')

    # insert dummy data into the table
    c.execute('INSERT INTO posts VALUES ("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES ("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES ("Excellent", "I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES ("Okay", "I\'m okay.")')