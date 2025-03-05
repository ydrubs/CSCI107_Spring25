"""
In this program we explore how to use private methods to hide information.

We also look at how to use getter and setter method to access and change information in a safer manner.
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

    def get_price(self):
        """See the price the car sells for"""
        print('Thanks for your inquiry, the price is:')
        return self.__price

    def set_price(self, suggested_price):
        if suggested_price > self.__dealer_price:
            print(f"Price was set to {suggested_price}.")
            self.__price = suggested_price
        else:
            print("Get out, you are ripping me off!!")


    def get_dealer_price(self):
        """See the dealers price the car sells for"""
        return self.__dealer_price


if __name__ == '__main__':
    print('here')
    car1 = Car('Honda', 'Accord', 'blue', '20000')

