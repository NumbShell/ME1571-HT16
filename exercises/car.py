

cars = []


class Car():

    def __init__(self, brand, cost, power):
        self.brand = brand
        self.cost = cost
        self.power = power


    def getBrand(self):
        return self.brand


    def getCost(self):
        return self.cost


    def getPower(self):
        return self.power


    def __str__(self):
        return str(self.brand) + ', HP: ' + str(self.power) + ', $' + str(self.cost)


def create_car():
    car = Car(input("brand "), float(input("cost ")), float(input("power ")))
    cars.append(car)


#Can be used in a while loop to create multiple car objects until the user want to stop e.g.
create_car()

for c in cars:
    print(c)

