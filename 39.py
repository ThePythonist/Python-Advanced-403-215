import xml.etree.ElementTree as ET

xml_data = open("flights.xml").read()
root = ET.fromstring(xml_data)
flights = root.findall("flight")

paris_flight = []

for i in flights:
    dest = i.find("destination")
    if dest.text.lower() == "paris":
        paris_flight.append(i)

for i in paris_flight:
    flight_number = i.find('flight_number').text
    origin = i.find('origin').text
    dest = i.find('destination').text
    departure_time = i.find('departure_time').text
    arrival_time = i.find('arrival_time').text

    print(f"Flight Number: {flight_number}")
    print(f"Origin: {origin}")
    print(f"Destination: {dest}")
    print(f"Departure Time: {departure_time}")
    print(f"Arrival Time: {arrival_time}")
    print("-"*50)
