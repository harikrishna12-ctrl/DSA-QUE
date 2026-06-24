n = int(input("Enter the number of rows: "))

for i in range(1,n):

    for j in range(0,i+1):
        print(i+j,end=" ")

    print()