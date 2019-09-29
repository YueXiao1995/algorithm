"""
Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
    Input: "aba", "cdc"
    Output: 3
    Explanation: The longest uncommon subsequence is "aba" (or "cdc"),
    because "aba" is a subsequence of "aba",
    but not a subsequence of any other strings in the group of two strings.

Note:
    Both strings' lengths will not exceed 100.
    Only letters from a ~ z will appear in input strings.
"""

def findLUSlength(a: str, b: str) -> int:
    if len(a) >= len(b):
        long_string = a
        short_string = b
    else:
        long_string = b
        short_string = a
    print(long_string)
    print(short_string)

    max_length = 0
    for i in range(len(short_string)):
        while True:
            isFound = False
            sub_short_string = short_string[i:i + max_length]
            print([sub_short_string])
            match_index = 0
            for j in range(i, len(long_string)):
                if long_string[j] == sub_short_string[match_index]:
                    match_index += 1
                    if match_index == max_length:
                        break


            print(max_length)
            if isFound:
                max_length += 1
            else:
                max_length -= 1
                break

    return 0

a1 = "aba"
b1 = "cdc"

a2 = "aaaaaasdf"
b2 = "absfcaaa"

print(findLUSlength(a2, b2))
