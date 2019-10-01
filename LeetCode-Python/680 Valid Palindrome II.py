"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
    Input: "aba"
    Output: True

Example 2:
    Input: "abca"
    Output: True
    Explanation: You could delete the character 'c'.

Note:
    The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

def validPalindrome(s: str) -> bool:
    # check if the string is a palindrome, if not, record the susepectable position
    s = list(s)
    is_palindrome = True
    susepectable_index = 0
    for i in range(len(s) // 2):
        if s[i] != s[-1-i]:
            is_palindrome = False
            susepectable_index = i
            break
    if is_palindrome:
        return True

    # delete the left susepectable char in string, check if it is a palindrome
    is_palindrome = True
    copy_1 = list(s)
    del copy_1[susepectable_index]
    for i in range(len(copy_1) // 2):
        if copy_1[i] != copy_1[-1-i]:
            is_palindrome = False
            break
    if is_palindrome:
        return True

    # delete the right susepectable char in string, check if it is a palindrome
    is_palindrome = True
    copy_2 = list(s)
    del copy_2[-1-susepectable_index]
    for i in range(len(copy_2) // 2):
        if copy_2[i] != copy_2[-1-i]:
            is_palindrome = False
            break
    if is_palindrome:
        return True
    else:
        return False


input1 = "aba"
input2 = "abca"
input3 = "abbca"
input4 = "abbbab"
input5 = "abaaabe"

print(validPalindrome(input5))
