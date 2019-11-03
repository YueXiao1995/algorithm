"""
You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

Example 1:
    Input: s1 = "xx", s2 = "yy"
    Output: 1
    Explanation:
    Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".

Example 2:
    Input: s1 = "xy", s2 = "yx"
    Output: 2
    Explanation:
    Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
    Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
    Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.

Example 3:
    Input: s1 = "xx", s2 = "xy"
    Output: -1

Example 4:
    Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
    Output: 4

Constraints:
    1 <= s1.length, s2.length <= 1000
    s1, s2 only contain 'x' or 'y'.
"""

def minimumSwap(s1, s2):
    num_of_x = s1.count("x") + s2.count("x")
    num_of_y = s2.count("y") + s2.count("y")
    if num_of_x % 2 != 0 or num_of_y % 2 != 0:
        return -1

    unmatch_list = list()
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if s1[i] == "x":
                unmatch_list.append(1)
            else:
                unmatch_list.append(2)
        else:
            unmatch_list.append(0)
    print(unmatch_list)

    unmatch_type1 = unmatch_list.count(1)
    unmatch_type2 = unmatch_list.count(2)

    if (unmatch_type1 + unmatch_type2) % 2 != 0:
        return -1

    if unmatch_type1 % 2 != unmatch_type2 % 2:
        return -1

    min_num_of_swapes = (unmatch_type1 // 2) + (unmatch_type2 // 2) + (unmatch_type1 % 2) * 2
    return min_num_of_swapes


s1 = "xx"
s2 = "yy"
print(minimumSwap(s1, s2))

s3 = "xy"
s4 = "yx"
print(minimumSwap(s3, s4))

s5 = "xx"
s6 = "xy"
print(minimumSwap(s5, s6))

s7 = "xxyyxyxyxx"
s8 = "xyyxyxxxyx"
print(minimumSwap(s7, s8))

