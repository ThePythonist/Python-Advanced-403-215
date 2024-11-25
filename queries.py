import sqlite3


def signup(username, password, gender, country):
    conn = sqlite3.connect("accounts.db")
    cur = conn.cursor()

    query1 = f"CREATE TABLE IF NOT EXISTS users (username,password,gender,country);"
    cur.execute(query1)

    query2 = f"INSERT INTO users VALUES {(username, password, gender, country)};"
    cur.execute(query2)

    conn.commit()
    conn.close()

    return True


def signin_logic(username, password):
    conn = sqlite3.connect("accounts.db")
    cur = conn.cursor()

    query = f"SELECT * FROM users;"

    cur.execute(query)
    record = cur.fetchall()

    for i in record:
        if i[0] == username and i[1] == password:
            # print("Successfully logged in")
            return True
    else:  # zamani ejra mishe ke for break nashe
        return False


# signup("admin", "123", "male", "iran")
# signin("admin", "123", "male", "iran")
