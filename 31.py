import json

f = open("states.json")
data = json.load(f)

names = []

for i in data["states"]:
    names.append(i["name"])

with open("states_names.json", "w") as f2:
    json.dump(names, f2, indent=4)
