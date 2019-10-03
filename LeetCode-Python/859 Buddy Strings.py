"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:
    Input: A = "ab", B = "ba"
    Output: true

Example 2:
    Input: A = "ab", B = "ab"
    Output: false

Example 3:
    Input: A = "aa", B = "aa"
    Output: true

Example 4:
    Input: A = "aaaaaaabc", B = "aaaaaaacb"
    Output: true

Example 5:
    Input: A = "", B = "aa"
    Output: false

Note:
    0 <= A.length <= 20000
    0 <= B.length <= 20000
    A and B consist only of lowercase letters.
"""

def buddyStrings(A: str, B: str) -> bool:
    l_a = len(A)
    l_b = len(B)
    # if the length of these two strings are not equal, they definitely are not buddy strings
    if l_a != l_b:
        return False
    else:
        # if the length of them are 0, they have nothing to swap, so they are not buddy strings
        if l_a == 0:
            return False

    # check if the A and B are equal,
    if A == B:
        # if any char in A appears more then one times, this char is swappable， so return True
        chars = set()
        for char in A:
            if char not in chars:
                chars.add(char)
            else:
                return True
        # if not find, return False
        return False
    else:
        # count and record the number of unmatch positions
        unequal_position = list()
        for i in range(l_a):
            if A[i] != B[i]:
                unequal_position.append(i)
        # check if number of unmatch positions is 2
        if len(unequal_position) == 2:
            # swap these chars
            B = list(B)
            temp_char = B[unequal_position[0]]
            B[unequal_position[0]] = B[unequal_position[1]]
            B[unequal_position[1]] = temp_char
            B = ("").join(B)
            # check if the A and B are equal after B swap
            if A != B:
                return False
            else:
                return True
        # if the number of unmatch position is not 2, return False
        else:
            return False

A1 = "ab"
B1 = "ba"

A2 = "ab"
B2 = "ab"

A3 = "aa"
B3 = "aa"

A4 = "aaaaaaabc"
B4 = "aaaaaaacb"

A5 = ""
B5 = "aa"

A6 = ""
B6 = ""

A7 = "abab"
B7 = "abab"

print(buddyStrings(A7, B7))
