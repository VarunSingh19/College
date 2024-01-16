
# first program.
print("Hello, World!")

# <-------------Variables------------->
# A variable is created the moment you first assign a value to it.


# -----------------------------------------------------

def variables():
    a = 4       # x is of type int
    a = "Sally" # x is now of type str
    print(a)
    print(type(a))


    x = str(3)    # x will be '3'
    y = int(3)    # y will be 3
    z = float(3)  # z will be 3.0

# variables()

# -----------------------------------------------------

# <------------Built-in Data Types------------->
# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:

# Text Type:	  str
# Numeric Types:  int, float, complex
# Sequence Types: list, tuple, range
# -list : 
x = ["apple", "banana", "cherry"]
# -tuple :
x = ("apple", "banana", "cherry")
# -range : 
x = range(6)

# Mapping Type:	  dict
# -dict : 
x = {"name" : "John", "age" : 36}

# Set Types:	  set, frozenset
# -set : 
x = {"apple", "banana", "cherry"}
# -frozenset : 
x = frozenset({"apple", "banana", "cherry"})

# Boolean Type:	  bool
# Binary Types:	  bytes, bytearray, memoryview
# None Type:	  NoneType

# -----------------------------------------------------

# <-----------Python Casting ----------->
# Specify a Variable Type
# There may be times when you want to specify a type on to a variable. 
# This can be done with casting. Python is an object-orientated language,
# and as such it uses classes to define data types, including its primitive types.

# Casting in python is therefore done using constructor functions:

# - int() - constructs an integer number from an integer literal, 
# a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# - float() - constructs a float number from an integer literal,
#  a float literal or a string literal (providing the string represents a float or an integer)
# - str() - constructs a string from a wide variety of data types, 
# including strings, integer literals and float literals
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

# -----------------------------------------------------

# <---------Python Operators------->
# Operators are used to perform operations on variables and values.
# In the example below, we use the + operator to add together two values:

def operators():
    a=5
    b=4
    print("Addition :",a+b)
    print("Subtraction :",a-b)
    print("Multiplication :",a*b)
    print("Division :",a/b)
    print("Module :",a%b)

# operators()

# -----------------------------------------------------

# <--------Python Lists------->

def lists():
    mylist = ["apple", "banana", "cherry"]
    print(mylist)
    print(len(mylist))

    list1 = ["apple", "banana", "cherry"]
    list2 = [1, 5, 7, 9, 3]
    list3 = [True, False, False]
    list4 = ["abc", 34, True, 40, "male"]
    print(type(mylist))
    # print(type(list1))
    # print(type(list2))
    # print(type(list3))
    # print(type(list4))

# To add an item to the end of the list, use the append() method:
    thislist = ["apple", "banana", "cherry"]
    thislist.append("orange")
    print(thislist)

# To insert a list item at a specified index, use the insert() method.

    thislist1 = ["apple", "banana", "cherry"]
    thislist1.insert(1, "orange")
    print(thislist1)

# To append elements from another list to the current list, use the extend() method.

    thislist2 = ["apple", "banana", "cherry"]
    tropical = ["mango", "pineapple", "papaya"]
    thislist2.extend(tropical)
    print(thislist2)

# The remove() method removes the specified item.

    thislist3 = ["apple", "banana", "cherry"]
    thislist3.remove("banana")
    print(thislist3)

# The pop() method removes the element at the given position.
    thislist4 = ["apple", "banana", "cherry"]
    thislist4.pop()
    print(thislist4)

# The clear() method empties the list.
# The list still remains, but it has no content.

    thislist5 = ["apple", "banana", "cherry"]
    thislist5.clear()
    print(thislist5)

# -----------------------------------------------------

# lists()

# <----------Python - Loop Lists---------->
# You can loop through the list items by using a for loop:
# Print all items in the list, one by one:

def loops():
    thislist = ["apple", "banana", "cherry"]
    # for x in thislist:
    #  print(x)

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
# Print all items by referring to their index number:

    thislist = ["apple", "banana", "cherry"]
    # for i in range(len(thislist)):
        # print(thislist[i])

# -----------------------------------------------------

# <------Using a While Loop----->
# You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list, 
# then start at 0 and loop your way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.


    thislist = ["apple", "banana", "cherry"]
    i = 0
    while i < len(thislist):
        print(thislist[i])
        i = i + 1
# loops()

# -----------------------------------------------------

# <--------List Comprehension-------->
# List comprehension offers a shorter syntax when you want to create a new list
# based on the values of an existing list.
# Example:
# Based on a list of fruits, you want a new list, 
# containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write 
# a for statement with a conditional test inside:

def Comprehension():
    fruits = ["apple", "banana", "cherry ", "kiwi", "mango"]
    newlist = []

    for x in fruits:
        if "a" in x:
            newlist.append(x)
    print(newlist)

# Comprehension()

# -----------------------------------------------------


# <--------Python - Sort Lists------->
# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically,
# ascending, by default:


def sorts():
# Sort the list alphabetically:
    # thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
    thislist = [4342,22,323,2,3,1,422]
    thislist.sort()
    print(thislist)
    
    # To copy the list into another list.
    mylist = thislist.copy()
    print(mylist)

    # to add two list.
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    list3 = list1 + list2
    print(list3)

    # To append list2 into list1
    for x in list2:
        list1.append(x)
    print(x)
# sorts()

# -----------------------------------------------------

# <-----List Methods----->
# Python has a set of built-in methods that you can use on lists.
# Method	    Description
# append()	Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count() 	Returns the number of elements with the specified value
# extend() 	Add the elements of a list (or any iterable), to the end of the current list
# index() 	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()   	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()  	Sorts the list

# -----------------------------------------------------


# <-----Python Dictionaries----->

def dictionaries():
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2023, #duplicates not allowed thats why new value will be alpha.
    "colors": ["red", "white", "blue"]
    }
    # print(thisdict)
    # print(thisdict["brand"])
    # print(len(thisdict))

    # The dict() Constructor
    # It is also possible to use the dict() constructor to make a dictionary.
    # Using the dict() method to make a dictionary:
    thisdict1 = dict(name = "John", age = 36, country = "Norway")
    print(thisdict1)

# dictionaries()

# -----------------------------------------------------


# <--------Python If ... Else------->
# Python Conditions and If statement

def ifElse():
    a = 33
    b = 200
    # if else ladder

    # if b > a:
    #     print("b is greater than a")
    # elif a == b:
    #      print("a and b are equal")
    # else:
    #      print("a is greater than b")
    
    # Short Hand If
    print("A") if a > b else print("=") if a == b else print("B")
# ifElse()

# -----------------------------------------------------



# <-------The while Loop----->
# With the while loop we can execute a set of statements as long as a condition is true.

# Example:
# i = 1
# while i < 6:
#   print(i)
#   if i==3:
#       break
#   i += 1

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# -----------------------------------------------------

# <--------Python For Loops----->
# A for loop is used for iterating over a sequence (that is either a list,
# a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages,
# and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements,
# once for each item in a list, tuple, set etc.

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break
  
# for x in range(2,6):
#   print(x)

# -----------------------------------------------------

# <-----Python Functions----->
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# ohh god fuvk it... i was doing this from the start how stupid that im  writing this shit off fr ngl...

# -----------------------------------------------------