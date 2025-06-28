# #function defination
# def sum(a,b):       #fd (parameter)
#     sum=a+b
#     return sum     
# print(sum(2,3))       #funt_name(argument1,arg2)

#vowel
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Calling the function
text = "Hello World"
result = count_vowels(text)
print("Number of vowels:", result)


#Mean of number
def find_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

# Calling the function
data = [5, 10, 15, 20]
average = find_mean(data)
print("Mean of the list:", average)
