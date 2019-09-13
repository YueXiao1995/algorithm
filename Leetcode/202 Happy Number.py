"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by
the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:
    Input: 19
    Output: true
    Explanation:
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1
"""

def isHappy(n):
    n_list = list()
    # iterate until the n repeated
    while n not in n_list:
        # add the n into list
        n_list.append(n)
        # convert the int to list, and calculate the sum of the squares of its digits
        n = list(str(n))
        sum = 0
        for i in n:
            sum += int(i) * int(i)
        # update the n
        n = sum
    # while the loop ending, if the n is 1, the original number is a happy number, return True
    if n == 1:
        return True
    else:
        return False

input1 = 19
print(isHappy(input1))
