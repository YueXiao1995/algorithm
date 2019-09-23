"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"
"""


def addBinary(a, b):
    list_a = list(a)
    list_b = list(b)
    l1 = len(list_a)
    l2 = len(list_b)
    result = list()
    temp = 0
    index = 0
    while(index < l1 or index < l2):
        num_a = 0
        num_b = 0
        if index < l1:
            num_a = int(list_a[l1-index-1])
        if index < l2:
            num_b = int(list_b[l2-index-1])
        sum = num_a + num_b + temp
        temp = 0
        if sum > 1:
            sum = sum - 2
            temp = 1
            result.append(str(sum))
        else:
            result.append(str(sum))
        index += 1
    if temp != 0:
        result.append(str(temp))
    return ('').join(reversed(result))




input1 = "11"
input2 = "1"

print(addBinary(input1, input2))
