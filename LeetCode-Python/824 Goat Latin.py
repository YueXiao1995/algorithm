"""
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.

Example 1:
    Input: "I speak Goat Latin"
    Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Example 2:
    Input: "The quick brown fox jumped over the lazy dog"
    Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

Notes:
    S contains only uppercase, lowercase and spaces. Exactly one space between each word.
    1 <= S.length <= 150.
"""

def toGoatLatin(S: str) -> str:
    # define a set which contains all of the vowels
    vowel_chars = {"a", "e", "i", "o", "u"}
    # split the sentence into a list
    S = S.split(" ")
    # init the number of "a" appended to the end of the words to 1
    num_of_a = 1
    # iterate over the words list
    for i in range(len(S)):
        # check if the first char is a vowel
        if S[i][0].lower() in vowel_chars:
            S[i] += "ma"
        else:
            S[i] = S[i][1:] + S[i][0] + "ma"
        # append "a"s to the end of the word
        S[i] += "a" * num_of_a
        num_of_a += 1
    # form a string by the words list and return it
    return (" ").join(S)

input1 = "I speak Goat Latin"
input2 = "The quick brown fox jumped over the lazy dog"

print(toGoatLatin(input2))
