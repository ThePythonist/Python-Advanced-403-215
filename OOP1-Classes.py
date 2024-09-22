import time


class Car:
    def __init__(self, name, year, hp, color, delay):  # constructor
        self.name = name
        self.year = year
        self.horsepower = hp
        self.color = color
        self.engine_is_on = False
        self.fuel = 24
        self.speed = 0
        self.delay = delay

    def startengine(self):
        if self.fuel > 0:
            self.engine_is_on = True
            print(self.name, "engine is on")

    def accelerate(self, value):
        if self.engine_is_on:
            for i in range(value):
                time.sleep(self.delay)
                self.speed += 10
                print(f"current car speed is {self.speed}")

    def carbreak(self):
        print("Slowing Down")

    def horn(self):
        print("Boooooooooooooooogh")


# sakht shey - instance - object
samand = Car("samand", 1399, 120, "white", 2)
dena = Car("dena", 1401, 140, "black", 1)
talisman = Car("talisman", 1398, 180, "black", 0.3)
persia = Car("persia", 1396, 135, "white", 1.5)

talisman.startengine()
talisman.accelerate(2)
