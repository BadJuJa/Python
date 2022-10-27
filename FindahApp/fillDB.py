import sqlite3
con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS books (`list_title` VARCHAR(100), `list_ISBN` VARCHAR(24), `list_author` VARCHAR(64),`list_description` VARCHAR(3600))""")

import pandas as pd
df = pd.read_json('books_clean.json')

for data in df['books']:
    book_id = data['id']
    book_author = data['author']
    book_title = data['title']
    book_description = data['description']
    cur.execute("""INSERT INTO books VALUES (?,?,?,?)""", (book_title, book_id, book_author, book_description))

con.commit()