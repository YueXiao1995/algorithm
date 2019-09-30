"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:
    Input: "Hello"
    Output: "hello"

Example 2:
    Input: "here"
    Output: "here"

Example 3:
    Input: "LOVELY"
    Output: "lovely"
"""
import string

def toLowerCase(str: str) -> str:
    str = list(str)
    for i in range(len(str)):
        str[i] = str[i].lower()
    return ("").join(str)

input1 = "Hello"
input2 = "here"
input3 = "LOVELY"

print(toLowerCase(input1))

