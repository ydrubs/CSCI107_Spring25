"""
Exercise 1.2 (Done after vehicle3 lesson)

Suppose you are creating a computer game that involves rolling dice.

Your task is to implement a simple dice rolling system that includes the following:

    1) Create a class called DiceBag.

    2) In the initialization method (__init__), it should accept:
         - the number of sides each dice in the bag will have (assume all dice will have the same number of sides)
         - the number of dice in the bag

                 * For example, we can have a bag of 10 six-sided dice.

    3) Add 3 methods:
        - A method that allows you to remove up to as many dice as there are in the bag.
          If more are removed the program does not allow it and gives a message

        - A method to roll up to as many dice as there are in the bag and return the results of each.
          Again, if more are rolled the program does not allow it and gives a message

        - A method to add dice to the bag

    4) Test you class by creating and using each method.
"""
import random
