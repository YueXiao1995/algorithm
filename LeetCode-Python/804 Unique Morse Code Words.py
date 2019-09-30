"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
    Input: words = ["gin", "zen", "gig", "msg"]
    Output: 2
    Explanation:
    The transformation of each word is:
    "gin" -> "--...-."
    "zen" -> "--...-."
    "gig" -> "--...--."
    "msg" -> "--...--."

    There are 2 different transformations, "--...-." and "--...--.".

Note:
    The length of words will be at most 100.
    Each words[i] will have length in range [1, 12].
    words[i] will only consist of lowercase letters.
"""
import string
def uniqueMorseRepresentations(words):
    # the morse code alphabet list and the english alphabet list
    morse_code_alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    english_alphabet = list(string.ascii_lowercase)

    # store the corresponding relations into a dict
    english_to_morsecode = dict()
    for i in range(26):
        english_to_morsecode[english_alphabet[i]] = morse_code_alphabet[i]
    # convert the words to some morse code strings, and store them into a set
    morse_code_srings = set()
    for word in words:
        # convert the word char by char
        morse_code_string = ""
        for char in word:
            morse_code_string += english_to_morsecode[char]
        # store the morse code string into the set
        morse_code_srings.add(morse_code_string)
    # return the number of string in the set
    return len(morse_code_srings)

words1 = ["gin", "zen", "gig", "msg"]
words2 = []
words3 = ["rwjje","aittjje","auyyn","lqtktn","lmjwn"]

print(uniqueMorseRepresentations(words2))
