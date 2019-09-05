"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Example 1:
    Input: words = ["cat","bt","hat","tree"], chars = "atach"
    Output: 6
    Explanation:
    The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
    Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
    Output: 10
    Explanation:
    The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

Note:
    1 <= words.length <= 1000
    1 <= words[i].length, chars.length <= 100
    All strings contain lowercase English letters only.
"""

def countCharacters(words, chars):
    sum_of_length = 0
    for word in words:
        # convert the string in words to list
        word = list(word)
        # copy the chars and convert it to list
        temp_chars = list(chars)
        # assume the word is good, if find any not good char, update if to False
        is_word_good = True
        # iterate the word list
        for c_word in word:
            # assume the char is not good, is find the same char in copied chars, update it to good
            is_char_good = False
            # iterate the copied chars list
            for c_char in temp_chars:
                # if find, remove it from copied chars, update the char to good char, break the loop
                if c_word == c_char:
                    temp_chars.remove(c_char)
                    is_char_good = True
                    break
            # if the char is not good, the word contains this word is also not good, break the loop
            if is_char_good == False:
                is_word_good = False
                break
        # if the word is good, add its length to the sum length
        if is_word_good:
            sum_of_length += len(word)
    return sum_of_length

words1 = ["cat","bt","hat","tree"]
chars1 = "atach"
words2 = ["hello","world","leetcode"]
chars2 = "welldonehoneyr"

print(countCharacters(words2,chars2))
