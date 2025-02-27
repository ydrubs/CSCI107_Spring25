"""
This is the module that uses the objects created in the car class of the:
    1) vehicle1 module
    2) vehicle 2 module
"""
#vehicle 1
# from vehicle1 import Car
#
# my_car = Car()
# print(my_car)
# print(my_car.mpg)
#
# my_car.color = 'black'
# my_car.make = 'Dodge'
# my_car.model = 'Demon'
# c1 = my_car.color
# print(f'My car is a {my_car.make} {my_car.model} and its {my_car.color}')
#
# alex_car = Car()
# # alex_car.color = 'purple'
# # alex_car.make = 'Ford'
# # alex_car.model = 'F-150'
# #
# # print(alex_car.color)
# # print(dir(alex_car))
#
# # print(alex_car.greeting())
#
# alex_car.warranty = '2 years'
# print(alex_car.warranty)
# print(dir(alex_car)) # Notice that alex_car now has a warranty attribute
# print(dir(my_car))
#
# a = 'hello'
# a.upper()
# a.is_phonenumber = False
# print(a.is_phonenumber)


###########################################################
#Vehicle 2
from vehicle2 import Car
car1 = Car('Toyota', 'Supra', 'White', 15000)
# # print(car1) # object reference
# # print(car1.make, car1.model)
#
# # print(help(Car))
# car2 = Car('Ford', 'Fusion', 'Silver', 20000)
#
# car_lot =[car1, car2]
# for car in car_lot:
#     print(car.make, car.model)



# print(help(int)) # See everything you can do with an int


###########################################################
##Practice building objects ##
"""
Ask the user how many cars they would like to enter
    For each car up to the number entered:
        1) Ask the user to enter the parameters needed to create each instance of the car class.
        2) Store each instance into a list.
        3) Print a list of the objects (not attributes or methods)
"""
number_of_cars = int(input("How much cars will be in your garage: "))
garage = []

for car in range(number_of_cars):
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    color = input("Enter the color of the car: ")
    price = input("Enter the price of the car: ")

    new_car = Car(make, model, color, price)
    garage.append(new_car)

print(garage)
print(garage[0].make)


