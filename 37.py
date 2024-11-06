import xmltodict

xml_data = open("payments.xml").read()  # opening a file as a string
xml_dict = xmltodict.parse(xml_data)  # xml to python dict

root = xml_dict['employees']
employees = root['employee']

for i in employees:
    if int(i['age']) <= 30:
        print(i)
