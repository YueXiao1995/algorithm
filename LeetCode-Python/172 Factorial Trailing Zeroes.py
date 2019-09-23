"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:
    Input: 3
    Output: 0
    Explanation: 3! = 6, no trailing zero.

Example 2:
    Input: 5
    Output: 1
    Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.
"""

# Time Limit Exceeded
"""
def trailingZeroes(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    num_of_trailing_zeroes = 0
    num = str(num)
    print(num)
    for i in reversed(range(len(num))):
        if num[i] == '0':
            num_of_trailing_zeroes += 1
        else:
            break
    return num_of_trailing_zeroes
"""
# Time Limit Exceeded
"""
def trailingZeroes(n):
    # because 10 = 2 * 5, so iterate the number form 1 to n, calculate the number of factor 2 and 5 in those numbers
    number_of_five = 0
    num = 5
    while num <= n:
        num_copy = num
        while num_copy % 5 == 0:
            number_of_five += 1
            num_copy //= 5
        num += 5
    return number_of_five
"""

def trailingZeroes(n):
    # each trailing zero in n! actually comes from 2 * 5
    # because there are so many 2 among factors, so the key is to find the number of 5
    # 5, 10(2*5), 15(3*5)...  contains only one 5
    # 25(1*5*5), 50(2*5*5)... contains two 5
    # 125(1*5*5*5), 250(2*5*5*5) contains three 5
    #...
    result = 0
    num = 5
    while num <= n:
        result += n // num
        num *= 5
    return result

input1 = 3
input2 = 5
input3 = 8417
print(trailingZeroes(30))

# 5! = 120
# 10! = 3628800
# 15! = 1307674368000
# 20! = 2432902008176640000
# 25! = 15511210043330985984000000
