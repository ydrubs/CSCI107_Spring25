""""
Turtle graphics originated from the 'Logo' programming language as a way to teach
beginners how to work with graphics and code.

It uses a 'turtle' to draw graphics onto the screen. So sending movement commands to the tutorials
is analgous to drawing on to the screen.

The Turtle module could also be used for elaborate, complex graphics.
"""

import turtle as t

t.Screen() #Create the screen object

#Specify the size and location of the screen (second two parameters optional).
t.setup(600, 500, 0, 0) #screen width, screen height, horizontal distance from the top left of your computer screen, and vertical distance from the top left of your computer screen
t.bgcolor('SpringGreen3') #Set bg color
t.title("Demo for a screen") #set the title of the window

t.shape('turtle') #Change cursor to turtle; starts at position (x = 0, y = 0) by default.
# t.speed('slowest')

#Screen orientation
t.up() #lift pen up
t.goto(-300 + 50, 250 -50) #Upper left corner is negative width/2, postive height/2
t.write('(300,250)') #Upper right corner is positive widht/2, postive height/2
t.goto(300 - 50, 250 -50) #Lower left corner is negative widht/2, positive height/2
t.write('(300,250)') #Lower right corner is negative widht/2, negative height/2

t.down() #Put pencil at the middle of the screen
t.tracer(0) # Don't show turtle movement


#Define movements
# t.pendown() # place pen down
# t.forward(200)
# t.right(90)
# t.backward(50)
# t.right(30)
# t.forward(50)
#
# for i in range(30):
#     t.forward(100)
#     t.left(20)
#



t.pensize(6) #Change pen size
t. color('green') #Change color

#More drawing demos
t.up()
t.goto(-300,-250)
t.down()
t.goto(300,250)
t.up()
t.goto(-300,250)
t.down()
t.color('blue')
t.goto(300,-250)
#
# t.up()
# t.color('blue')


##Draw with a loop
t.goto(0,0)
t.up()
for i in range(12):
    t.goto(-300 + 50*i, 0)
    t.down()
    t.goto(-300+50*i+35, 0)
    t.up()


t.update() #redraws the screen (usually used after calling a change within a program so won't see effect here)
t.done() #Keep window open after drawing finishes
