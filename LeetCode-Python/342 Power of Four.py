"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:
    Input: 16
    Output: true

Example 2:
    Input: 5
    Output: false
    Follow up: Could you solve it without loops/recursion?
"""

def isPowerOfFour(num):
    # convert to binary string
    num = str(bin(num))[2:]
    # if the number is the power of 4, the rest of digits all should be zero
    num_of_zero = len(num) - 1
    # check the if the num is start with "1" and followed with n "0", where n is an even
    if num == "1" + ("0" * num_of_zero) and num_of_zero % 2 == 0:
        return True
    else:
        return False

input1 = 16
input2 = 2
input3 = 64

print(isPowerOfFour(input2))
