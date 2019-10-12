"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
    The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    You could assume no leading zero bit in the integer’s binary representation.

Example 1:
    Input: 5
    Output: 2
    Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:
    Input: 1
    Output: 0
    Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""

def findComplement(num):
    # convert the num to binary string
    binary = str(bin(num))[2:]
    # flip the bits of the binary, get the binary string of the complement
    complement = ""
    for digit in binary:
        complement += (str(abs(int(digit)-1)))
    complement = str(int(complement))
    # convert the complement from binary to decimal
    decimal = 0
    time = 1
    for i in reversed(range(len(complement))):
        if complement[i] == "1":
            decimal += time
        time *= 2
    return decimal

input1 = 5
input2 = 2

print(findComplement(input1))

