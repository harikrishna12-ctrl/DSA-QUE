n = int(input("enter the number : "))

a = 64
for i in range(1, n):
    for j in range(1, i + 1):
        z = a + j
        print(chr(z), end=" ")
    print()

x=n
b=1
for i in range(1, n):
    for j in range(n-i,0,-1):
        z = a + b
        b=b+1
        print(chr(z), end=" ")
    x=x-1
    b=1
    print()
