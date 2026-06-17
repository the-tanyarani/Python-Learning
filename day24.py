# Tuple:- Tuples are ordered collection of data items. They store multiple items in a single variable.
# Tuple items are separated by commas and enclosed within round brackets().
# Tuples are unchangeable meaning we can not alter them after creation.
tuple=(1,2,303,4,"red",True)
print(tuple)
print(type(tuple))
# tuple=(1)
# print(type(tuple))# it will give int data type
# tuple=(1,)
# print(type(tuple)) #if you want  tuple data type on one element then comma(,) is necessary after data.
print(len(tuple))
print(tuple[0])
print(tuple[1])
print(tuple[2])
print(tuple[3])
print(tuple[-3])
print(tuple[-1])

# Checking 
if 302 in tuple:
    print("Yes, 303 is present ")
else:
    print("not present")


#Slicing
tup=tuple[1:5] #This will not change tuple, it creates a new tuple (tup)
print(tup)