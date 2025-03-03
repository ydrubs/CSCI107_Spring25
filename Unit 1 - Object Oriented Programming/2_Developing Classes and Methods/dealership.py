"""
This is the code that implements the Car class from the modules:
    1) vehicle 3
    2) vehicle 4
    3) vehicle 5
    4) vehicle 5 inheritance
"""

from vehicle3 import Car
car1 = Car('Honda', 'Accord', 'blue', '20000')

m1 = car1.increase_mileage(10)
print(m1)
m2 = car1.increase_mileage(8)
print(m2)

car1.mileage = 0 # Reset miles back to 0

drive_recipet = car1.test_drive('A123', 12)
print(drive_recipet)






#######################################
# from vehicle4 import Car







#######################################
##Getter / Setter







###########################################
# from vehicle5 import Car





###########################################
# from vehicle5_inheritence import GasolineCar, ElectricCar
