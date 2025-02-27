"""
In this program we:

Develop the concept of encapsulation by -
        passing in parameters into the initialization __init__ method rather than
        allowing them to be defined when creating an instance.

        This is often more efficient and helps encapsulate the code.
"""
class Car:
    def __init__(self, make, model, color, price, sold = False):
        self.make = make
        self.model = model
        self.color = color
        self.vin = ''
        self.price = price
        self.mpg = 0
        self.year = 0
        self.mileage = 0
        self.sold = sold
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
