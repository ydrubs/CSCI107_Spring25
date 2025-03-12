"""
Demonstration of how inheritence works in OOP with Python

We create two new classes, ElectricCar and GasolineCar that inherit from the Car class.
We then write a method (give_discount) that gives a discount on an electric vehicle purchase.
"""


class Car:
    discount_percentage = 0
    _instances = []

    def __init__(self, make, model, color, price, dealer_price, sold=False, ):
        self.make = make
        self.model = model
        self.color = color
        self.vin = ''
        self.__price = price
        # self.mpg = 0
        self.year = 0
        self.mileage = 0
        self.sold = sold
        self.on_lot = False
        self.numb_of_test_drives = 0
        self.__dealer_price = dealer_price

        Car._instances.append(self)

        self.greeting()

    def greeting(self):
        print("Welcome to Shady Acres Car Dealership")

    def give_discount(self, percentage):
        return "Sorry no discount for you"

    def increase_mileage(self, miles):
        self.mileage += miles
        return self.mileage

    def sell_car(self, final_price):
        pass

    def test_drive(self, license_number, amount_driven):
        print(f'Your plate number is {license_number}')
        self.numb_of_test_drives += 1
        self.increase_mileage(amount_driven)
        return (f'Yay you drove the {self.make} {self.model} '
                f'it now has {self.mileage} miles on it.')

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > self.__dealer_price:
            print(f"The {self.make} {self.model} now costs ${price}")
            self.__price = price
        else:
            print("You will lose money, STOP IT.")

    @property
    def available(self):
        if self.sold == False and self.on_lot == True:
            return f"The {self.make} {self.model} is available"
        else:
            return f"The {self.make} {self.model} is NOT available"

    @available.setter
    def available(self, availability: tuple):
        """Accepts Boolean Tuple (self.on_lot, self.sold)"""
        self.on_lot = availability[0]
        self.sold = availability[1]

    @classmethod
    def apply_global_discount(cls, percentage):
        """Applies a discount to all stored car instances"""
        cls.discount_percentage = percentage
        print(f'A {percentage}% discount has been applied to ALL cars.')

        for car in cls._instances:
            discount_amount = car.__price * (cls.discount_percentage / 100)
            car.__price = car.__price - discount_amount  # Update the stored price

    # def get_price(self):
    #     """See the price the car sells for"""
    #     print('Thanks for your inquiry, the price is:')
    #     return self.__price

    # def set_price(self, suggested_price):
    #     if suggested_price > self.__dealer_price:
    #         print(f"Price was set to {suggested_price}.")
    #         self.__price = suggested_price
    #     else:
    #         print("Get out, you are ripping me off!!")

    # def get_dealer_price(self):
    #     """See the dealers price the car sells for"""
    #     return self.__dealer_price


class GasolineCar(Car):
    def __init__(self, make, model, color, price, dealer_price, mpg):
        super().__init__(make, model, color, price, dealer_price)
        self.mpg = mpg

    def get_mpg(self):
        return self.mpg

class ElectricCar(Car):
    def __init__(self, make, model, color, price, dealer_price, mpc):
        self.mpc = mpc
        super().__init__(make, model, color, price, dealer_price)

    def set_miles_per_charge(self, miles_per_charge):
        self.mpc = miles_per_charge

    def give_discount(self, percentage):
        new_price = self.price*(1-percentage/100)
        if new_price > self._Car__dealer_price:
            print(f"You recieved a {percentage} discount for buying a clean energy car")
            self.price = new_price
            return f'Reduced price is now {self.price}'
        else:
            return Car.give_discount(self, percentage)



if __name__=='__main__':
    my_car = GasolineCar('Toyota', 'Corolla', 'red', 30500, 26000, 35)
    my_car2 = ElectricCar('Toyota', 'Prius', 'red', 30500, 26000, 55)

    my_car2.set_miles_per_charge(65)
    # print(my_car2.mpc)

    my_car2.give_discount(10)
    print(my_car2.give_discount(50))
    print(my_car.give_discount(10))
