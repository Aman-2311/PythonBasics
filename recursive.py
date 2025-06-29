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


# Print 1 to N recursively
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n)

print_1_to_n(5)
# Output: 1 2 3 4 5


# Recursive factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))