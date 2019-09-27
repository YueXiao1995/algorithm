"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
    Input: haystack = "hello", needle = "ll"
    Output: 2

Example 2:
    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

Clarification:
    What should we return when needle is an empty string? This is a great question to ask during an interview.
    For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""

# Time Limit Exceeded
"""
def strStr(haystack, needle):
    l_neddle = len(needle)
    if l_neddle == 0:
        return 0
    l_haystack = len(haystack)

    for i in range(l_haystack):
        match_index = 0
        for j in range(i, l_haystack):
            print(match_index)
            if haystack[j] == needle[match_index]:
                if match_index == l_neddle - 1:
                    return i
                match_index += 1
            else:
                break
    return -1
"""
def strStr(haystack, needle):
    # if the needle is a empty string, return 0
    l_needle = len(needle)
    if l_needle == 0:
        return 0
    l_haystack = len(haystack)
    # compare the length of the haystack and the needle
    if l_haystack > l_needle:
        # iterate over the haystack to find the match substring
        for i in range(l_needle - 1, l_haystack):
            # if the string are equal, return the index of the start point
            if haystack[i-l_needle+1:i+1] == needle:
                return i - l_needle + 1
    # if the length of haystack and needle are equal, check if these two string are equal
    elif l_haystack == l_needle:
        if haystack == needle:
            return 0
    # if didn't find any match substring in haystack, return -1
    return -1

haystack1 = "hello"
needle1 = "ll"
haystack2 = "aaaaa"
needle2 = "bba"
haystack3 = "acdsdfa"
needle3 = ""
haystack4 = "mississippi"
needle4 = "issip"
haystack5 = "a"
needle5 = "a"
haystack6 = "mississippi"
needle6 = "pi"

print(strStr(haystack6, needle6))
