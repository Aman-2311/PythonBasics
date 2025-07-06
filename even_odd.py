def even_odd_check(n):
    even =0
    odd =0
    for digit in n:
        if digit.isdigit():
            if int(digit) % 2 == 0:
                even +=1
            else:
                odd+=1
    return even,odd

n = input("enter a number : ")
even,odd = even_odd_check(n)
print(f"Even digits: {even}")
print(f"Odd digits: {odd}")
