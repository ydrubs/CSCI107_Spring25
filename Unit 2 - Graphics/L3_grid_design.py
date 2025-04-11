"""
In this program we will learn how to layout a grid.
First with specific numbers, then by generalizing the dimensions.
Grids are useful in many different GUI applications such as games, menu layouts, organizers, etc..
"""

# import turtle as t
#
# #Set up screen
# t.Screen()
# t.setup(800, 600)
# t.hideturtle()
# t.tracer(False)
# t.bgcolor('lightgreen')
# t.pensize(5)
#
#
# #We will create a 5(rows)x7(columns) grid where each cell is 100x100 and there is a border of 50 pixel around each edge.
# #It could help sketching and labeling the dimensions on a paper to layout the logic
#
# #Draw the vertical lines
# t.up()
# for i in range(-350, 351, 100):
#     t.goto(i, -250)
#     t.down()
#     t.goto(i, 250)
#     t.up()
#
#
#
# #Draw the Horizontal lines
# t.up()
# for i in range(-250, 251, 100):
#     t.goto(-350, i)
#     t.down()
#     t.goto(350, i)
#     t.up()
#
#
# """place a dot in the top left cell"""
# t.up() #Move pen up
#
# # To find the center of the first cell:
#     #1) -350 is the left most point of the grid, we need to go halfway across this cell which has a lenght of 100
#     #2) 250 is the top most point of the grid, we need to go halfway down this cell, again lenght=100.
#
# t.goto(-350 +50, 250-50)
# t.dot(2, 'black')# Since each cell is 100x100, we can make that the diameter of the dot
#
#
# t.done()







###Let's rewrite this program to allow us to create a grid based on the rows, columns, and column size desired
import turtle as t

#Set grid variables to fully define custom grid and window
columns = 10
rows = 12
cell_dim = 40
border = 40


##Define window and edges based on variables
screen_width = columns * cell_dim + 2*border
screen_height = rows * cell_dim + 2*border

#Corners/edges
max_X = screen_width//2
min_X = -max_X
max_Y = screen_height//2
min_Y = -max_Y

#Set up screen function
def screen_setup(size = 5, bgcolor = 'lightgreen'):
    t.Screen()
    t.setup(screen_width, screen_height)
    t.tracer(False)
    t.bgcolor(bgcolor)
    t.pensize(size)


#Draw vertical lines  based on variables
def vertical_lines():
    t.up()
    for i in range(min_X + border, max_X-border+1, cell_dim):
        t.goto(i, min_Y+border)
        t.down()
        t.goto(i, max_Y-border)
        t.up()



#Draw horizonal lines
def horizontal_lines():
    t.up()
    for i in range(min_Y+border, max_Y-border+1, cell_dim):
        t.goto(min_X+border, i)
        t.down()
        t.goto(max_X-border, i)
        t.up()


##Exercise 2.2
"""Write a function called place_dot that accepts row, column, and color as a parameter.

    1) The function should display a dot in the middle of the row, column specified with the color passed in. 
    2) The dot should be the same diamater as the cell side legnth.
    3) The  dot should draw correctly even if the number of rows, columns, and/or cell dimensions is changed.
        So it should be defined relative to the grid and not in absolute terms
    4) Finally, if the row and/or columsn passed into the function exceeds the rows/columns the grid generates, the message 'out of range'
        should be printed in the terminal.
        
"""

def place_dot(*args): #Replace *args with specific parameters
    pass
#
#
if __name__ == '__main__':
#     #Run functions
    screen_setup()
    vertical_lines()
    horizontal_lines()
#
#     #Use the function to draw dots in the grid below
#     pass
#     pass
#     pass
#

    t.done()
