import json

file = open("payments.json")
file = json.load(file)

for i in file["employees"]:
    print(i["name"], ":", i["job_title"])
