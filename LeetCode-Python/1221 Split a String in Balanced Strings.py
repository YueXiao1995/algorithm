"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

Example 1:
    Input: s = "RLRRLLRLRL"
    Output: 4
    Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:
    Input: s = "RLLLLRRRLR"
    Output: 3
    Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:
    Input: s = "LLLLRRRR"
    Output: 1
    Explanation: s can be split into "LLLLRRRR".

Constraints:
    1 <= s.length <= 1000
    s[i] = 'L' or 'R'
"""

def balancedStringSplit(s):
    num_of_balanced_strings = 0
    num_of_L = 0
    num_of_R = 0
    # iterate the string and count the number of the "L" and "R"
    for char in s:
        if char == "R":
            num_of_R += 1
        else:
            num_of_L += 1
        # when the number of R and L are equal, means we can split a balanced string from the original string
        if num_of_R == num_of_L:
            num_of_balanced_strings += 1
    return num_of_balanced_strings

s1 = "RLRRLLRLRL"
s2 = "RLLLLRRRLR"
s3 = "LLLLRRRR"
s4 = "RLLRRRLLLR"

print(balancedStringSplit(s4))

