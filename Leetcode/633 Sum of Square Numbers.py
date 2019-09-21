"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
    Input: 5
    Output: True
    Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
    Input: 3
    Output: False
"""

# Time Limit Exceeded
"""
def judgeSquareSum(c):
    pow_list = []
    pow = 0
    num = 0
    while pow <= c:
        pow_list.append(pow)
        num += 1
        pow = num * num
    print(pow_list)
    l = len(pow_list)
    for i in range(l):
        for j in range(i, l):
            if pow_list[i] + pow_list[j] == c:
                return True
    return False
"""
def judgeSquareSum(c):
    return 0
input1 = 5
input2 = 3
input3 = 4
print(judgeSquareSum(2))
