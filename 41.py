import csv


def write(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f'{filename} has been created successfully.')


def read(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            print(row)


data = [
    ["name", "field", "grade"],
    ["helia", "computer", "18.5"],
    ["kiarash", "memari", "19.3"],
    ["leila", "shimi", "16.5"],
    ["mohammad", "computer", "16.6"],
]

# write("students.csv", data)
read("students.csv")
