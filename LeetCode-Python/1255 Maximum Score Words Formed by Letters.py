"""
Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

Example 1:
    Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    Output: 23
    Explanation:
    Score  a=1, c=9, d=5, g=3, o=2
    Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
    Words "dad" and "dog" only get a score of 21.

Example 2:
    Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
    Output: 27
    Explanation:
    Score  a=4, b=4, c=4, x=5, z=10
    Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
    Word "xxxz" only get a score of 25.

Example 3:
    Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
    Output: 0
    Explanation:
    Letter "e" can only be used once.

Constraints:
    1 <= words.length <= 14
    1 <= words[i].length <= 15
    1 <= letters.length <= 100
    letters[i].length == 1
    score.length == 26
    0 <= score[i] <= 10
    words[i], letters[i] contains only lower case English letters.
"""
import string
def maxScoreWords(words, letters, score):
    letter_freq = dict()
    for letter in letters:
        if letter not in letter_freq:
            letter_freq[letter] = 1
        else:
            letter_freq[letter] += 1

    letter_score = dict()
    all_letters = string.ascii_letters
    for i in range(len(score)):
        if score[i] != 0:
            letter_score[all_letters[i]] = score[i]

    unique_letters = set(letter_freq.keys())

    valid_word_score = dict()
    valid_word = list()
    valid_word_letter_count = dict()
    for word in words:
        letter_count = dict()
        for letter in word:
            if letter not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1
        if set(letter_count.keys()).issubset(unique_letters):
            is_valid = True
            total_score = 0
            for letter in letter_count.keys():
                total_score += letter_count[letter] * letter_score[letter]
                if letter_count[letter] > letter_freq[letter]:
                    is_valid = False
                    break
            if is_valid:
                valid_word.append(word)
                valid_word_score[word] = total_score
                valid_word_letter_count[word] = letter_count

    max_score = 0
    for i in range(len(valid_word)):
        valid_words_group = valid_group(valid_word[i], valid_word[i+1:], letter_freq, valid_word_letter_count)
        for group in valid_words_group:
            total_score = 0
            for letter in group:
                total_score += letter_score[letter]
            if total_score > max_score:
                max_score = total_score
    return max_score

def valid_group(word, words, letter_freq, valid_word_letter_count):
    valid_words_group = set()
    valid_words_group.add(word)
    if len(words) == 0:
        return valid_words_group
    new_letter_freq = letter_freq.copy()
    letter_count = valid_word_letter_count[word]
    for letter in letter_count.keys():
        new_letter_freq[letter] -= letter_count[letter]

    for i in range(len(words)):
        is_valid = True
        letter_count = valid_word_letter_count[words[i]]

        for letter in valid_word_letter_count[words[i]]:
            if letter_count[letter] > new_letter_freq[letter]:
                is_valid = False
                break

        if is_valid:
            new_word = word + words[i]
            new_valid_word_letter_count = valid_word_letter_count.copy()
            new_word_count = dict()
            for letter in new_word:
                if letter not in new_word_count:
                    new_word_count[letter] = 1
                else:
                    new_word_count[letter] += 1
            new_valid_word_letter_count[new_word] = new_word_count
            valid_words_group |= valid_group(new_word, words[i+1:], letter_freq, new_valid_word_letter_count)
    return valid_words_group


#print(valid_group('dog', ['dad', 'good'], {'a': 2, 'c': 1, 'd': 3, 'g': 1, 'o': 2}, {'dog': {'d': 1, 'o': 1, 'g': 1}, 'dad': {'d': 2, 'a': 1}, 'good': {'g': 1, 'o': 2, 'd': 1}}))

words1 = ["dog","cat","dad","good"]
letters1 = ["a","a","c","d","d","d","g","o","o"]
score1 = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
print(maxScoreWords(words1, letters1, score1))

words2 = ["xxxz","ax","bx","cx"]
letters2 = ["z","a","b","c","x","x","x"]
score2 = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
print(maxScoreWords(words2, letters2, score2))

words3 = ["leetcode"]
letters3 = ["l","e","t","c","o","d"]
score3 = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
print(maxScoreWords(words3, letters3, score3))


words4 = ["get","set"]
letters4 = ["g","s","e","t"]
score4 = [0,0,0,0,1,0,2,0,0,0,0,0,0,0,0,0,0,0,3,1,0,0,0,0,0,0]
print(maxScoreWords(words4, letters4, score4))

words5 = ["baaa","aacc","ccbc","da","dbbc"]
letters5 = ["a","a","a","c","c","c","c","c","d","d","d"]
score5 = [9,4,10,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(maxScoreWords(words5, letters5, score5))
