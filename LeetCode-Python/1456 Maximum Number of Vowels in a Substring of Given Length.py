"""
Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).

Example 1:
    Input: s = "abciiidef", k = 3
    Output: 3
    Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
    Input: s = "aeiou", k = 2
    Output: 2
    Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
    Input: s = "leetcode", k = 3
    Output: 2
    Explanation: "lee", "eet" and "ode" contain 2 vowels.

Example 4:
    Input: s = "rhythms", k = 4
    Output: 0
    Explanation: We can see that s doesn't have any vowel letters.

Example 5:
    Input: s = "tryhard", k = 4
    Output: 1

Constraints:
    1 <= s.length <= 10^5
    s consists of lowercase English letters.
    1 <= k <= s.length
"""

def maxVowels(s, k):
    vowel_letters = {'a', 'e', 'i', 'o','u'}
    vowel_letters_indexs = list()
    for i in range(len(s)):
        if s[i] in vowel_letters:
            vowel_letters_indexs.append(i)

    if len(vowel_letters_indexs) == 0:
        return 0
    index_diff = list()
    for i in range(1, len(vowel_letters_indexs)):
        index_diff.append(vowel_letters_indexs[i] - vowel_letters_indexs[i - 1])

    total_diff = 0
    start_index = 0
    end_index = 0
    max_num = 1
    while end_index < len(index_diff):

        if total_diff + index_diff[end_index] <= k - 1:
            max_num = max(max_num, end_index - start_index + 2)
            total_diff += index_diff[end_index]
            end_index += 1
        else:
            if end_index == len(index_diff) - 1:
                break
            else:
                if start_index < end_index:
                    total_diff -= index_diff[start_index]
                    start_index += 1
                else:
                    total_diff += index_diff[end_index]
                    end_index += 1
    return max_num

s = "weallloveyou"
k = 7
print(maxVowels(s, k))

s = "abciiidef"
k = 3
print(maxVowels(s, k))

s = "aeiou"
k = 2
print(maxVowels(s, k))

s = "leetcode"
k = 3
print(maxVowels(s, k))

s = "rhythms"
k = 4
print(maxVowels(s, k))

s = "tryhard"
k = 4
print(maxVowels(s, k))

