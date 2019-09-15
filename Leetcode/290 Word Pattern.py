"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
    Input: pattern = "abba", str = "dog cat cat dog"
    Output: true

Example 2:
    Input: pattern = "abba", str = "dog cat cat fish"
    Output: false

Example 3:
    Input: pattern = "aaaa", str = "dog cat cat dog"
    Output: false

Example 4:
    Input: pattern = "abba", str = "dog dog dog dog"
    Output: false

Notes:
    You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""

def wordPattern(pattern, str):
    # iterate the pattern list to recode the position of each char in list
    p_dict = dict()
    for i in range(0, len(pattern)):
        if pattern[i] not in p_dict:
            p_dict[pattern[i]] = [i]
        else:
            p_dict[pattern[i]].append(i)
    p_list = sorted(p_dict.values())

    # split the string into a list
    str = str.split(" ")

    # iterate the str list to recode the position of each char in list
    s_dict = dict()
    for i in range(0, len(str)):
        if str[i] not in s_dict:
            s_dict[str[i]] = [i]
        else:
            s_dict[str[i]].append(i)
    s_list = sorted(s_dict.values())

    # check if these two list are equal
    if p_list == s_list:
        return True
    else:
        return False

pattern1 = "abba"
str1 = "dog cat cat dog"

pattern2 = "abba"
str2 = "dog cat cat fish"

pattern3 = "aaaa"
str3 = "dog cat cat dog"

pattern4 = "abba"
str4 = "dog dog dog dog"

print(wordPattern(pattern4, str4))
