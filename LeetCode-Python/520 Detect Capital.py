"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
    Input: "USA"
    Output: True

Example 2:
    Input: "FlaG"
    Output: False

Note:
    The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""

def detectCapitalUse(word: str) -> bool:
    # find all of the uppercase chars and record their index
    capital_index_list = list()
    for i in range(len(word)):
        if not word[i].islower():
            capital_index_list.append(i)
    # decide the return value by the length of the capital index list and the first element
    l = len(capital_index_list)
    if l == 0 or l == len(word) or (l == 1 and capital_index_list[0] == 0):
        return True
    else:
        return False

input1 = "USA"
input2 = "FlaG"
input3 = "leetcode"
input4 = "Google"

print(detectCapitalUse(input3))
