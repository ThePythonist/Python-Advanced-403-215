header = input("Type your header : ")
par = input("Type a paragraph : ")

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

"""

with open("index.html", "w") as f:
    body = f"""
<h1>{header}</h1>
<p>{par}</p>
    """
    html += body

    html += """
</body>
</html>
    """
    f.write(html)
