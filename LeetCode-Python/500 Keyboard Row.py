"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

def findWords(words):
    # list the chars in each rows on American keyboard
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")

    result = list()
    # check if the chars in each word are come from the same row
    for word in words:
        row = None
        is_chars_in_same_row = True
        # downcase the word and iterate it
        for char in list(word.lower()):
            # find the first char in word form these three rows, and set the row
            if row == None:
                if char in row1:
                    row = row1
                elif char in row2:
                    row = row2
                else:
                    row = row3
            # if the char is not in the row, this word is not conform to the condition, break the loop
            else:
                if char not in row:
                    is_chars_in_same_row = False
                    break
        # append the word which conform to the condition to the result list
        if is_chars_in_same_row:
           result.append(word)
    return result

input = ["Hello", "Alaska", "Dad", "Peace"]
print(findWords(input))
