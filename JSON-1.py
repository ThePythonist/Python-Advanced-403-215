import json

data = {
    "url": "https://www.youtube.com/watch?v=UmljXZIypDc",
    "title": "django tutorial part 1",
    "date": "1397",
    "comments": True,
    "list_of_comments": [
        {
            "shahla": "awesome!",
        },
        {
            "rajab": "keep it up",
        }
    ],
    "suggestions": ["flask tutorial", "fastapi tutorial"],
    "likes": None,

}

# json_st = json.dumps(data)
# print(json_st)
# print(type(json_st))


json_fl = open("data.json", "w")
json.dump(data, json_fl, indent=4)
