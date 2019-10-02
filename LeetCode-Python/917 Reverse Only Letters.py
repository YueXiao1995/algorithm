"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:
    Input: "ab-cd"
    Output: "dc-ba"

Example 2:
    Input: "a-bC-dEf-ghIj"
    Output: "j-Ih-gfE-dCba"

Example 3:
    Input: "Test1ng-Leet=code-Q!"
    Output: "Qedo1ct-eeLg=ntse-T!"

Note:
    S.length <= 100
    33 <= S[i].ASCIIcode <= 122
    S doesn't contain \ or "
"""
import string
def reverseOnlyLetters(S: str) -> str:
    letters = set(string.ascii_letters)
    letters_list = list()
    punctuations_list = list()
    # separate the letters and punctuations, store them in two lists respectively
    for char in S:
        if char in letters:
            letters_list.append(char)
            punctuations_list.append("")
        else:
            punctuations_list.append(char)
    # generate a new list with the punctuations and letters
    index = 0
    for i in range(len(punctuations_list)):
        if punctuations_list[i] == "":
            punctuations_list[i] = letters_list[-1-index]
            index += 1
    # form a string and return it
    return ("").join(punctuations_list)

input1 = "ab-cd"
input2 = "a-bC-dEf-ghIj"
input3 = "Test1ng-Leet=code-Q!"

print(reverseOnlyLetters(input3))

