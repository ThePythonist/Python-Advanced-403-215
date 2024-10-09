class Parent:
    def __init__(self, familyname, address, city, job):
        self.familyname = familyname
        self.address = address
        self.city = city
        self.job = job

    def sayhello(self):
        print("Hello")


class Child(Parent):
    def __init__(self, familyname, address, city, university, job=None):
        super().__init__(familyname, address, city, job)
        self.university = university

    def goodbye(self):
        print("Goodbye")


valed = Parent("ahmadi", "ekbatan, varzesh street", "tehran", "mechanic")
farzand = Child("mohammadi", "ekbatan, varzesh street", "tehran", "olom tahghighat")

print(farzand.job)
print(farzand.university)
