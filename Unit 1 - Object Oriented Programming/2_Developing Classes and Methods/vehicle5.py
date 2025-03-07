"""
In this script we explore how to use property decorators.

Property decorators allow method calls to be made using attributes rather than the method names.
    This, in-turn, makes it easier to use on the end-user side and allows for better control over how method are used.
"""
class Car:
    def __init__(self, make, model, color, price, dealer_price, sold = False, ):
        self.make = make
        self.model = model
        self.color = color
        self.vin = ''
        self.__price = price
        self.mpg = 0
        self.year = 0
        self.mileage = 0
        self.sold = sold
        self.on_lot = False
        self.numb_of_test_drives = 0
        self.__dealer_price = dealer_price


        self.greeting()


    def greeting(self):
        print( "Welcome to Shady Acres Car Dealership")

    def give_discount(self, percentage):
        pass

    def increase_mileage(self, miles):
        self.mileage +=miles
        return self.mileage

    def sell_car(self, final_price):
        pass

    def test_drive(self, license_number, amount_driven):
        print(f'Your plate number is {license_number}')
        self.numb_of_test_drives +=1
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
    def available(self, availability : tuple):
        """Accepts Boolean Tuple (self.on_lot, self.sold)"""
        self.on_lot = availability[0]
        self.sold = availability[1]

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





"""
Property decorator Wrap up. 

Suppose you want a property called 'available' that allows the dealership to keep track of inventory.

    - The @property should check if a car is:
        1) On the Lot
        2) Sold 
    If the car IS on the lot AND not sold, calling the property should give you a message saying the car is avaialble
    .....Otherwise, it should say the car is not available 
    
    The @available.setter property should:
         - Accept a parameter passed in as a tuple (True, True) for example, 
        .....then set the on_lot and sold attributes accordingly based on the value of the tuples 

"""
if __name__ == '__main__':
    car1 = Car('Toyota', 'Camry', 'Purple', 37000, 29000)

    is_here = car1.available
    print(is_here)

    car1.available = (True, False)
    print(car1.available)
