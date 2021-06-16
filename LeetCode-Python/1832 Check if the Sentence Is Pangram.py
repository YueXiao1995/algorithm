"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:
    Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
    Output: true
    Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
    Input: sentence = "leetcode"
    Output: false

Constraints:
    1 <= sentence.length <= 1000
    sentence consists of lowercase English letters.
"""

import string

def checkIfPangram(sentence):
    """
    :type sentence: str
    :rtype: bool
    """
    alphabet = list(string.ascii_lowercase)
    for letter in sentence:
        if letter in alphabet:
            alphabet.remove(letter)
    if len(alphabet) == 0:
        return True
    else:
        return False

sentence = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(sentence))

sentence = "leetcode"
print(checkIfPangram(sentence))
