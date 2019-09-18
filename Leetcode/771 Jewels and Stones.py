"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
    Input: J = "aA", S = "aAAbbbb"
    Output: 3

Example 2:
    Input: J = "z", S = "ZZ"
    Output: 0

Note:
    S and J will consist of letters and have length at most 50.
    The characters in J are distinct.
"""

def numJewelsInStones(J, S):
    # convert the string to list
    J = list(J)
    num_of_Jewels = 0
    # iterate the string to count the jewels
    for char in S:
        if char in J:
            num_of_Jewels += 1
    return num_of_Jewels

J1 = "aA"
S1 = "aAAbbbb"

J2 = "z"
S2 = "ZZ"

print(numJewelsInStones(J2, S2))
