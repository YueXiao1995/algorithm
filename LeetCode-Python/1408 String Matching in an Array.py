"""
Given an array of string words. Return all strings in words which is substring of another word in any order.

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

Example 1:
    Input: words = ["mass","as","hero","superhero"]
    Output: ["as","hero"]
    Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
    ["hero","as"] is also a valid answer.

Example 2:
    Input: words = ["leetcode","et","code"]
    Output: ["et","code"]
    Explanation: "et", "code" are substring of "leetcode".

Example 3:
    Input: words = ["blue","green","bu"]
    Output: []

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 30
    words[i] contains only lowercase English letters.
    It's guaranteed that words[i] will be unique.
"""

def stringMatching(words):
    words.sort(key=len)

    length_list = list()
    for word in words:
        length_list.append(len(word))

    result = list()
    for i in range(len(words)):
        l = len(words[i])
        is_substring = False
        for j in range(i + 1, len(words)):
            for k in range(length_list[j] - l + 1):
                if words[i] == words[j][k: k + l]:
                    is_substring = True
                    break
            if is_substring == True:
                break
        if is_substring:
            result.append(words[i])
    return result

words1 = ["mass","as","hero","superhero"]
words2 = ["leetcode", "et", "code"]
words3 = ["blue","green","bu"]

print(stringMatching(words3))
