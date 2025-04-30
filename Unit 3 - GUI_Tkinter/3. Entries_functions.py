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
A common strategy in GUI design is to layout you font and color pallatte to be used.
"""
##Layout color ideas: https://coolors.co
root_color = 'teal'
input_color = '#B28B88'
output_color = '#8AE1FC'
button_color='#081D21'
button_font_color = 'white'
font = 'Arial'
root.config(bg=root_color)


##Define Functions (last)
def greet():
    "Show a custom greeting based on value of entry box"
    #Get the value of the entry box and use it to make a label
    greet_message = f"Hello {text_entry.get()}" # gets the data in the entry box with the variable test_entry
    greeting = tk.Label(output_frame, text=greet_message, # format the custom message
                        bg=output_color,
                        pady=5,
                        font=font)
    greeting.pack() # place it in the output frame
    text_entry.delete(0, 'end') # After clicking the button delete data in the entry box

def get_random_num():
    "Generate a list of random numbers"
    num = str([randint(1,20) for x in range(5)])
    tk.Label(output_frame, text=num, bg=output_color, pady=5, font=font).pack()

#Build ALL Frames first
input_frame = tk.Frame(root, bg=input_color, height=150, width=500)
input_frame.pack(fill='x', padx=10, pady=(10,0)) # fill = 'x' ensures the entire width of the frame is used regardless of how much space the widgets need(try removing this)

output_frame = tk.Frame(root, bg=output_color, height=300, width=500)
output_frame.pack(padx=10, pady=5) # We don't need fill = 'x' here becuase this frame size adjust based on the one above.


#Turn off the ability to resize frame around a widget.
output_frame.pack_propagate(False)# Remove to see the effects


#Input widgets
text_entry = tk.Entry(input_frame, width=40) # Creates an entry box
text_entry.grid(row=0, column=0, padx=20, pady=20, ipady=5)
text_entry.insert(0, "Enter your name") # Place default text into the entry box

# Create a button, like with most things in tkinter, there is lots of parameters we can set.
input_button = tk.Button(input_frame, text = 'Go!', bg=button_color, fg=button_font_color, font=font, command=greet)
input_button.grid(row=0, column=1, ipadx=20)


random_number_button = tk.Button(input_frame, text='Generate random Number', command=get_random_num)
random_number_button.grid(row=1, column=0, columnspan=2, sticky='ew', padx=(20,0), pady=(0,10)) #Use (20,0) to ensure the right side aligns with widget above
# The columnspan parameter says that the widget should across both column
# The sticky parameter ensures that the widget stretches fully across both columns - this looks better

#Run the root window
root.mainloop()
