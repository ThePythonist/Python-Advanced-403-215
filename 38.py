import xmltodict

xml_data = open("payments.xml").read()  # opening a file as a string
xml_dict = xmltodict.parse(xml_data)  # xml to python dict

root = xml_dict['employees']
employees = root['employee']

python_salaries = []

for i in employees:
    if "Python" in i["job_title"]:
        for j in i["monthly_payment"].values():
            python_salaries.append(int(j))

avg = sum(python_salaries) / len(python_salaries)
print("Average salary for python programmers :", avg)
