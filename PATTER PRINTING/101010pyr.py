n =int(input("enter the number of rows: " ))
for i in range(1,n):

    for j in range(1,i+1):
      if((i+j)%2==0):
       print("1",end=" ")
      else:
       if(j!=0):
        print("0",end=" ")
   
    print()



# n = int(input("Enter the number of rows: "))

# for i in range(1, n + 1):
#     for j in range(i):
#         if (i + j) % 2 == 0:
#             print("1", end="")
#         else:
#             print("0", end="")
#     print()