"""
In this script we explore how to use property decorators.

Property decorators allow method calls to be made using attributes rather than the method names.
    This, in-turn, makes it easier to use on the end-user side and allows for better control over how method are used.
"""











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
        .....then set the on_lot and sold attributes accordingly based on the valiue of the tuples 

"""
