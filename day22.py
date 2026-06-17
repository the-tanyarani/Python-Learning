# List
# ~List are ordered collection of data items.
# ~They store multiple items in a single variable.
# ~List items are separated by commas and enclosed within square brackets[].
# ~Lists are changeable meaning we can alter them after creation.
# Example:-
list1=[34,5,6,78]
list2=["Red","Green", "Blue","Yellow"]
print(list1)
print(list2)


# As we can see, a single list can contain items of different data types.
list3=[34,5,6,78,"red"]
print(list3)


### List Index
# Each item has its own unique index and it can be 
# used to access any particular item from the list.
#Example:-
colors=["Red","Green", "Blue","Yellow"]
#        [0]    [1]     [2]     [3]


# Accessing list items
# we can access list items by using its index with 
# the square bracket[]
print(colors[0])
print(list2[2])

# Positive indexing:- same as like string
# Negative indexing:- same as like as string.
# length of list-negative indexing= positive indexing.


# Checking whether an item is present in the list?
list4=["Tanya", "Tanvi","Neha",]
if "Tanya" in list4:
    print("Yes, Tanya is present in list4")
else:
    print("No")
# This same thing is applied on string


# Slicing
list3=[34,5,6,78,"red"]
print(list3[:]) #all element will be printed, it will automatically accepted as [0:len(list)]
print(list3)    #all element will be printed
print(list3[1:])#all element will be printed but started from index [1]
print(list3[1:4])#all element will be printed but started from index [1] and ended at index[3] except [4].
print(list3[1:4:2])#started from index[1] and will jump from 1 element and ended without printing index[4]


# List Comprehension:-
# List Comprehensions are used for creating new lists from other iterables like lists,tuples,dictionaries,sets and even
# in arrays and strings.
# SYNTAX:
# List=[Expression(item) for item in iterable if condition]
# Expression:-It is the item which is being iterted.
# Iterable:-it can be list, tuples, dictionaries,sets and even in arrays and strings.
# Conditions:-Condition checks if the item should be added to the new list or not.
# Example 1.-
list = [i for i in range(10)]
print(list)
list = [i*i for i in range(20)]
print(list)
list = [i for i in range(10) if i%2==0]
print(list)
 
# Example 2:-
names=["Hilo", "Sarah", "Bruno","Ananya","Rosa"]
namesWith_a = [i for i in names if "a" in i]
print(namesWith_a)

# Example 3:-
namesWith_o= [i for i in names if (len(i)>4)]
print(namesWith_o)