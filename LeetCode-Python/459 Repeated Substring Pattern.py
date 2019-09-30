"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
    Input: "abab"
    Output: True
    Explanation: It's the substring "ab" twice.

Example 2:
    Input: "aba"
    Output: False

Example 3:
    Input: "abcabcabcabc"
    Output: True
    Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

def repeatedSubstringPattern(s: str) -> bool:
    can_be_construced = False
    l_s = len(s)
    for i in range(0, l_s // 2 + 1):

        if l_s % (i + 1) == 0:

            substring = s[:i + 1]
            l_sub_s = len(substring)
            index = l_sub_s

            while index <= l_s - l_sub_s:
                if s[index:index + l_sub_s] != substring:
                    break

                if index == l_s - l_sub_s:
                    can_be_construced = True
                    break
                else:
                    index += l_sub_s
    return can_be_construced

input1 = "abab"
input2 = "aba"
input3 = "abcabcabcabc"
input4 = "a"

print(repeatedSubstringPattern(input4))
