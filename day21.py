

# FUNCTIONS ARGUMENT and RETURN STATEMENT


# There are 4 types of arguments that we can provide in a functions:
# ~ Default Arguments
# ~Keywords Arguments
# ~Variable length Arguments
# ~Required Arguments

###  1. Default Arguments:

# we can provide a default value while creating a function.
# This way the function assumes a default value even if a value is not provided in the funnc call for that argument.
# Example:
def name(first, mid="Rani", last="Singh"):
    print("Hello", first, mid, last)
name("Tanvi")
name("Tannu")



### 2. Keyword Arguments:

# We can provide arguments with key=value, this way the 
# interpreter recognizes the arguments by the parameter name.
# Hence, the order in which the arguments are passed does not matter 
def name(first, mid, last):
    print("Hello", first, mid, last)
# name(mid="Tanvi")  # It will also give error bcoz we have to provide value of each argument.
# name("Tannu","Kashyap")
name(first="Tanya", mid="Rani", last="Singh")
name( mid="Rani", last="Singh",first="Tanya")



### 3. Required Arguments:

# In case we don't pass the arguments with a key=value syntax,
# then it is necessary to pass the arguments in the correct positional order and the number 
# of arguments passed should match with actual function definition.
# Example1:-When number of arguments passed doesnot matach to the actual function definition.
def name(first, mid, last):
    print("Hello", first, mid, last)
# name(mid="Tanvi")
# name("Tannu","Kashyap") # doesnot matach to the actual function definition.

# Example2:- When number of arguments passed matches to the actual funtion definition.
def name(first, mid, last):
    print("Hello", first, mid, last)
    name(first="Tanya", mid="Rani", last="Singh")

 
### 4. Variable length Arguments:

# Sometimes we may need to pass more arguments than those defined in the actual
# funtion.This can be done using variable-length arguments.
# There are two ways to achieve this:
##  ARBITARY ARGUMENTS:
# While creating a function, pass a "before the parameter name while defining the function.The accesses the 
# arguments by prcessing them in the formof tuple.
# Example:
# def name(*name):
#     print ("Hello", name[0], name[1], name[2])
# name("Tanya", "Rani", "Singh")

def average(*numbers):
    print(type(numbers))# Here, the number type is tuple becoz we use * before parameter
    sum=0
    for i in numbers:
        sum= sum + i
    print("The average of ", sum /  len(numbers))
average(20,50)
average(40,47,50,33,23,36)




## Keyword Arbitary Arguments:
# While creating a function, pass a * before the parameter anme while defining the function. 
# The function accesses the arguments by processing them in the form of dictionary.

    # """here, we can give the value of arguments and 
    # when we use it as a function,the function 
    # will automatically access
    # the value and execute it."""
def average(a=5,b=7):
      print("The average of ",(a+b)/2)
average()
average(9)# if we just give one argument func will automatic get it as the value of 'a'.
average(b=13)
# """ but if we want to give argument of b (or other/second argument)
#                  we have to define it like b=.."""
  


# RETURN STATEMENT
# The return statement is used to return the value of the expression back to the calling function.
# Example:-
def name(fname, mname, lname):
    return "Hello" " "+fname+ " "+ mname+ " "+lname+ " " 
print(name("tanya", "rani","singh"))


# Example:-
def num(*numbers):
    sum =0
    for i in numbers:
        sum=sum+i
    return sum

c=num(34,56)
print(c)


#Example:-
def marks(a,b,c):
    return a+b+c
a=marks(40,60,56)
print(a)

