"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""

def repeatedStringMatch(A: str, B: str) -> int:
    l_A = len(A)
    l_B = len(B)
    # if the string A is longer than B
    if l_A > l_B:
        # check if the B is the substring of A or 2 * A
        possible_repeat_time = 1
        while possible_repeat_time <= 2:
            for i in range(possible_repeat_time * l_A - l_B + 1):
                if A[i:i + l_B] == B:
                    return possible_repeat_time
            possible_repeat_time += 1
            A += A
        # if not, return -1
        return -1
    else:
        # iterate over the B, find the possible repeat times of A
        possible_repeat_time = 0
        i = 0
        while i + l_A <= l_B:
            if B[i: i + l_A] == A:
                if possible_repeat_time == 0 and i != 0:
                    possible_repeat_time += 2
                else:
                    possible_repeat_time += 1
            if possible_repeat_time == 0:
                i += 1
            else:
                if i + l_A == l_B:
                    break
                else:
                    i += l_A
        # check if there is at least one A find in B, and the end of the last A is not equal to the end of B
        if possible_repeat_time != 0 and i + l_A > l_B:
            possible_repeat_time += 1
        # if there is no A found in B, may be it is because B is in the substring of 2 * A
        if possible_repeat_time == 0:
            possible_repeat_time = 2
        # check if the B is in the multiple times of A
        A = A * possible_repeat_time
        for i in range(possible_repeat_time * l_A - l_B + 1):
            if A[i:i+l_B] == B:
                return possible_repeat_time
        return -1

A1 = "abcd"
B1 = "cdabcdab"

A2 = "abcd"
B2 = "baabcdabcd"

A3 = "abcd"
B3 = "abcd"

A4 = "a"
B4 = "aa"

A5 = "aaaaaaaaaaaaaaaaaaaaaab"
B5 = "ba"

A6 = "abcd"
B6 = "bcdab"

print(repeatedStringMatch(A5, B5))
