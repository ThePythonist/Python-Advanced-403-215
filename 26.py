import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

records = cur.execute("SELECT * FROM customers;")
records = records.fetchall()

for i in records:
    print(i)

con.commit()
con.close()
