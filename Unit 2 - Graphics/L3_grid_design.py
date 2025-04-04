"""
In this program we will learn how to layout a grid.
First with specific numbers, then by generalizing the dimensions.
Grids are useful in many different GUI applications such as games, menu layouts, organizers, etc..
"""

# import turtle as t

#Set up screen



#We will create a 5(rows)x7(columns) grid where each cell is 100x100 and there is a border of 50 around each edge.
#It could help sketching and labeling the dimensions on a paper to layout the logic
#Draw the vertical lines




#Draw the Horizontal lines


"""place a dot in the top left cell"""
pass #Move pen up
# To find the center of the first cell:
    #1) -350 is the left most point of the grid, we need to go halfway across this cell
    #2) 250 is the top most point of the grid, we need to go halfway down this cell.
pass
pass# Since each cell is 100x100, we can make that the diameter of the dot


t.done()



###Let's rewrite this program to allow us to create a grid based on the rows, columns, and column size desired
# import turtle as t

#Set grid variables to fully define custom grid and window



##Define window and edges based on variables


#Corners/edges


#Set up screen function




#Draw vertical lines  based on variables




#Draw horizonal lines



##Exercise 3.2
"""Write a function that accepts row, column, and color as a parameter.

The function should display a dot in the middle of the row, column specified with the color passed in. 
The dot should be the same diamater as the cell side legnth.
The  dot should draw correctly even if the number of rows, columns, and/or cell dimensions is changed.

So it should be defined relative to the grid and not in absolute terms

Finally, if the row and/or columns passed into the function exceeds the rows/columns the grid generates, the message 'out of range'
should be printed in the terminal."""

def place_dot(row:int, column:int, color = 'black'):
    pass


#Run functions
