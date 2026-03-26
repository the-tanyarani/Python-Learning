# Strings are immutable (can't be changed)
# ........String methods..........

#1. Length of string
a="Tanya"
print(len(a))


#2. Every cahracter of string in upper case
print(a.upper())


#3. Every character of string in lower case
print(a.lower())


#4. rstrip():- It removes any trailing characters.
b="!!!Tanya!!"
print(b.rstrip("!")) # It will remove ! only after of tanya.


#5. replace():- It replaces all occurances of a string with another string.
print(b.replace("Tanya", "Tanvi"))


#6. split():- It splits the given string at the specified instance and
#             returns the separated strings as list items.
d="Tanya Rani"
print(d.split(" "))
c="!!!!!utanuyau!!u!!!"
print(c.split("!"))


#7. capitalized():- first character -> upper case
#                   rest character -> lower case
#                   no effect -> if already in upper case
str="welcome to my youtube channel"
print(str.capitalize())


# 8. center():-It aligns the string to the center 
# as per the parameters given by the user.
# d=(c.center(100,(".")))
# print(d)
# print(len(b))
# print(len(d))
# a="AbfDacac"

# b=int(a.count("a"))
# c=int(a.count("A"))
# # print(b+c)
# # t="will you marry me"
# # print(t.endswith("Me"))
# a="His  Gentle BOy"
# # print(a.find("is"))
# # print(a.find("girl"))
# print(a.istitle())
