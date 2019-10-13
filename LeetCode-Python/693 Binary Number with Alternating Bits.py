"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
    Input: 5
    Output: True
    Explanation:
    The binary representation of 5 is: 101

Example 2:
    Input: 7
    Output: False
    Explanation:
    The binary representation of 7 is: 111.

Example 3:
    Input: 11
    Output: False
    Explanation:
    The binary representation of 11 is: 1011.

Example 4:
    Input: 10
    Output: True
    Explanation:
    The binary representation of 10 is: 1010.
"""

def hasAlternatingBits(n):
    # convert the n to binary string
    binary_string = str(bin(n))[2:]
    last_digit = None
    is_alternating_bits = True
    # iterate over the binary string
    for i in range(len(binary_string)):
        if last_digit == None:
            last_digit = binary_string[i]
        else:
            if last_digit == binary_string[i]:
                is_alternating_bits = False
                break
            else:
                last_digit = binary_string[i]
    return is_alternating_bits

input1 = 5
input2 = 7
input3 = 11
input4 = 10

print(hasAlternatingBits(input4))
