"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:
    Input: S = "ab#c", T = "ad#c"
    Output: true
    Explanation: Both S and T become "ac".

Example 2:
    Input: S = "ab##", T = "c#d#"
    Output: true
    Explanation: Both S and T become "".

Example 3:
    Input: S = "a##c", T = "#a#c"
    Output: true
    Explanation: Both S and T become "c".

Example 4:
    Input: S = "a#c", T = "b"
    Output: false
    Explanation: S becomes "c" while T becomes "b".

Note:
    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.

Follow up:
    Can you solve it in O(N) time and O(1) space?
"""

def backspaceCompare(S: str, T: str) -> bool:
    # get the final result of string S
    result_s = ""
    for i in range(len(S)):
        if S[i] != "#":
            result_s += S[i]
        else:
            if len(result_s) != 0:
                result_s = result_s[:-1]

    # get the final result of string T
    result_t = ""
    for i in range(len(T)):
        if T[i] != "#":
            result_t += T[i]
        else:
            if len(result_t) != 0:
                result_t = result_t[:-1]
    # compare these two strings
    if result_s == result_t:
        return True
    else:
        return False

S1 = "ab#c"
T1 = "ad#c"

S2 = "ab##"
T2 = "c#d#"

S3 = "a##c"
T3 = "#a#c"

S4 = "a#c"
T4 = "b"

print(backspaceCompare(S4, T4))
