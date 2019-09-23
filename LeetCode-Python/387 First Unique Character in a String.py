"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.

Note:
    You may assume the string contain only lowercase letters.
"""

def firstUniqChar(s):
    # count and freq of each nums in dict and store their index
    freq = dict()
    for i in range(0, len(s)):
        if s[i] in freq:
            freq[s[i]].append(i)
        else:
            freq[s[i]] = [i]
    # find the index of the first unique char
    first_unique_char_index = None
    for num in freq:
        # check the length of the index list of a num is 1
        if len(freq[num]) == 1:
            if first_unique_char_index != None:
                # if the index is smaller than previous minimum index, update the index of the first unique num
                if freq[num][0] < first_unique_char_index:
                    first_unique_char_index = freq[num][0]
            else:
                first_unique_char_index = freq[num][0]
    # check if there is unique char in the s
    if first_unique_char_index == None:
        return -1
    else:
        return first_unique_char_index

s1 = "leetcode"
s2 = "loveleetcode"
print(firstUniqChar(s1))
