import sqlite3
conn = sqlite3.connect('database.sqlite3')
c = conn.cursor()

for row in c.execute('SELECT * FROM Users'):
    print str(row[0]) + str(row[1])
