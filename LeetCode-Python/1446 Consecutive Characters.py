"""
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

Example 1:
    Input: s = "leetcode"
    Output: 2
    Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
    Input: s = "abbcccddddeeeeedcba"
    Output: 5
    Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Example 3:
    Input: s = "triplepillooooow"
    Output: 5

Example 4:
    Input: s = "hooraaaaaaaaaaay"
    Output: 11

Example 5:
    Input: s = "tourist"
    Output: 1

Constraints:
    1 <= s.length <= 500
    s contains only lowercase English letters.
"""

def maxPower(s):
    max_l = 1
    temp_l = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            temp_l += 1
        else:
            max_l = max(max_l, temp_l)
            temp_l = 1
            current_char = s[i]
    max_l = max(max_l, temp_l)
    return max_l

s = "leetcode"
print(maxPower(s))

s = "abbcccddddeeeeedcba"
print(maxPower(s))

s = "triplepillooooow"
print(maxPower(s))

s = "hooraaaaaaaaaaay"
print(maxPower(s))

s = "tourist"
print(maxPower(s))
