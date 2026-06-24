n = int(input("enter the number : "))

a = 64
for i in range(1, n):
    for j in range(1, i + 1):
        z = a + j
        print(chr(z), end=" ")
    print()
