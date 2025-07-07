import numpy as np

n = input("Enter a number: ")
digits = np.array([int(d) for d in n if d.isdigit()])

even_mask = digits % 2 == 0
odd_mask = digits % 2 != 0

even_count = np.sum(even_mask)
odd_count = np.sum(odd_mask)

even_sum = np.sum(digits[even_mask])
odd_sum = np.sum(digits[odd_mask])

even_mean = np.mean(digits[even_mask]) if even_count else 0
odd_mean = np.mean(digits[odd_mask]) if odd_count else 0

std_dev = np.std(digits)

print(f"Even digits: {even_count} (Sum: {even_sum}, Mean: {even_mean})")
print(f"Odd digits : {odd_count} (Sum: {odd_sum}, Mean: {odd_mean})")
print(f"Standard Deviation of all digits: {std_dev:.2f}")