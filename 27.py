import sqlite3

students = [
    {"name": "najmeh", "field": "hotel dari", "score": 17.0},
    {"name": "mohammad javad", "field": "computer", "score": 18.36},
    {"name": "matin", "field": "computer", "score": 18.00},
    {"name": "hossein", "field": "computer", "score": 15.50},
]


def create_table():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    query = "CREATE TABLE IF NOT EXISTS student (name,field,score);"

    cur.execute(query)
    conn.commit()
    conn.close()


def insert(std):
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    query = f"INSERT INTO student VALUES {(std['name'],std['field'],std['score'])};"
    cur.execute(query)

    conn.commit()
    conn.close()


def select():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    query = "SELECT * FROM student;"
    records = cur.execute(query)
    records = cur.fetchall()

    for i in records:
        if i[2] >= 17:
            print(i)

    conn.commit()
    conn.close()


# create_table()

# for i in students:
#     insert(i)

select()
