### BREAK STATEMENT
# The break statement enables a program to skip over a part of the code. 
# A break statement terminates the very loop it lies within.
# Example:
# for i in range(10):
#    print(i)
#    if i==5:
#     break

# for p in range(1,101,1):
#   print(p,  end=' ')
#   if(p==50):
#     break
#   else:
#     print("miss")
# print("Thank You")


#   Write the table of 5
# for i in range(15):
#     print( " 5 * ",i+1, "= ", 5*(i+1))
#     if (i==10):
#      break



### CONTINUE STATEMENT
# The continue statement skips the rest of the loop 
# statement and causes the next iteration to occur.
# example
for l in range(0,10,2):
  if(l%2 != 0):
    continue
  print(l)

#   we can also take range in list form.
for i in[2,4,6,8,3,7,0]:  #Here, the range is in list form.
  if(i%2 !=0):
    continue
  print(i)