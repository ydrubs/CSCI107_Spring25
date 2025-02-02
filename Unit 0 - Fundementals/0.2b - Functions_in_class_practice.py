"""
Write a function that accepts a string representing a phone number as an input and validates if the phone number is valid.
If the phone number is valid the code returns True otherwise it returns False

A valid phone number will be of the form: 555-555-5555

    All of the following are NOT valid:
        1) 5-555-555-5555
        2) 5a5-555-5555
        3) 555-5555-555
        4) 555 - 555 - 5555

HINT: You can use the command <string>.split('<split_character>')
to seperate string <string> into a list using a <split_character> as a seperator

"""

"""
Strategy:
1) Check if there are exactly 2 '-' in the number
2) THEN check if the number of digits in each part of the number is 3,3 and 4
3) THEN check if all parts of the number are numeric
"""
def valid_digits(lst : list[str]):
    if len(lst[0]) == 3 and len(lst[1]) == 3 and len(lst[2]) == 4:

        for n in lst:
            if not n.isnumeric():
                return False
        return True

    return False

def valid_phone_number(number: str):
    if number.count('-') == 2:
        digit_lst = number.split('-')
        check = valid_digits(digit_lst)
        return check # either true or false

    return False


phone_number = '555 - 555-5555'
valid = valid_phone_number(phone_number)
print(valid)
