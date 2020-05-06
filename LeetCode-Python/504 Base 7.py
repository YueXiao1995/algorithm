"""
Given an integer, return its base 7 string representation.

Example 1:
    Input: 100
    Output: "202"

Example 2:
    Input: -7
    Output: "-10"

Note: The input will be in range of [-1e7, 1e7].
"""

def convertToBase7(num):
    if num == 0:
        return "0"
    abs_num = abs(num)
    base7 = ""
    i = 0
    n = 1
    while True:
        if n < abs_num:
            n *= 7
            i += 1
        elif n == abs_num:
            i += 1
            break
        else:
            n //= 7
            break

    for j in range(i):
        base7 += str(abs_num//n)
        abs_num %= n
        n //= 7
    if num >= 0:
        return base7
    else:
        return "-" + base7


num1 = 100
num2 = -7

print(convertToBase7(num1))

print(convertToBase7(num2))
