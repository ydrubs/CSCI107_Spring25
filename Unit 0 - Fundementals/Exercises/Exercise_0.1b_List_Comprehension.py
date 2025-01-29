"""
Exercise 0.1b - List Comprehension

    - Remember to use List Comprehension to solve these -
"""

"""
Problem 1 - 

Given the list of names, create and print a new list with only the names that have more then three letters.
"""
names = ['Tom', 'Bob', 'James', 'Frank', 'Ron', 'Jon', 'Greg']

#YOUR SOLUTION HERE


"""
Problem 2 -

Given the list of numbers as strings, create and print a new list with 10 added to every number in the list.

    - NOTE: It is possible and SHOULD be done with one line using a single list comprehension
    
"""
numbers = ['28', '11', '56', '32', '13']

#YOUR SOLUTION HERE



"""
Challenge (OPTIONAL - This one is more difficult)

Given the numbers from above, create and print a new list that contain only the PRIME numbers.

HINT - You might want to make a function that checks for a prime and is called from within your list comprehension.

      - Take a look at the example is_even function to see how this could be structured. 
"""

#EXAMPLE of calling a function from a list comprehension to check if a number is even
n = [2,3,4,5]
def is_even(n):
    if n%2 == 0:
        return n


# Notice, we call is_even() inside the list comprehension with the elements from the first list passed as an argument
evens = [i for i in n if is_even(i)]
print(evens)


#YOUR SOLUTION HERE
