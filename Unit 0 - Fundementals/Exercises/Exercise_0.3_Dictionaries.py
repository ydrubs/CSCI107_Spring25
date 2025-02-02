"""
Exercise 0.3
"""

"""
Exercise 1 

Generate a list (not dictionary) of 5 random 7-digit phone numbers as strings in the format of ###-####.
    - The first digit of any phone number CANNOT be zero, the rest CAN

Print the list.
"""
from random import randint





"""
Exercise 2

The code below shows how the faker module can be used to grab a single name rather then an entire profile.

    Modify the code to:
        - Create a list (again, not dictionary) of 5 fake names using the faker module

            - HINT: You might want to create a loop that generates and stores the names
                    rather then re-type the code 5 times
"""
import faker
profile = faker.Faker()
name = profile.name()
print(name)


"""
Exercise 3

Create a dictionary called 'phone _directory' in which the Keys represents the names (from the list in exercise 2)
    and the values represents the phone numbers (in exercise 1)
"""
