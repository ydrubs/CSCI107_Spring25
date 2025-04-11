"""In this lesson you will learn how to automate design tasks effectively by laying out windows with variables
and creating functions"""

import turtle as t

##Let's start by defining a few variables for our window.
##This will help generalize the dimensions when screen size changes
screen_width = 800
screen_height = 600

max_X = screen_width//2
min_X = -(screen_width//2)

max_Y = screen_height//2
min_Y = -(screen_height//2)



##Function to setup the screen
def screen_setup():
    t.Screen()
    t.setup(screen_width, screen_height)
    t.bgcolor('cyan')
    t.title('Turtle function practice')



# Write the dimensions of the screen on the screen
def screen_dimension_write():
    t.up()
    t.goto(min_X +10, min_Y+10)
    loc = str(min_X) + ',' + str(min_Y)
    t.write(loc)

    t.up()
    t.goto(max_X -100, min_Y+10)
    loc = str(max_X) + ',' + str(min_Y)
    t.write(loc)

    t.up()
    t.goto(max_X -100, max_Y-20)
    loc = str(max_X) + ',' + str(max_Y)
    t.write(loc)

    t.up()
    t.goto(min_X +10, max_Y-20)
    loc = str(min_X) + ',' + str(max_Y)
    t.write(loc)




## Function to draw the border.
def draw_border(offset : int, color='black', size = 5):
    """
        This function draws a border around the screen

        Args:
            offset (int): The offset of the border-lines from the ege of the screen
            color (str): The color of the border-lines
            size (int): Changes the size of the border

        Returns:
            None
    """
    t.up()
    t.pensize(size)
    t.color(color)

    t.goto(max_X-offset, max_Y-offset)
    t.down()

    t.goto(max_X - offset, min_Y + offset)
    t.goto(min_X + offset, min_Y + offset)
    t.goto(min_X + offset, max_Y - offset)
    t.goto(max_X - offset, max_Y - offset)



###Use our functions
screen_setup() #Setup the screen
screen_dimension_write() #Write the dimensions of the screen to the screen

draw_border(50) # Draw a border in black
draw_border(100, 'green')# Draw a border in green
draw_border(10, 'purple', 1) # Draw a border in purple


t.done()
