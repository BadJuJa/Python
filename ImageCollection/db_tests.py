import os.path
import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()
#collections = cur.execute(
#    '''
#    select * from collections
#    '''
#).fetchall()

#print(collections)
#print(os.path.exists(""))
mypath = r"C:\Users\Guren\Downloads\Telegram"
import os
with os.scandir(mypath) as i:
    for entry in i:
        print(entry)