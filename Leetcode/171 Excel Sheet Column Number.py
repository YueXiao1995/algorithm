"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

Example 1:
    Input: "A"
    Output: 1

Example 2:
    Input: "AB"
    Output: 28

Example 3:
    Input: "ZY"
    Output: 701
"""

def titleToNumber(s):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # store the index of each char into a dict
    char_index = dict()
    for i in range(26):
        if alphabet[i] not in char_index:
            char_index[alphabet[i]] = i + 1
    # calculate the num
    num = 0
    time = 1
    for i in reversed(range(len(s))):
        num += char_index[s[i]] * time
        time *= 26
    return num


input1 = "A"
input2 = "AB"
input3 = "ZY"

print(titleToNumber(input3))
