def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

# Calling the function
n = 5
print("Sum of first", n, "natural numbers:", sum_natural(n))


#print N to 1

def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n - 1)

# Example:
print_n_to_1(5)
# Output: 5 4 3 2 1
