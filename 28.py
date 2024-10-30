import sqlite3

students = [
    {"name": "najmeh", "field": "hotel dari", "score": 17.0},
    {"name": "mohammad javad", "field": "computer", "score": 18.36},
    {"name": "matin", "field": "computer", "score": 18.00},
    {"name": "hossein", "field": "computer", "score": 15.50},
    {"name": "parham", "field": "computer", "score": 17.60},
]


def create_table():
    con = sqlite3.connect("info.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    field VARCHAR(70),
    score FLOAT
    );
    """)
    con.commit()
    con.close()


def insert(std):
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    query = "SELECT * FROM student;"
    records = cur.execute(query)
    records = cur.fetchall()

    for i in records:  # har i yek khat az table student ast va yek tuple ast
        if i[1] == std["name"] and i[2] == std["field"] and i[3] == std["score"]:
            print("Record already exists")
            break
    else:  # zamani ejra mishavad ke for break nashavad
        query = f"""
            INSERT INTO student (name,field,score)
            VALUES {(std['name'], std['field'], std['score'])};"""
        cur.execute(query)
        print(f"Successfully inserted {std['name']}")

        conn.commit()
        conn.close()


def select():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    query = "SELECT * FROM student;"
    records = cur.execute(query)
    records = cur.fetchall()

    for i in records:
        print(i)

    conn.commit()
    conn.close()


# create_table()

for i in students:
    insert(i)

# select()
