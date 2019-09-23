"""
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.

Example 1:
    Input: "abbxxxxzzy"
    Output: [[3,6]]
    Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.

Example 2:
    Input: "abc"
    Output: []
    Explanation: We have "a","b" and "c" but no large group.

Example 3:
    Input: "abcdddeeeeaabbbcd"
    Output: [[3,5],[6,9],[12,14]]

Note:  1 <= S.length <= 1000
"""

def largeGroupPositions(S):
    start = None
    repeat_time = 0
    last_char = None
    large_group_list = list()
    l = len(S)
    S = list(S)
    for i in range(0, l):
        if start == None:
            start = i
            repeat_time += 1
            last_char = S[i]
        else:
            if S[i] == last_char:
                repeat_time += 1
            else:
                if repeat_time >= 3:
                    large_group_list.append([start, i - 1])
                start = i
                repeat_time = 1
                last_char = S[i]

    if start != l - 1:
        if repeat_time >= 3:
            large_group_list.append([start, l - 1])

    return large_group_list

input1 = "abbxxxxzzy"
input2 = "abc"
input3 = "abcdddeeeeaabbbcd"
input4 = "aaa"
input5 = "babaaaabbb"

print(largeGroupPositions(input5))
