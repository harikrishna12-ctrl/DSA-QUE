n = int(input("enter the number of rows : "))


for i in range(2*n-1):
   if(i<n):
      for j in range(i):
         print("*",end=" ")

      print()
   else:
      for i in range(2*n-i):
         print("*",end=" ")

      print()