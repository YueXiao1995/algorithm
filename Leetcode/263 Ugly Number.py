"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:
    Input: 6
    Output: true
    Explanation: 6 = 2 × 3

Example 2:
    Input: 8
    Output: true
    Explanation: 8 = 2 × 2 × 2

Example 3:
    Input: 14
    Output: false
    Explanation: 14 is not ugly since it includes another prime factor 7.

Note:
    1 is typically treated as an ugly number.
    Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].
"""


def isUgly(num):
    # check if the num is a positive number
    if num <= 0:
        return False
    # check if the can be divided exactly by 2, 3, or 5
    while num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        if num % 2 == 0:
            num //= 2
        elif num % 3 == 0:
            num //= 3
        else:
            num //= 5
    # finally, if the num equal to 1, return True
    if num == 1:
        return True
    else:
        return False

input1 = 6
input2 = 8
input3 = 14
print(isUgly(input3))
