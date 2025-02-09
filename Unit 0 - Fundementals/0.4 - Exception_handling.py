"""
Lesson 0.4 - Exception Handling

Powerpoint Lesson: 0.4 - Exception Handling
"""

## Slide 1 ##
# twilzzler_count = 0
# add_twizzler  = int(input("How much Twilzzlers would you like to add tp your cart? "))
#
# twilzzler_count += add_twizzler
#
# print(f"You now have {twilzzler_count} Twilzzlers in your cart")


## Slide 4 ##
# print "hello world" # Syntax Error

# x = 10/0 # ZeroDivisionError


## Slide 7 ##
# try:
#     pass
#     # Code that might raise an exception  (but runs if there is no exception)
#
# except Exception:
#     pass
#     # Code to handle the specific exception if it arises


## Slide 8 ##
"""
Opening a non-existant file
"""
# try:
#     with open("nonexistent_file.txt", "r") as file:
#         content = file.read()
#         print(content)
#
# except Exception:
#     print("Error: The file was not found. Please check the file name and try again.")



## Slide 9 ##
## General Exception Handling
# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
#
# except Exception:
#     print("An error occurred!")  # Not specific; hard to debug



## Slide 10 ##
## Specific Exception Handling
# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
#
# except pass:
#     print("You can't divide by zero!")
#
# except pass:
#     print("Invalid input! Please enter a number.")
#
#
# except pass:
#     print("Well now you've really screwed things up")


## Slide 11 ##
# secret_code = 'secret'
# entered_code = input("Please enter the secret code: ")
#
# if entered_code == '':
#     pass ("Nothing was entered")
#
# elif entered_code != secret_code:
#     pass ("You have been denied entry to the super-secret website")
#
# else:
#     print('Access granted')

## Slide 12 ##
# age = input("Enter your age: ")
#
# try:
#     if int(age) < 18:
#         pass ("you are not old enough")
#
#     print("Age confirmed")
#
# except pass:
#     print(f"Invalid input")


## Slide 13 ##
## Re-raising/catching exceptions
# age = input("Enter your age: ")
#
# try:
#     if int(age) < 18:
#         pass ("you are not old enough")

        # elif int(age) > 120:
        # pass ("This doesn't seem right...")
#
#     print("Age confirmed")
#
# pass:
#     print(f"Invalid input: pass")


