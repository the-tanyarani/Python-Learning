# Typecasting
# The conversion of one data type into other data type is called typecasting. 
a="Tanya "
b="Rani"
print(a+b)
# Typs of typecasting
# 1. Explicit typecasting :- The conversion of one data type into another 
# data type done via developer
x="9"
y="5"
print(int(x)+int(y))
# 2. Implicit typecasting :- The conversion of one data type
#  into another data type automatically,
#  Python converts a smaller data type to a higher data type to prevent data loss.
p= 3.6
q= 8
print((p)+ (q))  # Python automatically changed the int data type into
                 # float (smaller D.T intp higher D.T. )
