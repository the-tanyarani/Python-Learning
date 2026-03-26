# Taking user input in Python
# In python, we can take user input directly by using 
# input() function.
# syntax:- variable=input()
# but input function returns the value as string. Hence we have 
# to typecast them whenever required to another datatype.
# variable= int(input())
# variable= float(input())
# we can also display a text using input function. 
a=input("Enter your name- ")
print("My name is ", a)
a=int(input("Enter your age-"))
print("Your age is ", a)