import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS customers (name, age, phone);")

# cur.execute("INSERT INTO customers VALUES ('Mohsen',23,'09334438725');")
# cur.execute("INSERT INTO customers VALUES ('Sara',24,'09213378325');")
# cur.execute("INSERT INTO customers VALUES ('Ali',17,'09213378325');")
# cur.execute("INSERT INTO customers VALUES ('Ghazal',13,'09213378325');")

# cur.execute("DELETE FROM customers;")  # Deletes every record in table
# cur.execute("DELETE FROM customers WHERE age<18;")
# cur.execute("DELETE FROM customers WHERE name='Ali';")

cur.execute("SELECT * FROM customers;")
records = cur.fetchall()

for i in records:
    print(i)

con.commit()
con.close()
print('Done')
