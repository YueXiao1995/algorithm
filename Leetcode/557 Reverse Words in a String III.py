"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


def reverseWords(s):
    words = s.split(" ")
    new_s = list()
    for word in words:
        word_list = list(word)
        for i in range(0, len(word_list)//2):
            temp = word[i]
            word_list[i] = word_list[-1-i]
            word_list[-1-i] = temp
        new_s.append(''.join(word_list))
    new_s = ' '.join(new_s)
    return new_s


input = "Let's take LeetCode contest"
print(reverseWords(input))
