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
    # iterate over the string, find all of the boundary of the 0 and 1
    while i < l_s - 1:
        # if equal, move forward
        if s[i] == s[i + 1]:
            i += 1
        # else, means this is a boundary, use this digit as the center to form a substring
        # expand the substring on both side
        else:
            left = s[i]
            right = s[i + 1]
            left_index = i
            right_index = i + 1
            # check if the index is out of range
            while left_index >= 0 and right_index < l_s:
                # check if the substring is valid
                if s[left_index] == left and s[right_index] == right:
                    num_of_valid_substring += 1
                    left_index -= 1
                    right_index += 1
                else:
                    break
            # move forward
            i = right_index-1
    return num_of_valid_substring

# little bit faster
def countBinarySubstrings2(s: str) -> int:
    # find and record the position of the boundary between 0 and 1
    boundary_list = list()
    # add the start point
    boundary_list.append(-1)
    l_s = len(s)
    for i in range(l_s - 1):
        if s[i] != s[i+1]:
            boundary_list.append(i)
    # add the end point
    boundary_list.append(l_s -1)

    # iterate over the boundary list, to count the number of valid string
    num_of_valid_string = 0
    for i in range(1, len(boundary_list) - 1):
        num_of_valid_string += min((boundary_list[i] - boundary_list[i - 1]),(boundary_list[i + 1] - boundary_list[i]))

    return num_of_valid_string



input1 = "00110011"
input2 = "10101"
input3 = "00110"

print(countBinarySubstrings2(input1))
