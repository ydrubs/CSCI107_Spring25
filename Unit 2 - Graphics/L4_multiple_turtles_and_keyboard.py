"""In this lesson we will explore how to use multiple turtles for drawing on to the screen.
We create instance variables from the turtle class rather then using the generic class as in previous lessons.
"""
import turtle

## Create an instance of the turtle screen object
window = turtle.Screen()
window.setup(600,800)
window.bgcolor('yellow')


## Create an array to store multiple turtle objects
my_turtles = []

##Create and store turtles into the list

# turtle 1
larry = turtle.Turtle()
larry.pensize(3)
larry.pencolor('purple')
larry.penup()
my_turtles.append(larry)



# turtle 2
curly = turtle.Turtle()
curly.pensize(4)
curly.pencolor('blue')
curly.penup()
my_turtles.append(curly)


# turtle 3
moe = turtle.Turtle()
moe.pensize(5)
moe.pencolor('red')
moe.penup()
my_turtles.append(moe)


## Send commands to each turtle individuals
larry.goto(-200,200)
curly.goto(200,200)
moe.goto(0, -200)

##Send commands to each turtle by looping through the list
for trtl in my_turtles:
    trtl.shape('turtle')
    trtl.pendown()
    for _ in range(3):
        trtl.forward(50)
        trtl.right(120)

turtle.write("Turtle Power!!!", align='center', font=('Verdana', 25, 'normal'))# Write to the screen but with formatting

##Define functions for keyboard presses
# When up key is pressed trigger this function

def up():
    larry.setheading(90)
    larry.forward(speed)


# When down key is pressed trigger this function
def down():
    larry.setheading(270)
    larry.forward(speed)


# When left key is pressed trigger this function
def left():
    larry.setheading(180)
    larry.forward(speed)



# When right key is pressed trigger this function
def right():
    larry.setheading(0)
    larry.forward(speed)

def increase_speed():
    global speed
    speed += 2  # Increase speed by 2 units
    print(f"Speed increased to {speed}")


##Create a keypress listener and associate with a key
# Note that these methods come from the turtle class itself rather then instances of individual turtles
speed = 5

turtle.listen()
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')
turtle.onkey(increase_speed, 's')


turtle.done()
