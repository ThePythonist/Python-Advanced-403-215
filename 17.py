class Person:
    def __init__(self, name, age, city, job):
        self.name = name
        self.age = age
        self.city = city
        self.job = job

    def talk(self):
        print(f"""
Hi Im {self.name} and Im {self.age} years old
Im a {self.job} and I live in {self.city}.
        """)


hamed = Person("hamed", 30, "tehran", "programmer")
alireza = Person("alireza", 23, "tabriz", "architect")

alireza.talk()
hamed.talk()
