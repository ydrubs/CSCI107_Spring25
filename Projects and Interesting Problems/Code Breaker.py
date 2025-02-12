"""
Codebreaker is about guessing the correct number chosen by your opponent (the computer).

It is played like this:
    1) The computer chooses a random three-digit number
    2) You are asked to guess a number
    3) After every guess the computer gives you two pieces of information:
     - How many digits you got correct
     - How many digits are in the correct position
    4) You should continue to be asked for a number until the correct guess is given

For example: If the computer chose the number 317, and you guess 113,
        THe computer will tell you that you have guesses two numbers correctly (the one and three) and that one number
        is in the correct position (the one).

Write a program that can play the codebreaker game. THe computer should always be providing the clues
and the player guessing the number.

Write two function:
    One function checks how many digits are correct
    The other function checks how many digits are in the correct position
"""