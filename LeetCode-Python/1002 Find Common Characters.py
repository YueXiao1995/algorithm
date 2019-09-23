"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:
    Input: ["bella","label","roller"]
    Output: ["e","l","l"]

Example 2:
    Input: ["cool","lock","cook"]
    Output: ["c","o"]

Note:
    1 <= A.length <= 100
    1 <= A[i].length <= 100
    A[i][j] is a lowercase letter
"""
def commonChars(A):
    # a list to store the common characters
    common = None
    for string in A:
        # if common is None, set the common
        if common == None:
            common = list(string)
        else:
            # create a new common list, to store the common characters of each sting and old common list
            new_common = list()
            for s_char in string:
                for c_char in common:
                    # check if the characters are equal
                    if s_char == c_char:
                        # add this character to new common list, and remove it from old common list
                        new_common.append(c_char)
                        common.remove(c_char)
                        break
            # update the common list
            common = new_common
    return common


input1 = ["bella","label","roller"]
input2 = ["cool","lock","cook"]

print(commonChars(input1))
