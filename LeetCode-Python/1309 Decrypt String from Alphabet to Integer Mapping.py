"""
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

Example 1:
    Input: s = "10#11#12"
    Output: "jkab"
    Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:
    Input: s = "1326#"
    Output: "acz"

Example 3:
    Input: s = "25#"
    Output: "y"

Example 4:
    Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    Output: "abcdefghijklmnopqrstuvwxyz"

Constraints:
    1 <= s.length <= 1000
    s[i] only contains digits letters ('0'-'9') and '#' letter.
    s will be valid string such that mapping is always possible.
"""

import string
def freqAlphabets(s):
    characters = list(string.ascii_lowercase)

    decrypt = list(range(1, 27))
    for i in range(1, 27):
        if i < 10:
            decrypt[i - 1] = str(decrypt[i - 1])
        else:
            decrypt[i - 1] = str(decrypt[i - 1]) + "#"

    convert_dict = dict()
    for i in range(26):
        convert_dict[decrypt[i]] = characters[i]

    result = ""
    i = len(s) - 1
    while i >= 0:
        if s[i] == "#":
            result = convert_dict[s[i-2 :i+1]] + result
            i -= 3
        else:
            result = convert_dict[s[i]] + result
            i -= 1
    return result

s1 = "10#11#12"
s2 = "1326#"
s3 = "25#"
s4 = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"

print(freqAlphabets(s4))
