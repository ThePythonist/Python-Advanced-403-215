import json

# f = open("states.json")
# data = json.load(f)
# for i in data["states"]:
#     print(i["name"])


with open('states.json') as f:
    data = json.load(f)

    for i in data["states"]:
        print(i["name"])
