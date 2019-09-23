"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:
    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:
    Input: ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
"""

def reverseString(s):
    l = len(s)
    if l % 2 == 0:
        l = int(l / 2)
    else:
        l = int(round(l / 2 - 0.5))

    for i in range(0, l):
        temp = s[i]
        s[i] = s[-i-1]
        s[-i-1] = temp

    return s

input = ["h","e","l","l","o"]
print(reverseString(input))
