"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.


Example 1:
    Input: [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.

Example 2:
    Input: [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.
"""

def plusOne(digits):
    l = len(digits)
    digits[l-1] += 1
    for i in reversed(range(0, l)):
        if digits[i] > 9:
            if i != 0:
                digits[i-1] += 1
                digits[i] -= 10
            else:
                digits[i] -= 10
                newdigit = [1] + digits
                return newdigit
    return digits


input = [9, 9, 9, 9]
print(plusOne(input))
