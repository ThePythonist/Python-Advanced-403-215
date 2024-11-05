import json

file = open("payments.json")
file = json.load(file)

total_payment = []

for i in file["employees"]:
    # total_payment.append(sum(i["monthly_payment"].values()))
    for j in i["monthly_payment"].values():
        total_payment.append(j)

print(total_payment)
print(sum(total_payment) / len(total_payment))
