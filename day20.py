### PYTHON FUNCTIONS
# A function is a block of code that performs a specific task whenever it is called.
#  In bigger programs, where we have large amounts of code, 
# it is advisable to create or use existing functions
#  that make the program flow organized and neat.
# There are two types of functions:
# 1. BUILT-IN FUNCTIONS
# 2. USER-DEFINED FUNCTIONS

### 1. BUILT-IN FUNCTIONS:-
# These functions are defined and pre-coded in python.
# Some examples of this functions are as follows:
# min(), max(), len(),sum(), type(),range(),dict(),list(),tuple(),
# set(),print(),etc.
# Examples:
a=10
b=20
# sum(a,b) -> this will give error bcoz sum func will not accept integer , it accepets tupple/list.
print(sum([a,b]))




### 2. USER-DEFINED FUNCTIONS:-
# We can create functions to perform soecific tasks as per our needs.
# such functiond are called user-defined functions.
def function_name(parameters):
    pass # pass is used when we want to define the funtions's work later.
# Any parameters and arguments should be placed within the parenthesis.
# Rules to naming functions are similar to that of naming variables. f
# Examples:-

# without using user defined func we have to repeat codes again and again like
a=100
b=20
if(a>b):
    print("The first num is greater")
else:
        print("The second num is greater or equal")

#Here,if we have to find out the greater or smaller num again and again
#  we have to write the code on repetitive mode so in this scenerio 
#  we can make a user defined function to ignore the big code 
def greaternum(a,b):
    if(a>b):
     print("The first num is greater")
    else:
     print("The second num is greater or equal")
a=30
b=200
(greaternum(a,b)) # To call the function we just write the function name not the print().

