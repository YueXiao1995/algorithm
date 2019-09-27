"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
    Input: "A man, a plan, a canal: Panama"
    Output: true

Example 2:
    Input: "race a car"
    Output: false
"""
import string

def isPalindrome(s: str) -> bool:
    # remove the blank space and punctuations, and lowercase the string
    translator = str.maketrans('', '', string.punctuation)
    s = s.translate(translator).replace(" ", "").lower()
    # the number of pairs need be check
    l = len(s) // 2
    # iterate over the l to find unmatch pairs
    for i in range(l):
        if s[i] != s[-1 - i]:
            return False
    # if not found, return True
    return True

input1 = "A man, a plan, a canal: Panama"
input2 = "race a car"

print(isPalindrome(input1))
