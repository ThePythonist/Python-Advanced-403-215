class Product:
    def __init__(self, name, id, price, barcode):
        self.name = name
        self.id = id
        self.price = price
        self.barcode = barcode


class Basket:
    def __init__(self):
        self.id = id
        self.items = []
        self.total = 0

    def add_to_basket(self, item):
        self.items.append(item)
        self.total += item.price
        print(f"Product {item.id} added to basket")

    def remove_from_basket(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Product {item.id} removed from basket")

    def show_factor(self):
        print("Total amount : ", self.total)

    def use_discount(self):
        pass


# objects
pr1 = Product("MacBook Air MGN63", "11891979", 41.399, "10001")
pr2 = Product("Vivobook X1504VA-NJ725-i3", "16670225", 21.499, "10002")
pr3 = Product("TUF Dash FX507ZI-F15", "13069711", 82.300, "10003")
user1 = Basket()

# ---------------------------------------------------------------------------

user1.add_to_basket(pr1)
user1.add_to_basket(pr2)
user1.add_to_basket(pr3)

print("-" * 50)
for i in user1.items:
    print(i.name)

print("-" * 50)
user1.remove_from_basket(pr2)

print("-" * 50)
for i in user1.items:
    print(i.name)

print("-" * 50)
user1.show_factor()
