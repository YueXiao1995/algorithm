"""
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
    Input:
    bits = [1, 0, 0]
    Output: True
    Explanation:
    The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Example 2:
    Input:
    bits = [1, 1, 1, 0]
    Output: False
    Explanation:
    The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

Note:
    1 <= len(bits) <= 1000.
    bits[i] is always 0 or 1.
"""

def isOneBitCharacter(bits):
    l = len(bits)
    if l == 1:
        if bits[0] == 0:
            return True
        else:
            return False
    else:
        if bits[- 1] == 1:
            return False
        else:
            num_of_1 = 0
            for i in reversed(range(0, l - 1)):
                if bits[i] == 1:
                    num_of_1 += 1
                else:
                    break
            if num_of_1 % 2 == 0:
                return True
            else:
                return False


input = [1, 0, 0]
input2 = [1, 1, 1, 0]
print(isOneBitCharacter(input2))
