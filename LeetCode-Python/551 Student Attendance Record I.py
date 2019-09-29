"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
    Input: "PPALLP"
    Output: True

Example 2:
    Input: "PPALLL"
    Output: False
"""

def checkRecord(s: str) -> bool:
    # use a dict to store the index of different types of attendance records in s
    freq = dict()
    freq["A"] = []
    freq["L"] = []
    freq["P"] = []
    for i in range(len(s)):
        freq[s[i]].append(i)
    # if the number of "A" record bigger than 1, return False
    if len(freq["A"]) > 1:
        return False
    # if the number of "L" record smaller than or equal to 2, return True
    if len(freq["L"]) <= 2:
        return True
    else:
        # check if there are three continue indexs in the list of "L" record.
        l_index_list = freq["L"]
        for i in range(0, len(l_index_list) - 2):
            if l_index_list[i] == l_index_list[i + 1] - 1 == l_index_list[i + 2] - 2:
                return False
        return True

input1 = "PPALLP"
input2 = "PPALLL"
input3 = "LALL"

print(checkRecord(input2))

