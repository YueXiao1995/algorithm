"""
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: s = "ababccc"
    Output: 5
    Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

Example 2:
    Input: s = "aba"
    Output: 2
    Explanation: One way to split maximally is ['a', 'ba'].

Example 3:
    Input: s = "aa"
    Output: 1
    Explanation: It is impossible to split the string any further.

Constraints:
    1 <= s.length <= 16
    s contains only lower case English letters.
"""


def maxUniqueSplit(s):
    unique_substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            unique_substrings.add(s[i:j])
    sorted_unique_substrings = list(unique_substrings)
    sorted_unique_substrings = sorted(sorted_unique_substrings, key=len)
    #print(unique_substrings)
    #print(len(unique_substrings))
    #print(sorted_unique_substrings)
    substrings_list = [s]
    def getremains(unique_s, s):
        if unique_s == s:
            return []
        for i in range(len(s) - len(unique_s) + 1):
            if s[i: i + len(unique_s)] == unique_s:
                if i == 0:
                    return [s[i + len(unique_s):]]
                if i == len(s) - len(unique_s):
                    return [s[: i]]
                else:
                    return [s[: i], s[i + len(unique_s):]]
    while True:
        is_find = False
        for unique_s in sorted_unique_substrings:
            is_match = False
            match_s = None
            new_s_set = unique_substrings.copy()
            new_s_set.remove(unique_s)
            #print(new_s_set)
            for substring in substrings_list:
                if unique_s in substring:
                    temp_s_list = getremains(unique_s, substring)
                    is_all_valid = True
                    #print(temp_s_list)
                    if len(temp_s_list) == 2 and temp_s_list[0] == temp_s_list[1]:
                        is_all_valid = False

                    for temp_s in temp_s_list:
                        if temp_s not in new_s_set or temp_s in substrings_list:
                            is_all_valid = False
                            break
                    if is_all_valid == True:
                        is_match = True
                        match_s = substring
                        break
                    else:
                        pass
                else:
                    pass
            if is_match:
                unique_substrings.remove(unique_s)
                sorted_unique_substrings.remove(unique_s)
                substrings_list.append(unique_s)
                substrings_list.extend(getremains(unique_s, match_s))
                substrings_list.remove(match_s)
                is_find = True
                break

        if not is_find:
            break
    print(substrings_list)
    return len(substrings_list)


s = "ababccc"
#print(maxUniqueSplit(s))

s = "aba"
#print(maxUniqueSplit(s))


s = "aa"
#print(maxUniqueSplit(s))

s = "fcmfacp"
print(maxUniqueSplit(s))

def getremains(unique_s, s):
    if unique_s == s:
        return []
    for i in range(len(s) - len(unique_s) + 1):
        if s[i: i + len(unique_s)] == unique_s:
            if i == 0:
                return [s[i + len(unique_s):]]
            if i == len(s) - len(unique_s):
                return [s[: i]]
            else:
                return [s[: i], s[i + len(unique_s):]]

print(getremains('bb', 'caabbb'))
