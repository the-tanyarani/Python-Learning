
# Manipulating Tuples:- Tuples are immutable, hence if
# you want to add, remove or change tuple items, 
# then first you must convert the tuple to a list.
# Then perform operation on that list and convert it back to tuple.
countries =("Spain", "Italy","India", "England", "Germany")
temp=list(countries) #convert tuple to list
temp.append("Russia") # add item at the end
temp.pop(3)#remove item
temp[2]= "Finland"#change item
countries =tuple(temp) #convert list to tuple
print(countries)
# print(temp)


# However, we can concatenate two tuples without converting them to list.
countries=("Pakistan", "Afghanistan", "Bangladesh")
countries2= ("Vietnam", "India", "China")
southEastAsia = countries+countries2
ten = list(southEastAsia)
ten.sort()
southEastAsia=tuple(ten)
print(southEastAsia)


# count(Method)
# The count() method of Tuple returns the number of times the given element appears in the tuple.
# Syntax:- tuple.count(element)
tuple1 =(0,1,2,3,4,3,5,3,5)
res= tuple1.count(3)
yes=tuple1.count(5)
print("Count of 3 in tuple is:", res)
print("Count of 5 in tuple is:", yes)


# index() method:- The Index()method returns the firrst occurance of the given element from the tuple.
# The index() method raises a ValueError if the element is not found
# in the tuple.
# Syntax:- tuple.index(element, start, end)
res= tuple1.index(5)
tup= tuple1.index(3,1,7)
print("First occurance of 5 is ", res)
print("First occurance of 3 is ", tup)


# Tuple methods:- As tuple is immutable type of collection of elements it has limited 
# built in methods. 



