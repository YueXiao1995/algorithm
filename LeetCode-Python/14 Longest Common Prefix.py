"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:
    Input: ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
"""


def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    prefix = ""
    min_l = len(strs[0])
    min_str = strs[0]
    for str in strs:
        if len(str) < min_l:
            min_l = len(str)
            min_str = str

    for i in range(0, min_l):
        temp_prefix = min_str[i]
        is_temp_prefix_real = True
        for str in strs:
            if str[i] != temp_prefix:
                is_temp_prefix_real = False
                break
        if is_temp_prefix_real:
            prefix += temp_prefix
        else:
            break
    return prefix


input = ["flower", "flow", "flight"]
print(longestCommonPrefix(input))

"""
Runtime: 20 ms, faster than 73.15% of Python online submissions for Longest Common Prefix.
Memory Usage: 11.7 MB, less than 98.75% of Python online submissions for Longest Common Prefix.

"""
