#///factorial
# def fact(n):
#   if (n==1 or n==0):
#     return 1    #BASE CASE
#   else:
#     return fact(n-1) * n  #RECURSIVE CASE

# print(fact(5))





#///Natural no. sum
# def cal_sum(n):
#   if (n==0):
#     return 0
#   else:
#     return cal_sum(n-1)+n

# sum = cal_sum(5)
# print(sum)






#///Fibonacci Series
#not resursion
# def fibo_series(n):
#   series=[]
#   if n>=0:
#     series.append(0)
#   if n>=1:
#     series.append(1)
#   for i in range(2,n+1):
#     next_fibo=series[i-1]+series[i-2]
#     series.append(next_fibo)
#   return series

# result =fibo_series(6)
# print(result)




#////
# def fibo_recur(n):
#   if n < 0: #base case
#     return []
#   elif n == 0:
#     return [0]
#   elif n == 1:
#     return [0, 1]
#   else: #recusive case
#     series = fibo_recur(n - 1)
#     next_fibo = series[n-1] + series[n-2]
#     series.append(next_fibo)
#     return series

# # Call the recursive function to get the series up to the 5th term
# result_series = fibo_recur(6)
# print(result_series)




# reverse a string
# def reverse_str(s):
#   if len(s)<=1:
#     return s
#   #recusive case
#   return reverse_str(s[1:]) +s[0]

# print(reverse_str("hello"))





# #palindrome
# def recur_palindrome(s):
#   if len(s)<=1:
#     return True
#   if s[0]!=s[-1]:
#     return False
#   return recur_palindrome(s[1:-1])

# print(recur_palindrome("madam"))





# #cal_sum of digits
# def cal_sum(n):
#   if n<10:
#     return n

#   return n%10 + cal_sum(n // 10) #n%10 give last digit + n//10 removes the last digit 
# #   #sum_digits(54321)
# # → 54321 % 10 + sum_digits(54321 // 10)
# # → 1 + sum_digits(5432)

# # → 1 + (2 + sum_digits(543))
# # → 1 + (2 + (3 + sum_digits(54)))
# # → 1 + (2 + (3 + (4 + sum_digits(5))))
# # → 1 + 2 + 3 + 4 + 5
# # → 15

# print(cal_sum(123))





# #power a^b
# def power(a,b):
#   if b ==0:
#      return 1
#   return a*power(a,b-1)

# print(power(2,5))





# #N -1
# def print_reverse(n):
#   if n==0:
#     return
#   print(n)
#   print_reverse(n-1)
# print(print_reverse(5))




# #no. of elements in list
# def count_elem(list):
#     if list ==[]:
#       return 0
    
#     return 1 + count_elem(list[1:])
# print(count_elem([1,2,3,4,5]))




# def max_elm(list):
#   if len(list)==1:
#     return list[0]

#   max_rest = max_elm(list[1:])
#   return list[0] if list[0]>max_rest else max_rest

# print(max_elm([1,2,3,4,5])) 