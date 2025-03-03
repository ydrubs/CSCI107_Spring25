"""
In this program we add a few attributes to the class.

We develop the methods that allow our car class to keep track of the test-drive information for  dealership.
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
        self.numb_of_test_drives = 0


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


if __name__ == '__main__':
    print('here')
    car1 = Car('Honda', 'Accord', 'blue', '20000')
