import numpy as np
n = input("Enter a number: ")

digits =np.array([int(d) for d in n if d.isdiigit()])

#boolean masks
even_mask =(digits % 2 == 0)
odd_mask =(digits % 2 == 0)

#count
even_count =np.sum(even_mask)
odd_counts =np.sum(odd_mask)

print(f"Even digits : {even_count}")
print(f"Odd digits: {odd_counts}")