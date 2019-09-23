"""
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.



Example 1:
    Input: 22
    Output: 2
    Explanation:
    22 in binary is 0b10110.
    In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
    The first consecutive pair of 1's have distance 2.
    The second consecutive pair of 1's have distance 1.
    The answer is the largest of these two distances, which is 2.

Example 2:
    Input: 5
    Output: 2
    Explanation:
    5 in binary is 0b101.

Example 3:
    Input: 6
    Output: 1
    Explanation:
    6 in binary is 0b110.

Example 4:
    Input: 8
    Output: 0
    Explanation:
    8 in binary is 0b1000.
    There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.

Note:
    1 <= N <= 10^9
"""

def binaryGap(N):
    # convert the N to binary form
    binary_N = ""
    while N != 1:
        binary_N = str(N % 2) + binary_N
        N -= N % 2
        N //= 2
    binary_N = str(N) + binary_N

    # find the maximum distance between two consecutive pairs of 1's
    index1 = None
    index2 = None
    max_distance = 0
    for i in range(len(binary_N)):
        if binary_N[i] == '1':
            index2 = index1
            index1 = i
            if index2 != None:
                if i - index2 > max_distance:
                    max_distance = i - index2
    return max_distance

input1 = 22
input2 = 5
input3 = 6
input4 = 8

print(binaryGap(input4))
