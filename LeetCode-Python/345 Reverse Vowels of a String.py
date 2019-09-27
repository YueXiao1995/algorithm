"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
    Input: "hello"
    Output: "holle"

Example 2:
    Input: "leetcode"
    Output: "leotcede"

Note:
    The vowels does not include the letter "y".
"""

def reverseVowels(s: str) -> str:
    # a set of the vowels (both uppercase and lowercase)
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    # find the vowels in string s and record their index
    vowels_list = list()
    vowels_index = list()
    # iterate over the string s
    for i in range(len(s)):
        if s[i] in vowels:
            vowels_list.append(s[i])
            vowels_index.append(i)

    # reverse the vowels list
    for i in range(len(vowels_list) // 2):
        char = vowels_list[i]
        vowels_list[i] = vowels_list[-1 - i]
        vowels_list[-1-i] = char

    # update the string s
    s = list(s)
    for i in range(len(vowels_list)):
        s[vowels_index[i]] = vowels_list[i]
    return ("").join(s)


input1 = "hello"
input2 = "leetcode"

print(reverseVowels(input1))
