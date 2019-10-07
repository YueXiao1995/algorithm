"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
    Input: S = "a1b2"
    Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

    Input: S = "3z4"
    Output: ["3z4", "3Z4"]

    Input: S = "12345"
    Output: ["12345"]
Note:
    S will be a string with length between 1 and 12.
    S will consist only of letters or digits.
"""

def letterCasePermutation(S):
    possible_strings = [S]
    for i in range(len(S)):
        new_strings = list()
        if S[i].isalpha():
            if S[i].islower():
                new_char = S[i].upper()
            else:
                new_char = S[i].lower()
            for string in possible_strings:
                copy = list(string)
                copy[i] = new_char
                new_strings.append(("").join(copy))
        possible_strings.extend(new_strings)

    return possible_strings

S1 = "a1b2"
S2 = "3z4"
S3 = "12345"

print(letterCasePermutation(S1))
