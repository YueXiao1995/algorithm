"""
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

Example 1:
    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"

Example 2:
    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"

Example 3:
    Input: str1 = "LEET", str2 = "CODE"
    Output: ""

Note:
    1 <= str1.length <= 1000
    1 <= str2.length <= 1000
    str1[i] and str2[i] are English uppercase letters.
"""

def gcdOfStrings(str1: str, str2: str) -> str:
    # find the factors of str1
    factor_set_1 = set()
    l_s = len(str1)
    # iterate over all of the substring of str1 include itself
    for i in range(0, l_s + 1):
        # check if the length of substring is a factor of the length of str1
        if l_s % (i + 1) == 0:
            # get the target substring
            substring = str1[:i + 1]
            l_sub_s = i + 1
            index = 0
            # iterate over the substrings in s with length equal to the target substring
            while index <= l_s - l_sub_s:
                # check if the substring equal to the target substring
                if str1[index:index + l_sub_s] != substring:
                    break
                # check if is the last substring of s have been passed
                if index == l_s - l_sub_s:
                    factor_set_1.add(substring)
                    break
                else:
                    # move the index froward in s
                    index += l_sub_s


    # find the factors of the str2
    factor_set_2 = set()
    l_s = len(str2)
    for i in range(0, l_s + 1):
        if l_s % (i + 1) == 0:
            substring = str2[:i + 1]
            l_sub_s = i + 1
            index = 0
            while index <= l_s - l_sub_s:
                if str2[index:index + l_sub_s] != substring:
                    break
                if index == l_s - l_sub_s:
                    factor_set_2.add(substring)
                    break
                else:
                    index += l_sub_s

    # find the common factors
    common_factors = factor_set_1 & factor_set_2
    # if common factor is not found, return an empty stirng ""
    if len(common_factors) == 0:
        return ""
    # else find the longest factor and return it
    else:
        largest_string = None
        # iterate over the common factors set, find the longest factor
        for factor in common_factors:
            if largest_string == None:
                largest_string = factor
            else:
                if len(factor) > len(largest_string):
                    largest_string = factor
        return largest_string

str1 = "ABCABC"
str2 = "ABC"
str3 = "ABABAB"
str4 = "ABAB"
str5 = "LEET"
str6 = "CODE"
print(gcdOfStrings(str1, str2))
