import sqlite3

conn=sqlite3.connect('my_database.db',check_same_thread=False)
cursor=conn.cursor()
cursor.execute(
    '''
CREATE TABLE IF NOT EXISTS todos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
completed TEXT
)

'''
)

conn.commit()
@app.get('/')
def home():
    return {"message":"SqlLite Database Connection is successful"}