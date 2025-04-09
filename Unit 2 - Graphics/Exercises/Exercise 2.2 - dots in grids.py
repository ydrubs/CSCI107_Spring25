import turtle as t

#Set screen variables
columns = 10
rows = 10
cell_dim = 20
border = 40

screen_width = columns*cell_dim+2*border
screen_height = rows*cell_dim+2*border
max_X = screen_width//2
min_X = -(screen_width//2)
max_Y = screen_height//2
min_Y = -(screen_height//2)
#
# #Set up screen
def screen_setup():
    t.Screen()
    t.setup(screen_width,screen_height)
    t.hideturtle()
    t.tracer(False)
    t.bgcolor("lightgreen")
#
#Draw vertical lines  based on variables
def vertical_lines():
    t.up()
    v_line_count = 0 #Prevents Python from making extra vertical lines for some dimensions
    for i in range (min_X+border, max_X-cell_dim, cell_dim):
        t.goto(i, min_Y+border)
        t.down()
        t.goto(i, max_Y-border)
        t.up()
        v_line_count +=1
        if v_line_count == columns + 1:
            break

#Draw horizonal lines
def horizontal_lines():
    t.up()
    for i in range(min_Y+border, max_Y-border+1, cell_dim):
        t.goto(min_X+border, i)
        t.down()
        t.goto(max_X-border, i)
        t.up()


##Exercise
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


if __name__ == '__main__':
    #Run functions
    screen_setup()
    vertical_lines()
    horizontal_lines()

    #Use the function to draw dots in the grid below
    pass
    pass
    pass

    t.done()
