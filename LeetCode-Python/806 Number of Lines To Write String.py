"""
We are to write the letters of a given string S, from left to right into lines. Each line has maximum width 100 units, and if writing a letter would cause the width of the line to exceed 100 units, it is written on the next line. We are given an array widths, an array where widths[0] is the width of 'a', widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.

Now answer two questions: how many lines have at least one character from S, and what is the width used by the last such line? Return your answer as an integer list of length 2.

Example :
    Input:
    widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    S = "abcdefghijklmnopqrstuvwxyz"
    Output: [3, 60]
    Explanation:
    All letters have the same length of 10. To write all 26 letters,
    we need two full lines and one line with 60 units.

Example :
    Input:
    widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    S = "bbbcccdddaaa"
    Output: [2, 4]
    Explanation:
    All letters except 'a' have the same length of 10, and
    "bbbcccdddaa" will cover 9 * 10 + 2 * 4 = 98 units.
    For the last 'a', it is written on the second line because
    there is only 2 units left in the first line.
    So the answer is 2 lines, plus 4 units in the second line.
Note:
    The length of S will be in the range [1, 1000].
    S will only contain lowercase letters.
    widths is an array of length 26.
    widths[i] will be in the range of [2, 10].
"""
import string
def numberOfLines(widths, S):
    chars = string.ascii_lowercase
    chars_length = dict()
    for i in range(26):
        chars_length[chars[i]] = widths[i]
    lines = 1
    empty_units = 100
    for i in range(len(S)):
        l = chars_length[S[i]]
        if empty_units > l:
            empty_units -= l
        elif empty_units == l:
            empty_units = 100
            lines += 1
        else:
            lines += 1
            empty_units = 100 - l

    return [lines, 100 - empty_units]

widths1 = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S1 = "abcdefghijklmnopqrstuvwxyz"
print(numberOfLines(widths1, S1))

widths2 = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S2 = "bbbcccdddaaa"
print(numberOfLines(widths2, S2))

widths3 = [5,7,4,7,6,7,9,5,8,8,5,10,9,10,2,5,7,9,3,8,8,8,10,2,2,9]
S3 = "lgrnv"
print(numberOfLines(widths3, S3))
