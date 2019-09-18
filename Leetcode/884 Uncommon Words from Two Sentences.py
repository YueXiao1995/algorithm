"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:
    Input: A = "this apple is sweet", B = "this apple is sour"
    Output: ["sweet","sour"]

Example 2:
    Input: A = "apple apple", B = "banana"
    Output: ["banana"]

Note:
    0 <= A.length <= 200
    0 <= B.length <= 200
    A and B both contain only spaces and lowercase letters.
"""

def uncommonFromSentences(A, B):
    # split the sentences
    A = A.split(" ")
    B = B.split(" ")
    # count the freq of the word in first sentence
    freq = dict()
    for word in A:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    # count the freq of the word in second sentence
    for word in B:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    # find the word which only appear once in these two sentences
    result = list()
    for word in freq:
        if freq[word] == 1:
            result.append(word)
    return result


A1 = "this apple is sweet"
B1 = "this apple is sour"
A2 = "apple apple"
B2 = "banana"

print(uncommonFromSentences(A2, B2))
