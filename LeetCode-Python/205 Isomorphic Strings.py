"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:
    Input: s = "egg", t = "add"
    Output: true

Example 2:
    Input: s = "foo", t = "bar"
    Output: false

Example 3:
    Input: s = "paper", t = "title"
    Output: true

Note:
    You may assume both s and t have the same length.
"""

def isIsomorphic(s, t):
    # find the unique chars in s and record their position in a list
    s_freq = dict()
    for i in range(0, len(s)):
        if s[i] not in s_freq:
            s_freq[s[i]] = [i]
        else:
            s_freq[s[i]].append(i)
    # get the values of the dict (which are the positions of each char in s) and sort it
    s_freq = sorted(s_freq.values())

    # find the unique chars in t and record their position in a list
    t_freq = dict()
    for i in range(0, len(t)):
        if t[i] not in t_freq:
            t_freq[t[i]] = [i]
        else:
            t_freq[t[i]].append(i)
    t_freq = sorted(t_freq.values())

    # check if these two list are equal
    if s_freq == t_freq:
        return True
    else:
        return False

s1 = "egg"
t1 = "add"

s2 = "foo"
t2 = "bar"

s3 = "paper"
t3 = "title"

print(isIsomorphic("ab", "ca"))
