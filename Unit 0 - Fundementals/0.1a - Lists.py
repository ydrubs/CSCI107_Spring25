"""
Review of Python Lists
"""

"""
1) Lists are defined with square brackets []
2) Lists can contain (most) data types including other lists
"""
pass
pass


"""
1) Lists can be accessed using their index
2) The first element in the list is index zero
3) The last element can be access with the -1 index
"""
pass
pass
pass


"""
You can check an element data-type of data with type()
"""
pass
pass
pass



"""
Accessing an index that does not exist will given an index error
"""
pass
pass #This fails becasue the len commans starts at 1 so will return one more item than the list index holds



"""
A list holding other lists can be accessed using a 2-dimensional list
"""
pass #THis is the inner list from above
pass #The first element in that list


"""
You can also use slicing on a list like you can with strings
"""
pass #original list
pass #Elements one to 3
pass #Elements 0 to 1
pass #Every other element


"""
You can add elements to a list by specifying the index they should be added into using bracket-notation
The element replaces the element currently in that position
"""
pass

pass #Replaces the int 2 in the lst
pass#Replaces the inner list
pass


"""
lists can be combined using '+'
"""
#light_colors = ['yellow', 'white', 'pink']
#dark_colors = ['black', 'blue', 'purple']

pass

pass

"""
Items can be added to the end of a list using the .append method
"""
pass
pass

pass

"""
The insert method can also add items to a list by putting it at the indicated index 
This shifts the element at that current position and all the others over one
"""
pass
pass


"""
The for command can loop through and act on individual elements
"""
pass #Loop using the elements themselves


pass #Loop Using the index (positions) of the elements

"""
The .pop method removes an element and stores it into memory (if needed) 
If .pop is used without an argument it removes the last element
"""
pass

pass
pass

pass
pass


"""
We can also return the index location given a list element using the .index method
"""
pass
pass #We get an error if an argument is not in the list. We will learn to handle it later


"""
We can use the 'in' command to see if an element exists in the list
"""

pass
pass


"""
We can sort a list in two ways 
"""
a = [3,6,1,8]
b = [3,6,1,8]

#Mutates the original list
pass
pass

#Returns a new list that is a sorted version of the original
pass
pass # Notice this did not work. This is because sorted() returned a new list but we did not save it to a variable

pass #Saving it to a variable
