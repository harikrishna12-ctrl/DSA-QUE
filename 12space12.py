n = int(input("Enter the number of rows: "))
x = 2 * n - 2

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range(1, x):
        print(" ", end=" ")

    for j in range(i,0,-1):
        print(j, end=" ")

    x = x - 2
    print()