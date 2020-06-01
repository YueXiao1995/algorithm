"""
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：
    输入: s1 = "abc", s2 = "bca"
    输出: true

示例 2：
    输入: s1 = "abc", s2 = "bad"
    输出: false

说明：
    0 <= len(s1) <= 100
    0 <= len(s2) <= 100
"""

def CheckPermutation(s1, s2):
    s1_char_freq = dict()
    for char in s1:
        if char not in s1_char_freq:
            s1_char_freq[char] = 1
        else:
            s1_char_freq[char] += 1

    s2_char_freq = dict()
    for char in s2:
        if char not in s2_char_freq:
            s2_char_freq[char] = 1
        else:
            s2_char_freq[char] += 1
    if s1_char_freq == s2_char_freq:
        return True
    else:
        return False


def CheckPermutation2(s1, s2):
    s1_char_freq = dict()
    for char in s1:
        if char not in s1_char_freq:
            s1_char_freq[char] = 1
        else:
            s1_char_freq[char] += 1
    for char in s2:
        if char not in s1_char_freq:
            return False
        else:
            s1_char_freq[char] -= 1
            if s1_char_freq[char] == 0:
                s1_char_freq.pop(char)
    return True

s1 = "abc"
s2 = "bca"
print(CheckPermutation2(s1, s2))

s1 = "abc"
s2 = "bad"
print(CheckPermutation2(s1, s2))
