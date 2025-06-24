row = int(input("Enter number of row: "))
for i in range(1,row+1):
    for j in range(i):
        print("*", end="")
    print()