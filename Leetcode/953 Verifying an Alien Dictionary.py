"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:
    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
    Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
    Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    Output: false
    Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Note:
    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are english lowercase letters.
"""

def isAlienSorted(words, order):
    # store the index of the char in alien language order list
    char_index = dict()
    for i in range(26):
        char_index[order[i]] = i

    # compare each word and the word before one by one
    last_word = None
    for word in words:
        if last_word != None:
            is_in_right_order = None
            # find the shortest length
            shorter_length = min(len(last_word), len(word))
            # iterate the chars in these two word
            is_equal = None
            for i in range(shorter_length):
                # check if the last word's i-th char is in front of the this word's i-th char in order list
                if char_index[last_word[i]] < char_index[word[i]]:
                    is_in_right_order = True
                    is_equal = False
                    break
                elif char_index[last_word[i]] == char_index[word[i]]:
                    is_equal = True
                else:
                    is_in_right_order = False
                    is_equal = False
                    break
            # if previous chars are same, then the last word should be shorter
            if is_equal:
                if shorter_length != len(last_word):
                    is_in_right_order = False
            # if the two words are in wrong order, return Fasle
            if is_in_right_order == False:
                return False
        # update the last word
        last_word = word
    return True

words1 = ["hello","leetcode"]
order1 = "hlabcdefgijkmnopqrstuvwxyz"

words2 = ["word","world","row"]
order2 = "worldabcefghijkmnpqstuvxyz"

words3 = ["apple","app"]
order3 = "abcdefghijklmnopqrstuvwxyz"

words4 = ["iekm","tpnhnbe"]
order4 = "loxbzapnmstkhijfcuqdewyvrg"

print(isAlienSorted(words4, order4))
