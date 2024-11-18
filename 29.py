import sqlite3
from prettytable import PrettyTable


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
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    tablename = input("Enter table name: ")

    print()

    query = f"SELECT * FROM {tablename};"

    cur.execute(query)
    records = cur.fetchall()

    # Get column names
    column_names = [description[0] for description in cur.description]

    # Create PrettyTable object
    table = PrettyTable()
    table.field_names = column_names

    # Add rows to the table
    for record in records:
        table.add_row(record)

    # Print the table
    print(table)


def main():
    choice = input("""
Hello Welcome To Database Manager
Choose an operation
1 : Create a table
2 : Insert a record into table
3 : Show table records
4 : Exit 
Choice : """)

    print()

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
