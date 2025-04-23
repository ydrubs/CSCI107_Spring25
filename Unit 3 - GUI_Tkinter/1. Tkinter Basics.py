"""
In this lesson we will look at creating a window using the Tkinter package,
processing text, and placing page elements in a window.

"""
import pass # import tkinter
import pass # import itertools


##Defining a window
pass #Define the root window
pass #Give the window screen a title
pass #Set the size of the window, x,y offset
pass #Don't allow window resizing (default is 1,1)

#Limit resize dimensions if resizing allowed
pass
pass

# set a background color
pass # We can also use hex by combing the numbers 1-9 and AF such as '#FFAA11'

# Some text we can use for demo purposes
txt = ['We set sail on this new sea because there is new knowledge to be gained',
       'Its conquest deserves the best of all mankind',
       'We choose to go to the moon.',
       'We choose to go to the moon in this decade and do the other things',
       "Well, space is there, and we're going to climb it"
       ]
pass # Allows us to grab the next element from the list without keeping track of the index

##Create text widgets(labels)
pass #Create a text widget in the root window
pass #place it in the first available spot

pass
pass #give it top and bottom padding

pass #Change font, font-size, bold, and color
pass

pass
pass #Add only padding, below, add internal padding (inside the text widget), align-left

pass
pass #Fill up all widget space in x-direction (could aldo do y and 'both', add some padding



"""Combination of useful parameters:

text: This is the text that will be displayed on the label.

font: This is used to specify the font type, size, and style of the text. It takes a tuple with the font name, size, and style (optional).

bg: This is used to set the background color of the label.

fg: This is used to set the color of the text.

padx and pady: These are used to add horizontal and vertical padding around the text.

relief: This is used to specify the type of the border. The options are RAISED, SUNKEN, FLAT, RIDGE, GROOVE, and SOLID.

bd or borderwidth: This is used to specify the width of the border.

anchor: This is used to specify the position of the text within the label. The options are the points of the compass: N, NE, E, SE, S, SW, W, NW, and CENTER.

justify: This is used to specify the alignment of multiple lines of text. The options are LEFT, RIGHT, and CENTER.

wraplength: This is used to specify at what length to wrap the text."""

label = tk.Label(root,
                 text="Hello, Tkinter!",
                 font=("Arial", 20, "bold"),
                 bg="yellow",
                 fg="red",
                 padx=10,
                 pady=10,
                 relief="solid",
                 bd=2,
                 anchor="nw",
                 justify="center",
                 wraplength=100)

label.pack()


#Run the mainloop
pass # This is necessary to keep the window open
