n = int(input(" enter the number of rows: "))
z=1
for i in range(1,n):
   
    for j in range(1,i+1):
        print(z,end=" ")
        z= z+1
    print()