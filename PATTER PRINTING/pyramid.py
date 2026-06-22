n = int(input("Enter the number of rows: "))

for i in range(2 * n - 1):

    if i < n:
        for j in range(n - i - 1):
            print(" ", end="")

        for j in range(2 * i + 1):
            print("*", end="")

        print()

    else:
        z = i - n + 1

        for j in range(z):
            print(" ", end="")

        for j in range(2 * (n - z) - 3):
            print("*", end="")

        print()