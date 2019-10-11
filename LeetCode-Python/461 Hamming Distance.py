"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
    0 ≤ x, y < 2^31.

Example:
    Input: x = 1, y = 4

    Output: 2

    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑

    The above arrows point to positions where the corresponding bits are different.
"""
def hammingDistance(x, y):
    # convert x and y to binary string
    x = str(bin(x))[2:]
    y = str(bin(y))[2:]
    # figure out which one is short and which one is longer
    if len(x) > len(y):
        longer = x
        shorter = y
    else:
        longer = y
        shorter = x
    # calculate the hamming distance
    hamming_distance = 0
    for i in range(len(longer)):
        if i < len(shorter):
            if longer[-1 - i] != shorter[-1 - i]:
                hamming_distance += 1
        else:
            if longer[-1 - i] == "1":
                hamming_distance += 1
    return hamming_distance

print(hammingDistance(1, 4))
