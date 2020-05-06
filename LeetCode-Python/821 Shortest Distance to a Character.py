"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.
Example 1:
    Input: S = "loveleetcode", C = 'e'
    Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

Note:
    S string length is in [1, 10000].
    C is a single character, and guaranteed to be in string S.
    All letters in S and C are lowercase.
"""

def shortestToChar(S, C):
    C_position = list()
    for i in range(len(S)):
        if S[i] == C:
            C_position.append(i)

    previous_C = list()
    distance = list()
    for i in range(len(S)):
        if len(C_position) != 0:
            if i == C_position[0]:
                previous_C.append(C_position[0])
                del C_position[0]
                distance.append(0)
            elif i < C_position[0]:
                if len(previous_C) != 0:
                    distance.append(min(i - previous_C[-1], C_position[0] - i))
                else:
                    distance.append(C_position[0] - i)
        else:
            distance.append(i - previous_C[-1])
    return distance


S1 = "loveleetcode"
C1 = 'e'
print(shortestToChar(S1, C1))

S2 = "aaba"
C2 = "b"
print(shortestToChar(S2, C2))
