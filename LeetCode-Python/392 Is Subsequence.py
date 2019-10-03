"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
    s = "abc", t = "ahbgdc"
    Return true.

Example 2:
    s = "axc", t = "ahbgdc"
    Return false.

Follow up:
    If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
    Special thanks to @pbrother for adding this problem and creating all test cases.
"""

def isSubsequence(s: str, t: str) -> bool:
    # if s is "", it is the subsequence of every stings
    if len(s) == 0:
        return True
    # the next position to check in s
    index = 0
    # iterate over the t
    for char in t:
        # check if this char can be used to form the subsequence s
        if char == s[index]:
            # move the index forward
            index += 1
            # if index reach the end of s, return True
            if index == len(s):
                return True
    return False

s1 = "abc"
t1 = "ahbgdc"

s2 = "axc"
t2 = "ahbgdc"

s3 = ""
t3 = "ahbgdc"
print(isSubsequence(s2, t2))
