"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words.
If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.

Example 1:
    Input:  words = ["w","wo","wor","worl", "world"]
    Output: "world"
    Explanation:
    The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
    Input:  words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    Output: "apple"
    Explanation:
    Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Note:
    All the strings in the input will only contain lowercase letters.
    The length of words will be in the range [1, 1000].
    The length of words[i] will be in the range [1, 30].
"""

def longestWord(words):
    class treeNode(object):
        def __init__(self, x):
            self.str = x
            self.children = []

    # generate a words tree, return the longest word
    def generateTree(root, words):
        longest_words = [root.str]
        i = 0
        # find all of the children
        while i < len(words):
            if len(words[i]) == len(root.str) + 1 and words[i][:len(root.str)] == root.str:
                root.children.append(treeNode(words[i]))
                del words[i]
            else:
                i += 1
        # generate the subtree from the children
        for child in root.children:
            return_word = generateTree(child, words)
            # compare the longest words returned from children, if longer than the first word in longest_words list, replace it with a new list
            if len(return_word) > len(longest_words[0]):
                longest_words = [return_word]
            # if equal long, add it into the list
            elif len(return_word) == len(longest_words[0]):
                longest_words.append(return_word)
        # sort the longest words list
        longest_words = sorted(longest_words)
        # return the first one
        return longest_words[0]

    return generateTree(treeNode(""), words)


words1 = ["w","wo","wor","worl", "world"]
words2 = ["a", "banana", "app", "appl", "ap", "apply", "apple"]

print(longestWord(words1))
print(longestWord(words2))
