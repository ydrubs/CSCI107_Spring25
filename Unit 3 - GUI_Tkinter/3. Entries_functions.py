"""
This program demonstrates how to grab data entered into a box and process it.
We also look at strategies for creating clean GUI's

In the previous program we built the frames and widgets for each section in-tandem.
In this example we seperate the layout from the widget design.

"""
import tkinter as tk
from random import randint

#Define window
root = tk.Tk()


"""
A common strategy in GUI design is to lay out your font and color pallatte to be used before creating the frames and widgets.
"""
##Layout color ideas: https://coolors.co
pass




##Define Functions (last)
pass
"Show a custom greeting based on value of entry box"
#Get the value of the entry box and use it to make a label
pass # gets the data in the entry box with the variable test_entry
pass # format the custom message



pass # place it in the output frame
pass # After clicking the button delete data in the entry box


pass
"Generate a list of random numbers"




#Build ALL Frames first, start with the input frame where the user will interact
pass
pass # fill = 'x' ensures the entire width of the frame is used regardless of how much space the widgets need(try removing this)

pass
pass # We don't need fill = 'x' here becuase this frame size adjust based on the one above.


#Turn off the ability to resize frame around a widget.
pass # Remove to see the effects


#Input widgets
pass  # Creates an entry box
pass
pass # Place default text into the entry box

# Create a button, like with most things in tkinter, there is lots of parameters we can set.
pass


# A button that generates a list of random numbers when clicked
pass
pass #Use (20,0) to ensure the right side aligns with widget above
# The columnspan parameter says that the widget should across both column
# The sticky parameter ensures that the widget stretches fully across both columns - this looks better

#Run the root window
root.mainloop()
