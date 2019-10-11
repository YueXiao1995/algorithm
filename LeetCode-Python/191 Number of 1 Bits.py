"""
"Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

Example 1:
    Input: 00000000000000000000000000001011
    Output: 3
    Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
    Input: 00000000000000000000000010000000
    Output: 1
    Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
    Input: 11111111111111111111111111111101
    Output: 31
    Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Note:
    Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.

Follow up:
    If this function is called many times, how would you optimize it?
"""

def hammingWeight(n):
    # convert the int n to binary string
    binary_string = ""
    while n > 0:
        binary_string = str(n % 2) + binary_string
        n //= 2
    # count the number of "1" in the binary string
    hamming_weight = 0
    for digit in binary_string:
        if digit == "1":
            hamming_weight += 1
    return hamming_weight

input1 = 11
input2 = 128
input3 = 4294967293

print(hammingWeight(input3))
