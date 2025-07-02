#Simple Data Analyzer
#mean#median#stdandard#maximum#minimum

import numpy as np
user_input = (input("enter numbers : "))
num_list = [float(i) for i in user_input.split()]

data = np.array(num_list)

def calculate_mean (arr):
    return np.mean(arr)
def calculate_median (arr):
    return np.median(arr)
def calculate_std (arr):
    return np.std(arr)
def calculate_max(arr):
    return np.max(arr)
def calculate_min(arr):
    return np.min(arr)

print("\n Data analysis ")
print(f"Data: {data}")
print(f"Mean: {calculate_mean(data)}")
print(f"Median: {calculate_median(data)}")
print(f"standard: {calculate_std(data)}")
print(f"Maximum: {calculate_max(data)}")
print(f"Minimum: {calculate_min(data)}")