employees = [
    {"name": "hossein", "age": 17, "job": "student"},
    {"name": "matin", "age": 16, "job": "backend-dev"},
    {"name": "mohammad", "age": 17, "job": "operator"},
    {"name": "najmeh", "age": 20, "job": "hotel manager"},
]

html = """
<!DOCTYPE html>
<html>
<head>
<style>
body { 
    font-family: Consolas, Helvetica, sans-serif;
}
            
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #a30062;
  color: white;
}
</style>
</head>
<body>

<h1>Employees Table</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Age</th>
    <th>Job</th>
  </tr>
  
"""

for i in employees:
    html += f"""
      <tr>
        <td>{i['name']}</td>
        <td>{i['age']}</td>
        <td>{i['job']}</td>
      </tr>
    """

html += """
</table>
</body>
</html>
"""

with open("table.html", "w") as f:
    f.write(html)

print("Done")
