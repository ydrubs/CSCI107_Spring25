"""
In this program we:

Demonstrate how a class is created, attributes defined, and methods declared.

"""
class Car:
    def __init__(self):
        self.make = ''
        self.model = ''
        self.color = ''
        self.vin = ''
        self.price = 0
        self.mpg = 0
        self.year = 0
        self.mileage = 0
        self.sold = False
        self.on_lot = False

        self.greeting()


    def greeting(self):
        print( "You got a new car!")

    def give_discount(self, percentage):
        pass

    def increase_mileage(self, miles):
        pass

    def sell_car(self, final_price):
        pass

    def test_drive(self, license_number):
        pass

