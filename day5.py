""" To comment the line we use (#) and we can also use
tripple single code ('''  ''') or triple double code (""" """).""" 

# To change the line we use  \n
print("hey! \nI am Tanya Rani.")

#Escape sequence character
""" -> To insert characters that cannot be directly used in a 
       string, we use an escape sequence character.
    -> An escape sequence character is a backslash \ followed by the 
       character you want to insert. 
    -> An example of a  character that cannot be directly used
       in a string quote inside a string that is surrounded by double quote.
       print(" hey, MY NAME IS " TANYA RANI ") <- it will give an error"""
   
print("hey, my name is \"TANYA RANI\" ")

# Other parameters of print statement
""" 1. object(s):- Any object, and as many as you like, will be converted into string before printed.
    2. sep='separator':-Specify how to separate the objects, if there is more that one. Default is.
    3. end='end' :- Specify what to print at the end. Default is '\n'
    4. file:-An object with a write methid. Default is sys.stdout"""
print(" hey " ,5,6, sep="~", end="009\n") # end is use to print whatever we want to print in last of the line
print("Tanya")
