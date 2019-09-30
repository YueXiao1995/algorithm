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
    l_s = len(s)
    # iterate over all of the substring with length smaller than or equal to half of the original string s
    for i in range(0, l_s // 2 + 1):
        # check if the length of substring is a factor of the length of s
        if l_s % (i + 1) == 0:
            # get the target substring
            substring = s[:i + 1]
            l_sub_s = i + 1
            index = l_sub_s
            # iterate over the substrings in s with length equal to the target substring
            while index <= l_s - l_sub_s:
                # check if the substring equal to the target substring
                if s[index:index + l_sub_s] != substring:
                    break
                # check if is the last substring of s have been passed
                if index == l_s - l_sub_s:
                    return True
                else:
                    # move the index froward in s
                    index += l_sub_s
    return False

input1 = "abab"
input2 = "aba"
input3 = "abcabcabcabc"
input4 = "a"

print(repeatedSubstringPattern(input4))
