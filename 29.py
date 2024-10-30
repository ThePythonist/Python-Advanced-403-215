import sqlite3


def create_table():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    tablename = input("Enter table name : ")
    fields = tuple(input("Enter table fields (seperated by comma) : ").split(","))

    query = f"CREATE TABLE IF NOT EXISTS {tablename} {fields};"
    cur.execute(query)

    print(f"Created table {tablename} successfully")
    conn.commit()
    conn.close()


def insert():
    pass


def select():
    pass


def main():
    choice = input("""
Hello Welcome To Database Manager
Choose an operation
1 : Create a table
2 : Insert a record into table
3 : Show table records
4 : Exit 
Choice : """)

    if choice == "1":
        create_table()
    elif choice == "2":
        insert()
    elif choice == "3":
        select()
    elif choice == "4":
        exit()
    else:
        print("Invalid operation. Try again")
        main()


main()
