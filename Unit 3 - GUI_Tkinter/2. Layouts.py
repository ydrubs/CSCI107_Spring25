"""
In this lesson we create a simple GUI that we can interact with. It will contain:
    - Buttons
    - Shapes
    - An image
    - An entry box

In a previous lesson we used the pack() method to place widgets (text) onto the screen,
here we will use another placement widget called grid() which gives us more control of our layout placement.

We also introduce the Pillows (PIL) library. A very popular library for working with images using Python.

The function for this lesson was adapted from this website: https://robotic-controls.com/learn/python-guis/basics-tkinter-gui
"""


pass # Import Tkinter
pass ##This library is for image processesing so we can resize an image

pass #Makes the window
pass #Makes the title that will appear in the top left
pass #White

##Functions to draw shapes onto the canvas when called
pass
    """
    The function that triggers automatically when the corresponding button is pressed

    Shapes accept ALOT of parameters.
    To specify its placement in a frame we have to specify the (x,y) of the TOP-LEFT corner and
    the (x,y) of the BOTTOM-RIGHT corner,

    Position of curved shapes such as ovals can be thought-of as though they were inscribed in a rectangle
    """
    pass

    # Allows us to apply text onto a text area the first argument, index represents where the text is inserted.
    # For instance 0.0 means first line character 1. If it was 2.3, we would be applying the next on line 2 character 3.
    pass

#Function to draw a yellow arc
pass

#Function to draw a green square
pass


#Left Frame and its contents
pass # Create a left-side frame and place it onto the root window
pass # Grid allows us to specify the row and column we want to place the frame relative to the master frame it is in (root here)

pass # Create some text and place that in the left frame. Note that we do this here with one line

pass # Some more text in the left frame
pass # and place it

##Try to open an image in current directory, print message if not found
pass
    ##Resize the image using the PIL package
    pass # open image
    pass # resize image
    pass # convert into a format that tkinter can use using a tkinter/PIL bridge

    ##Place the image
    pass

pass # if the image does not exist....
    pass # Do this


##Right Frame and its contents
pass


##Canvas for displaying shapes goes into the right frame
pass


##A seperate frame, inside the right frame, will hold the buttons to make placement easier
pass

##Entry box for displaying some text goes in the right frame
pass



# Create some buttons
# command argument is the callback function that gets triggered when the button is clicked (and released, by default)
pass


pass


pass

pass  #start monitoring and updating the GUI
