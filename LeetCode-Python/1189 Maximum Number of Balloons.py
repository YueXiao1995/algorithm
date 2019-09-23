"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
    Input: text = "nlaebolko"
    Output: 1

Example 2:
    Input: text = "loonbalxballpoon"
    Output: 2

Example 3:
    Input: text = "leetcode"
    Output: 0

Constraints:
    1 <= text.length <= 10^4
    text consists of lower case English letters only.
"""

def maxNumberOfBalloons(text):
    char_freq = dict()
    for char in text:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    print(char_freq)

    min = None
    target_word = "balloon"
    for char in target_word:
        if char in char_freq:
            if char == 'l' or char == 'o':
                temp_min = char_freq[char] // 2
            else:
                temp_min = char_freq[char]

            if min == None:
                min = temp_min
            else:
                if min > temp_min:
                    min = temp_min
        else:
            return 0
    return min


input1 = "nlaebolko"
input2 = "loonbalxballpoon"
input3 = "leetcode"

print(maxNumberOfBalloons(input3))
