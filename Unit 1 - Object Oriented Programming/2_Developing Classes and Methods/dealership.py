"""
This is the code that implements the Car class from the modules:
    1) vehicle 3
    2) vehicle 4
    3) vehicle 5
    4) vehicle 5 inheritance
"""

# from vehicle3 import Car
# car1 = Car('Honda', 'Accord', 'blue', '20000')
#
# m1 = car1.increase_mileage(10)
# print(m1)
# m2 = car1.increase_mileage(8)
# print(m2)
#
# car1.mileage = 0 # Reset miles back to 0
#
# drive_recipet = car1.test_drive('A123', 12)
# print(drive_recipet)
#
#




#######################################
from vehicle4 import Car
car1 = Car('Toyota', 'Camry', 'Purple', 37000, 29000)
# print(car1.__price)

# print(car1.__price)

car1.__price = 900 # Creates a new attribute DOES NOT change the __price
print(car1.__price)
print(dir(car1))

print(car1._Car__price)
print(car1._Car__dealer_price)

car1._Car__price = 20000
print(car1._Car__price)

p = car1.get_price()
print("here", p)

car1.set_price(30000)
print(car1.get_price())

car1.set_price(28999)





#######################################
##Getter / Setter







###########################################
# from vehicle5 import Car





###########################################
# from vehicle5_inheritence import GasolineCar, ElectricCar
