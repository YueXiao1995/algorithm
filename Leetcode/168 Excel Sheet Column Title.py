"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:
    Input: 1
    Output: "A"

Example 2:
    Input: 28
    Output: "AB"

Example 3:
    Input: 701
    Output: "ZY"
"""
def convertToTitle(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    num_of_digit = 0
    total_number = 0
    # count the number of the chars in final result string
    while n > total_number:
        num_of_digit += 1
        total_number += pow(26, num_of_digit)
    """
    example: AAA = 1*1 + 26*1 + 26*26*1
    """
    # iterate the number of digits times, to get each char in result string
    for i in range(num_of_digit):
        index = n % 26
        if index == 0:
            index = 26
        # add to the result string
        result = alphabet[index - 1] + result
        # update the n
        n = (n - index) // 26
    return result

input1 = 1
input2 = 28
input3 = 701
input4 = 703
input5 = 52
print(convertToTitle(input5))
