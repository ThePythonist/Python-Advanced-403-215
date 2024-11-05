import json

file = open("states.json")
file = json.load(file)

for i in file["states"]:
    if i["name"].lower() in ["alaska", "florida", "new york"]:
        print(i)
