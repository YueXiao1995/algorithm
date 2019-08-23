"""
Given a 32-bit signed integer, reverse digits of an integer.


Example 1:
    Input: 123
    Output: 321
"""

def reverse(x):
    Max_32_bit_int = 2147483648
    if x < 0:
        nums = list(map(int, str(-x)))
        i = 1
        result = 0
        for num in nums:
            result += num * i
            i *= 10
        if result > Max_32_bit_int:
            return 0
        else:
            return -result
    else:
        nums = list(map(int, str(x)))
        i = 1
        result = 0
        for num in nums:
            result += num * i
            i *= 10
        if result > Max_32_bit_int:
            return 0
        else:
            return result
print(reverse(1563847412))
