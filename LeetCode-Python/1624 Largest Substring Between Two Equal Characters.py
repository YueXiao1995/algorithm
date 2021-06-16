"""
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: s = "aa"
    Output: 0
    Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:
    Input: s = "abca"
    Output: 2
    Explanation: The optimal substring here is "bc".

Example 3:
    Input: s = "cbzxy"
    Output: -1
    Explanation: There are no characters that appear twice in s.

Example 4:
    Input: s = "cabbac"
    Output: 4
    Explanation: The optimal substring here is "abba". Other non-optimal substrings include "bb" and "".

Constraints:
    1 <= s.length <= 300
    s contains only lowercase English letters.
"""

def maxLengthBetweenEqualCharacters(s):
    character_position = dict()
    for i in range(len(s)):
        char = s[i]
        if char not in character_position:
            character_position[char] = [i]
        else:
            character_position[char].append(i)
    print(character_position)

    max_length = -1
    for char in character_position:
        position_list = character_position[char]
        if len(position_list) > 1:
            l = position_list[-1] - position_list[0] - 1
            max_length = max(max_length, l)
    return max_length

s = "aa"
print(maxLengthBetweenEqualCharacters(s))

s = "abca"
print(maxLengthBetweenEqualCharacters(s))

s = "cbzxy"
print(maxLengthBetweenEqualCharacters(s))

s = "cabbac"
print(maxLengthBetweenEqualCharacters(s))
