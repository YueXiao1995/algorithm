"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false
    Note:
    You may assume the string contains only lowercase alphabets.

Follow up:
    What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

# Time Limit Exceeded
"""
def isAnagram(s, t):
    s = list(s)
    t = list(t)
    l_s = len(s)
    while l_s > 0:
        is_found = False
        for char in t:
            if char == s[0]:
                is_found = True
                t.remove(char)
                break
        if is_found:
            del s[0]
            l_s -= 1
        else:
            return False
    if len(t) == 0:
        return True
    else:
        return False
"""

def isAnagram(s, t):
    # find the unique chars in each list and sore there freq into a dict
    s_freq = dict()
    for char in s:
        if char not in s_freq:
            s_freq[char] = 1
        else:
            s_freq[char] += 1
    print(s_freq)
    t_freq = dict()
    for char in t:
        if char not in t_freq:
            t_freq[char] = 1
        else:
            t_freq[char] += 1
    print(t_freq)

    # compare if these two list are the same
    if t_freq != s_freq:
        return False
    else:
        return True

s1 = "anagram"
t1 = "nagaram"

s2 = "rat"
t2 = "car"

print(isAnagram(s1, t1))
