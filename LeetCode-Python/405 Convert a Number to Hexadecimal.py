"""
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:
    All letters in hexadecimal (a-f) must be in lowercase.
    The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
    The given number is guaranteed to fit within the range of a 32-bit signed integer.
    You must not use any method provided by the library which converts/formats the number to hex directly.

Example 1:
    Input: 26
    Output: "1a"

Example 2:
    Input: -1
    Output: "ffffffff"
"""
import string
def toHex(num):
    # the chars that can be used to form a hexadecimal
    digits = list(range(10)) + list(string.ascii_lowercase)
    # if the num is 0, return 0
    if num == 0:
        return "0"
    # if num is negative, we need to change it
    elif num < 0:
        # first get the binary string of its abs value
        binary_string = str(bin(num))[3:]
        # make it a 32 bit string
        binary_string = "0" * (32 - len(binary_string)) + binary_string
        # flip every bit
        filpped_binary_string = ""
        for digit in binary_string:
            if digit == "0":
                filpped_binary_string += "1"
            else:
                filpped_binary_string += "0"
        # convert the binary string to a int and plus 1
        num = int(filpped_binary_string, 2) + 1
    else:
        # if num is positive, dont do anything
        pass
    # convert the decimal int to a hexadecimal string
    base = 16
    hexadeciaml = ""
    while num > 0:
        remain = num % base
        x = remain // (base // 16)
        hexadeciaml = str(digits[x]) + hexadeciaml
        num -= remain
        base *= 16
    return hexadeciaml

input1 = 26
input2 = -1
print(toHex(input2))
