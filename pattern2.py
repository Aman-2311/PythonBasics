rows = int(input("Enter the number of rows: "))

for i in range(rows // 2, rows, 2):
    # top left curve
    for j in range(1, rows - i, 2):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    print()

# lower part
for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end="")
    for j in range(1, i * 2):
        print("*", end="")
    print()
