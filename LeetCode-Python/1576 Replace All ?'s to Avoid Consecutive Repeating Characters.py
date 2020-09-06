"""
Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.



Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
Example 2:

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
Example 3:

Input: s = "j?qg??b"
Output: "jaqgacb"
Example 4:

Input: s = "??yw?ipkj?"
Output: "acywaipkja"


Constraints:

1 <= s.length <= 100

s contains only lower case English letters and '?'.


"""
import string
def modifyString(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == '?':
            if i == 0:
                left = None
                if len(s) > 1:
                    right = s[i + 1]
                else:
                    right = None
            elif i == len(s) - 1:
                left = s[i -1]
                right = None
            else:
                left = s[i - 1]
                right = s[i + 1]
            for c in list(string.ascii_lowercase):
                if c != left and c != right:
                    s[i] = c
                    break
    return ('').join(s)

s = "?zs"
print(modifyString(s))

s = "ubv?w"
print(modifyString(s))

s = "j?qg??b"
print(modifyString(s))

s = "??yw?ipkj?"
print(modifyString(s))

s = "?"
print(modifyString(s))
