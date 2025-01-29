# Declaring a function


# def greeting():
#     print("Hello there")
#
# greeting()

###########################

#Declaring a function with a parameter
# def greeting2(a_name):
#     print(f'Hello {a_name}')
#
#
# name = input("Enter your name: ")
# greeting2(name)

###########################


#Declaring a function with multiple parameters
# def greeting3(first_name : str, last_name : str, age : int):
#     print(f'Hello {first_name} {last_name}, you are {age} yars old')
#
# greeting3('Yuriy', 'Drubinskiy', '38')
# greeting3('38', 'Y', 'D')
# greeting3('Bob', 'Dole', 80)
#
# greeting3('John') # Gives an error, not enough arguments

###########################


#Positional vs. keyword parameters
# Keyword parameters do not have to be passed in
#... They take the default value when not passed in
# def greeting4(first_name = 'Marquise', last_name = 'Xavier'):
#     print(f'Hello {first_name} {last_name}')

# greeting4()
# greeting4("yuriy")
# greeting4(last_name = 'Drubinskiy')
# greeting4(first_name = 'Clint', last_name = "Eastwood")


###########################


#A function, by default returns the data type NONE
# In order to have it return back any other data, we need to use the 'return command'
# This is good practice and often prefered over print()

def greeting5(first_name, last_name):
    # print('Function is being executed')
    return f'{first_name} {last_name}'
#
# print('Function called')
# greeting5('Yuriy', 'Drubinskiy') #Does not show anything
# hello = greeting5('Yuriy', 'Drubinskiy')
#
# print(hello) #save output from function to a variable

###########################

#Functions can call other functions
def message(a,b):
    full_name = greeting5(a,b)
    return f'Hello {full_name} + enjoy your stay'

print(message('Yuriy', "Drubinskiy"))



### PRACTICE ###
"""Write a function called is_float that accepts a string and returns a boolean indicating 
    whether the string is a valid float value. 
    
Not valid examples:
1) 1.1.1
2) 1.2a
3) a.1
4) 100

Valid Example:
4) 1.0
5) 1.1

"""

# Strategy:
    # 1) Look for exactly one decimal place
    # 2) Check that each character is an integer
        # Note: Since '.' is not an integer, we can remove it when we check for an integer (still need to keep the original value though)

def is_float(info):
    pass