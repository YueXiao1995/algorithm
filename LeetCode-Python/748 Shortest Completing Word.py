"""
Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. Such a word is said to complete the given string licensePlate

Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.

It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.

The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.

Example 1:
    Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
    Output: "steps"
    Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
    Note that the answer is not "step", because the letter "s" must occur in the word twice.
    Also note that we ignored case for the purposes of comparing whether a letter exists in the word.

Example 2:
    Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
    Output: "pest"
    Explanation: There are 3 smallest length words that contains the letters "s".
    We return the one that occurred first.

Note:
    licensePlate will be a string with length in range [1, 7].
    licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
    words will have a length in the range [10, 1000].
    Every words[i] will consist of lowercase letters, and have length in range [1, 15].
"""

def shortestCompletingWord(licensePlate, words):
    # downcase the licensePlate and remove the space and the numbers
    # count and sore the freq of char into a dict
    char_freq = dict()
    for char in licensePlate:
        if not char.isdigit() and char != " ":
            if char.lower() not in char_freq:
                char_freq[char.lower()] = 1
            else:
                char_freq[char.lower()] += 1

    shortest_word = None
    for word in words:
        l = len(word)
        if shortest_word == None:
            temp_freq = dict()
            # count and store the freq of the char in word
            for char in word:
                if char not in temp_freq:
                    temp_freq[char] = 1
                else:
                    temp_freq[char] += 1

            has_all_letters = True
            # check if it meet the condition
            for char in char_freq:
                if char not in temp_freq:
                    has_all_letters = False
                    break
                else:
                    if temp_freq[char] < char_freq[char]:
                        has_all_letters = False
                        break
            # first time to set the shortest word
            if has_all_letters:
                shortest_word = word
        else:
            if l < len(shortest_word):
                temp_freq = dict()
                # count and store the freq of the char in word
                for char in word:
                    if char not in temp_freq:
                        temp_freq[char] = 1
                    else:
                        temp_freq[char] += 1

                has_all_letters = True
                # check if it meet the condition
                for char in char_freq:
                    if char not in temp_freq:
                        has_all_letters = False
                        break
                    else:
                        if temp_freq[char] < char_freq[char]:
                            has_all_letters = False
                            break
                # first time to set the shortest word
                if has_all_letters:
                    shortest_word = word

    return shortest_word

licensePlate1 = "1s3 PSt"
words1 = ["step", "steps", "stripe", "stepple"]

licensePlate2 = "1s3 456"
words2 = ["looks", "pest", "stew", "show"]

print(shortestCompletingWord(licensePlate2, words2))
