def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

# Calling the function
n = 5
print("Sum of first", n, "natural numbers:", sum_natural(n))
