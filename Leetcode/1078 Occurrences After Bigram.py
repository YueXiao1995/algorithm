"""
Given words first and second, consider occurrences in some text of the form "first second third", where second comes
immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

Example 1:
    Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
    Output: ["girl","student"]

Example 2:
    Input: text = "we will we will rock you", first = "we", second = "will"
    Output: ["we","rock"]

Note:
    1 <= text.length <= 1000
    text consists of space separated words, where each word consists of lowercase English letters.
    1 <= first.length, second.length <= 10
    first and second consist of lowercase English letters.
"""
def findOcurrences(text, first, second):
    # split the text and store the words into a list
    text_list = text.split(" ")
    # use two variables to store previous two words
    word_before_last = None
    last_word = None
    # find the word meet the condition
    result = list()
    for word in text_list:
        if word_before_last != None:
            if word_before_last == first and last_word == second:
                result.append(word)
        word_before_last = last_word
        last_word = word
    return result


text1 = "alice is a good girl she is a good student"
first1 = "a"
second1 = "good"
text2 = "we will we will rock you"
first2 = "we"
second2 = "will"

print(findOcurrences(text2, first2, second2))
