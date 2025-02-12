"""
Monte Carlo Simulation is a type of computational algorithm that uses repeated random sampling to obtain the
likelihood of a range of results of occurring.

As the number of samples increases in a Monte Carlo Simulation, the more accurate the results become to the calculated value.

A simple application of this is the 'birthday problem' - Mathematically there is a slightly greater than 50% chance that
if there are 23 people in a room at least two people have the same birthday (50.7) and with 75 people there is a 99.9% chance.

We can use a Monte Carlo simulation to test this problem - your task:

    1) Create a list of 23 random numbers between 1 and 365
    2) Check if there is any duplicate numbers from the list
        -Add one to a counter if there is a duplicate
    3) Repeat steps 1 and 2 100 times.
    4) Display what percent of the 100 times there were duplicates
"""
