"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
    Input: "Hello World"
    Output: 5
"""

def lengthOfLastWord(s: str) -> int:
    # split the string s by " "
    s = s.split(" ")
    # iterate the s list to remove ""
    l = len(s)
    i = 0
    while i < l:
        if s[i] == "":
            del s[i]
            l -= 1
        else:
            i += 1
    # if the list s is empty after delete all of the "", return 0
    if len(s) == 0:
        return 0
    # else return the length of last element in list
    else:
        return len(s[-1])

input1 = "Hello World"
input2 = ""
input3 = "a "
input4 = " aa "
input5 = "b   a    "

print(lengthOfLastWord(input5))
