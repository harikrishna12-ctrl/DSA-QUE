n= int(input("enter the number : "))

# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end="")

#     print( )



# for i in range(n,1,-1):
#     for j in range(1,i):
#         print(j,end="")

#     print( )


# for i in range(1,n):
#     for j in range(0,n-i-1):
#         print(" ",end="")

#     for j in range(2*i-1):
#         print("*",end="")
    
#     print( )
    




for i in range(0,n):


    for j in range(n-i-1):
        print("*",end="")
    
    print( )

    for j in range(0,i+1):
        print(" ",end="")
    
    
    