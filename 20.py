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
        self.total = sum([i.price for i in self.items])

    def add_to_basket(self):
        pass

    def remove_from_basket(self):
        pass

    def show_factor(self):
        pass


pr1 = Product("MacBook Air MGN63", "11891979", 41.399, "1001")
pr2 = Product("Vivobook X1504VA-NJ725-i3", "16670225", 21.499, "1002")

user1 = Basket()
