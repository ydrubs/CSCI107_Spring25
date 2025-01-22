"""
Review of Python Lists
"""

"""
1) Lists are defined with square brackets []
2) Lists can contain (most) data types including other lists
"""
lst = ['hello', 7, 3.5, True, ['red', 'green', 'blue']]
# print(lst)

# print(type(lst))


"""
1) Lists can be accessed using their index
2) The first element in the list is index zero
3) The last element can be access with the -1 index
"""
# print(lst[0])
# print(lst[4])
# print(lst[-1])

"""
You can check an element data-type of data with type()
"""
# print(type(lst[1]))
# print(type(lst[2]))
# print(type(lst[3]))



"""
Accessing an index that does not exist will given an index error
"""
# print(lst[5])
# print(len(lst))# How long is a list

# print(lst[len(lst)]) #This fails becasue the len commans starts at 1 so will return one more item than the list index holds



"""
A list holding other lists can be accessed using a 2-dimensional list
"""
# print(lst[4]) #THis is the inner list from above
# print(lst[4][0]) #The first element in that list
#
# print(len(lst[4]))

"""
You can also use slicing on a list like you can with strings
"""
# print(lst) #original list
# print(lst[1:4]) #Elements one to 3
# print(lst[:2]) #Elements 0 to 1
# print(lst[::2]) #Every other element
#
# print(lst[::-1])

# new_lst = lst[::2]
# inner_list = lst[4][::2]
# print(new_lst)
# print(inner_list)
# master_list = new_lst+inner_list
# print(master_list)


"""
You can add elements to a list by specifying the index they should be added into using bracket-notation
The element replaces the element currently in that position
"""

#
# lst[1] = 'Goodbye' #Replaces the int 2 in the lst
# print(lst)
# lst[-1] = True #Replaces the inner list
# print(lst)


"""
lists can be combined using '+'
"""
light_colors = ['yellow', 'white', 'pink']
dark_colors = ['black', 'blue', 'purple']

all_colors = light_colors + dark_colors

print(all_colors)

"""
Items can be added to the end of a list using the .append method
"""
all_colors.append('red')
print(all_colors)
all_colors.append('grey')
print(all_colors)

all_colors.insert(1, 'aquamarine')
print(all_colors)

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
