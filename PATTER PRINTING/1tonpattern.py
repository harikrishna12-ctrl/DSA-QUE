
n=int(input("Enmter the number : "))
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print( )

for i in range(1,n):
    for j in range(1,i):
        print(j,end=" ")
    print( )



    
for i in range(1,n):
    for j in range(1,i):
        print(i,end=" ")
    print( )