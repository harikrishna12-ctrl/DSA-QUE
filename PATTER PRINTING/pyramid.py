n = int(input("Enter the number of rows: "))

ml=n//2+1
nsp=n//2
nst=1

for i in range(1,n+1):

    for j in range(nsp):
        print(" ",end=" ")


    for j in range(nst):
        print("*",end=" ")


    if(i<ml):
        nst=nst+2
        nsp=nsp-1


    else:
        nsp=nsp+1
        nst=nst-2

    print()