# List Methods
l=[1,77,4,7,8,67,7]

l.sort() # sort the element by incresing order
print(l)

l.sort(reverse=True) # decresing order
print(l)

l.append(56)# add element at the end
print(l)

l.reverse()# reverse the element 
print(l)

print(l.index(7))#return the index of the first occurance of the list item, # 7 is present at index 3.

print(l.count(7))# how many times 7 is present.

# m=l # if you wrtite this instead of m=l.copy() then the real l list will be changed.
m=l.copy()
m[0]=0
print(m) # this will only change the new list which is m(copy of l )

l.insert(3,50)# at index 3, 50 is replaced. 
print(l)
 
n=[900,1100,1200]
k=[l+n] # if you don't want to change real list
# l.extend(m) # if you want to change the real list which is l
print(k)




 
