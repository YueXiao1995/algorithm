"""
You are given an array A of strings.

Two strings S and T are special-equivalent if after any number of moves, S == T.

A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping S[i] with S[j].

Now, a group of special-equivalent strings from A is a non-empty subset S of A such that any string not in S is not special-equivalent with any string in S.

Return the number of groups of special-equivalent strings from A.

Example 1:
    Input: ["a","b","c","a","c","c"]
    Output: 3
    Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]

Example 2:
    Input: ["aa","bb","ab","ba"]
    Output: 4
    Explanation: 4 groups ["aa"], ["bb"], ["ab"], ["ba"]

Example 3:
    Input: ["abc","acb","bac","bca","cab","cba"]
    Output: 3
    Explanation: 3 groups ["abc","cba"], ["acb","bca"], ["bac","cab"]

Example 4:
    Input: ["abcd","cdab","adcb","cbad"]
    Output: 1
    Explanation: 1 group ["abcd","cdab","adcb","cbad"]

Note:
    1 <= A.length <= 1000
    1 <= A[i].length <= 20
    All A[i] have the same length.
    All A[i] consist of only lowercase letters.
"""

# Time Limit Exceeded
def numSpecialEquivGroups(A):
    l = len(A)
    i = 0
    groups = list()
    while i < l:
        new_group = [A[i]]
        j = i + 1
        while j < l:
            str1 = A[i]
            str2 = A[j]
            freq_1 = dict()
            freq_2 = dict()
            freq_3 = dict()
            freq_4 = dict()
            for k in range(len(str1)):
                if k % 2 == 0:
                    if str1[k] not in freq_1:
                        freq_1[str1[k]] = 1
                    else:
                        freq_1[str1[k]] += 1

                    if str2[k] not in freq_2:
                        freq_2[str2[k]] = 1
                    else:
                        freq_2[str2[k]] += 1
                else:
                    if str1[k] not in freq_3:
                        freq_3[str1[k]] = 1
                    else:
                        freq_3[str1[k]] += 1

                    if str2[k] not in freq_4:
                        freq_4[str2[k]] = 1
                    else:
                        freq_4[str2[k]] += 1
            if freq_1 == freq_2 and freq_3 == freq_4:
                new_group.append(A[j])
                del A[j]
                l -= 1
            else:
                j += 1
        groups.append(new_group)
        del A[i]
        l -= 1
    return len(groups)


def isSpecialEquivalent(str1, str2):
    freq_1 = dict()
    freq_2 = dict()
    freq_3 = dict()
    freq_4 = dict()
    for i in range(len(str1)):
        if i % 2 == 0:
            if str1[i] not in freq_1:
                freq_1[str1[i]] = 1
            else:
                freq_1[str1[i]] += 1

            if str2[i] not in freq_2:
                freq_2[str2[i]] = 1
            else:
                freq_2[str2[i]] += 1
        else:
            if str1[i] not in freq_3:
                freq_3[str1[i]] = 1
            else:
                freq_3[str1[i]] += 1

            if str2[i] not in freq_4:
                freq_4[str2[i]] = 1
            else:
                freq_4[str2[i]] += 1

    if freq_1 == freq_2 and freq_3 == freq_4:
        return True
    else:
        return False


def numSpecialEquivGroups2(A):
    l = len(A[0])
    # a set to store the different chars combinations (for each string, use its chars to generate a new string s = chars with odd index in order + chars with even index in order
    chars_of_strings = set()
    # iterate over the string in list
    for string in A:
        # use two lists to store the chars with odd and even index respectively
        even_index = list()
        odd_index = list()
        # iterate over the chars in a string
        for i in range(l):
            if i % 2 == 0:
                even_index.append(string[i])
            else:
                odd_index.append(string[i])
        # use the chars of a string to form a new string, and store it in to the set
        chars_of_strings.add(("").join(sorted(odd_index)) + ("").join(sorted(even_index)))
    return len(chars_of_strings)

input1 = ["a","b","c","a","c","c"]
input2 = ["aa","bb","ab","ba"]
input3 = ["abc","acb","bac","bca","cab","cba"]
input4 = ["abcd","cdab","adcb","cbad"]
input5 = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]

print(numSpecialEquivGroups2(input1))
