hour=int(input("Enter time(0-23) "))
# import time
# hour= time.localtime().tm_hour
if(hour<12):
  print("good morning sir")
elif(hour<18):
  print("good after noon")
# elif(time>=20):
#   print("good evenind sir")
else:
  print("good night")
