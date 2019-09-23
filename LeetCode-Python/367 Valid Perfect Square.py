"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
    Input: 16
    Output: true

Example 2:
    Input: 14
    Output: false
"""

def isPerfectSquare(num):
    if num < 2:
        return True
    start = 1
    end = num
    while end - start > 1:
        middle = (start + end) // 2
        if middle * middle > num:
            end = middle
        else:
            start = middle
    if start * start == num:
        return True
    else:
        return False

input1 = 16
input2 = 14
print(isPerfectSquare(input2))

