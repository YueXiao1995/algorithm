"""
A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

Example 1:
    Input: s = "xyzzaz"
    Output: 1
    Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
    The only good substring of length 3 is "xyz".

Example 2:
    Input: s = "aababcabc"
    Output: 4
    Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
    The good substrings are "abc", "bca", "cab", and "abc".

Constraints:
    1 <= s.length <= 100
    s​​​​​​ consists of lowercase English letters.
"""

def countGoodSubstrings(s):
    good_substrings = list()
    substr = []
    for char in list(s):
        if char not in substr:
            substr.append(char)
        else:
            substr.append(char)
            for i in range(len(substr)):
                if substr[i] == char:
                    substr = list(substr[i+1:])
                    break
        if len(substr) > 3:
            substr = list(substr[1:])
        if len(substr) == 3:
            good_substrings.append(('').join(substr))
    return len(good_substrings)

s = "xyzzaz"
print(countGoodSubstrings(s))

s = "aababcabc"
print(countGoodSubstrings(s))

s = "owuxoelszb"
print(countGoodSubstrings(s))
