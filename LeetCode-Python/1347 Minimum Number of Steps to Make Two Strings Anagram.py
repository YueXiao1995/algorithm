"""
Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example 1:
    Input: s = "bab", t = "aba"
    Output: 1
    Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:
    Input: s = "leetcode", t = "practice"
    Output: 5
    Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example 3:
    Input: s = "anagram", t = "mangaar"
    Output: 0
    Explanation: "anagram" and "mangaar" are anagrams.

Example 4:
    Input: s = "xxyyzz", t = "xxyyzz"
    Output: 0

Example 5:
    Input: s = "friend", t = "family"
    Output: 4

Constraints:
    1 <= s.length <= 50000
    s.length == t.length
    s and t contain lower-case English letters only.
"""

def minSteps(s, t):
    s_freq = dict()
    for i in range(len(s)):
        if s[i] not in s_freq:
            s_freq[s[i]] = 1
        else:
            s_freq[s[i]] += 1

    for i in range(len(t)):
        if t[i] in s_freq:
            s_freq[t[i]] -= 1

    min_num_of_steps = 0
    for char in s_freq:
        if s_freq[char] > 0:
            min_num_of_steps += s_freq[char]
    return min_num_of_steps

s = "bab"
t = "aba"
print(minSteps(s, t))


s = "leetcode"
t = "practice"
print(minSteps(s, t))

s = "anagram"
t = "mangaar"
print(minSteps(s, t))

s = "xxyyzz"
t = "xxyyzz"
print(minSteps(s, t))

s = "friend"
t = "family"
print(minSteps(s, t))
