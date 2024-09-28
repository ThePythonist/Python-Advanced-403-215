class Account:
    def __init__(self, name, id, bank, balance):
        self.name = name
        self.id = id
        self.bank = bank
        self.balance = balance

    def show_balance(self):
        print("Current account balance is :", self.balance)

    def deposit(self, value):
        if value > 0:
            self.balance += value
            print(f"Successfully deposited {value}$ to your account")
            self.show_balance()
        else:
            print("Invalid value")

    def withdraw(self, value):
        if value + 10 <= self.balance:  # 10 dollar hatman baghi bemanad
            self.balance -= value
            print(f"Successfully withdrew {value}$ from your account")
            self.show_balance()
        else:
            print("Not enough credit")


user1 = Account("mohamad teymori", "1010", "pasargad", 0)
user2 = Account("roya kiani", "3050", "saman", 0)
user3 = Account("kiarash abdi", "1030", "ayandeh", 0)

user1.deposit(500)
user1.withdraw(490)
