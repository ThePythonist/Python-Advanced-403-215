import sqlite3

conn = sqlite3.connect("info.db")
cur = conn.cursor()

# cur.execute("CREATE TABLE student (name,code,score,field);")
# -----------------------------------------------------------------------------------------
# cur.execute("INSERT INTO student VALUES ('ahmad','1010','16.5','computer');")
# cur.execute("INSERT INTO student VALUES ('kiarash','1020','17.35','electrical');")
# cur.execute("INSERT INTO student VALUES ('kiana','1030','19.87','architecture');")
# -----------------------------------------------------------------------------------------
records = cur.execute("SELECT * FROM student;")
records = records.fetchall()

for i in records:
    print(i)

conn.commit()
conn.close()
