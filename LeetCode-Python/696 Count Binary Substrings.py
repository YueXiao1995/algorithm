"""
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
    Input: "00110011"
    Output: 6
    Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
    Notice that some of these substrings repeat and are counted the number of times they occur.
    Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
    Input: "10101"
    Output: 4
    Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Note:
    s.length will be between 1 and 50,000.
    s will only consist of "0" or "1" characters.
"""

def countBinarySubstrings(s: str) -> int:
    num_of_valid_substring = 0
    l_s = len(s)
    i = 0
    while i < l_s - 1:
        if s[i] == s[i + 1]:
            i += 1
        else:
            left = s[i]
            right = s[i + 1]
            left_index = i
            right_index = i + 1
            while left_index >= 0 and right_index < l_s:
                if s[left_index] == left and s[right_index] == right:
                    num_of_valid_substring += 1
                    left_index -= 1
                    right_index += 1
                else:
                    break
            i = right_index-1
    return num_of_valid_substring

input1 = "00110011"
input2 = "10101"
input3 = "00110"

print(countBinarySubstrings(input3))
