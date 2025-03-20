"""
Exploring Magic methods
"""

"""
part 1 - given a class called WordFind, we want to:
    1) create an instance from a word passed in to the __init__ of the class (has the string as an attribute)
    2) Return the string passed in when calling the object through print
    3) Index into the object as though it were a normal string 
"""
# class WordFind:
    # def __init__(self, word: str):
    #     self.word = word


# The __str__ magic method tells Python how to return an object when it is called directly
# By default this returns a memory reference to the object if not implemented
#     def __str__(self):
#         return self.word

# The __getitem__ magic method tells python how to return the INDEX of an object when referenced using <obj>[i]
#     def __getitem__(self, i):
#         return self.word[i]


# Testing
# w = WordFind('hello')
# g = WordFind('Yeeet')
#
# n1 = 3
# n2 = 4
# print(type(n1))

# print(w)
# print(dir(w))
# print(w[0])

# print(n1.__eq__(3))

"""
part 2 - How does Python utilize operator overload with arithmetic functions?
    Given an arithmetic operation, how does Python hande operations such as '+' or '*' on different data types 

    NOTICE - Same operations could be used across different data types 
"""
a = 1
b = 2
#
# m = 'Hello'
# print(m.upper())
# n = 'There'
#
# x = [1, 2, 3]
# y = [9, 8, 7]

# print(a+b)
# print(a.__add__(b)) # same as equal
# print(m+n)
# print(x+y)
#
# print(a*b)
# # print(m*n) # Not implemented (ERROR)
# print(m*b)
#
# print(dir(m))


"""
Part 3 - Implementing Custom Operators using magic methods

    Create a new class to make working with Rational Numbers (Fractions) easier. The objects in the class should - 
        - be able to utilize the 4 basic operations '+' '-' '*' and '/' in order to calculate and return another rational number (fraction) 
"""
class RationalNumber:
    def __init__(self, numerator, denominator = 1):
        self.n= numerator
        self.d = denominator

    def __add__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = self.n * other.d + self.d * other.n
        d = self.d * other.d

        return RationalNumber(n,d)

    def __sub__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d

        return RationalNumber(n1 * d2 - n2 * d1, d1 * d2)

    def __radd__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = self.n * other.d + self.d * other.n
        d = self.d * other.d


        return RationalNumber(n,d)



    def __str__(self):
        return f"{self.n}/{self.d}"

if __name__ == '__main__':
    a = RationalNumber(1,2)
    b = RationalNumber(1,3)
    c = RationalNumber(3)

    print(a) # __str__ is working, yay

    print(a+b)
    print(a+3)
    print(3+a)

    print(a-b)
    print(a-3)




    # print(isinstance(c, RationalNumber)) # True
    # print(isinstance('hello', RationalNumber)) # False
    # print(isinstance(a, object)) # True
