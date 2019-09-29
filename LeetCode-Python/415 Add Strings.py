"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

def addStrings(num1: str, num2: str) -> str:
    # use a dict to store the relationship of string char and num
    str_to_num = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    sum = ""

    l_num1 = len(num1)
    l_num2 = len(num2)

    carry_bit = 0
    # iterate the two strings
    for i in range(max(l_num1, l_num2)):
        temp_sum = carry_bit
        if i < l_num1:
            temp_sum += str_to_num[num1[-1-i]]
        if i < l_num2:
            temp_sum += str_to_num[num2[-1-i]]
        # if the sum bigger than 9, the carry_bit should be 1
        if temp_sum > 9:
            sum = str(temp_sum - 10) + sum
            carry_bit = 1
        else:
            sum = str(temp_sum) + sum
            carry_bit = 0
    # if the carry bit is not 0, add 1 to the start of the sum string
    if carry_bit != 0:
        sum = "1" + sum
    return sum

input1 = "100"
input2 = "234"
print(addStrings(input1, input2))
