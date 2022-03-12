import sqlite3

conn=sqlite3.connect('login.db')
c=conn.cursor()
c.execute('create table login (name text,email text primary key ,password text)')
conn.commit()
conn.close()