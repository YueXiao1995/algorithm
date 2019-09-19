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
    factors = list()
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
    print(factors)
    return 0

input1 = 6
input2 = 8
input3 = 14
print(isUgly(input1))
