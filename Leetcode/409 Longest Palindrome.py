"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
    Input: "abccccdd"
    Output: 7
    Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

def longestPalindrome(s):
    # count and record the freq of the chars in string
    freq = dict()
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    print(freq)

    # calculate the maximum longest length of the palindrome
    length = 0
    for n in freq:
        # if the freq of char n is bigger than or equal to 2
        if freq[n] // 2 > 0:
            # increase the length
            length += (freq[n] // 2) * 2
            # decrease the freq
            freq[n] = freq[n] % 2
    # check if any of the char's freq is still bigger than 1, that means this char can be put into the centre of the palindrome
    for n in freq:
        if freq[n] == 1:
            # length plus 1 and break the loop
            length += 1
            break
    return length

input1 = "abccccdd"
print(longestPalindrome(input1))
