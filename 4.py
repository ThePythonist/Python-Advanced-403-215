# from faker import Faker
# fake = Faker()
#
# print(fake.name())

# -------------------------------------------------------------

from faker import Faker
from phonenumbers import *

# fake = Faker('fa_IR')  # LOCALIZING DATA
fake = Faker()

people = []

for i in range(4):
    data = {
        "name": fake.name(),
        "email": fake.email(),
        "city": fake.city(),
        "company": fake.company()
    }

    people.append(data)

for i in people:
    print(i["city"])
