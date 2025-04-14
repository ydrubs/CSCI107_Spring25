import turtle
import random
import math


##This class creates and draws individua rectangles
##It recieves the rect collection parameter in order to allow us to add rectangles to the list from the RectCollection class
# #We also pass turtle.Turtle into the class in order to allow us to use turtle methods on the objects created with the class
        #...otherwise we would not be abe to, unless we define turtle in the class itself

class RectBody(turtle.Turtle):
    def __init__(self, rect_collection, scaler, pos = (0,0)):
        super().__init__()

        self.x = pos[0]
        self.y = pos[1]

        self.scaler = scaler # Allows the size of the rectangle to be individually changed
        self.penup() #Don't draw until ready
        self.goto(pos) #set the rectangle objects position

        rect_collection.add_rect(self) #call the add method of the rectangle collection object in order to add the instance to a list


    ##method to draw each rectangle
    def draw(self):
        self.clear()
        self.fillcolor('green')
        self.begin_fill()

        # for _ in range(4):
        #     self.pendown()
        #     self.forward(20*self.scaler)
        #     self.right(90)
        # self.end_fill()

        for i in range(200):
            angle_rad = math.radians(i)
            x = 100 * math.cos(math.log(3) * angle_rad) * math.sin(angle_rad)
            y = 100 * math.cos(2.4 * angle_rad) * math.sin(angle_rad)

            self.goto(x+self.x,y+self.y)
            self.pendown()

"""
    Use trig for some extra funzies
        Make sure to add self.x and self.y as atttributes of each objects position 
"""



##This is the builder class that manages the set of objects created in the above class
##Pass width and height of the screen as parameters
class RectCollection:
    def __init__(self, width, height):

        self.rect_canvas = turtle.Screen() #create the screen
        self.rect_canvas.setup(width, height) #Setup screen dimensions
        self.rect_canvas.bgcolor('yellow') # Set the BG dcolor

        self.rect_collection = [] #List to hold the rectangles

    def add_rect(self, rect):
        self.rect_collection.append(rect)


    ##Method that adds the rectangle to the list
    pass



    ##Method that changes the size of the rectangles when called
        ##Iterate through:
        #...1) Randomly resize each rectangle
        #...2) Call the draw method for each rectangle
        #...3) Update the screen after each call to draw.
    def update_all(self):
        for rect in self.rect_collection:
            self.rect_canvas.tracer(0)
            rect.scaler = round(random.random()*4,1)# Change the size of each rectangle object
            print(rect.scaler)# Debug info
            rect.draw()# Call the draw method in the RectBody class for each object
            self.rect_canvas.update() # Update the screen



###Create objects and test
if __name__ == '__main__':
    # Create a screen object from the RectCollection class and individual objects from the rect_body class
    rect_container = RectCollection(600, 400)
    r1 = RectBody(rect_container, 1, (-50, -50))
    r2 = RectBody(rect_container, 2, (20, 0))
    r3 = RectBody(rect_container, 3, (90, 50))
    r4 = RectBody(rect_container, 4, (160, 100))

    # r1.draw()

    ##Iterate by calling each object in the list and using its draw method
    for rect in rect_container.rect_collection:
        rect.draw()


    #Call the update method from the RectCollection class
    rect_container.update_all()


    ##Show our rectangle object list in raw form
    pass


    turtle.done()#Update the screen
