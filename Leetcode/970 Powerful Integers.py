"""
Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.

Example 1:
    Input: x = 2, y = 3, bound = 10
    Output: [2,3,4,5,7,9,10]
    Explanation:
    2 = 2^0 + 3^0
    3 = 2^1 + 3^0
    4 = 2^0 + 3^1
    5 = 2^1 + 3^1
    7 = 2^2 + 3^1
    9 = 2^3 + 3^0
    10 = 2^0 + 3^2

Example 2:
    Input: x = 3, y = 5, bound = 15
    Output: [2,4,6,8,10,14]

Note:
    1 <= x <= 100
    1 <= y <= 100
    0 <= bound <= 10^6
"""


def powerfulIntegers(x, y, bound):
    x_power_list = list()
    y_power_list = list()
    x_power = 1
    if x == 1:
        x_power_list = [1]
    else:
        while x_power <= bound:
            x_power_list.append(x_power)
            x_power *= x

    y_power = 1
    if y == 1:
        y_power_list = [1]
    else:
        while y_power <= bound:
            y_power_list.append(y_power)
            y_power *= y

    result = set()
    for num_1 in x_power_list:
        for num_2 in y_power_list:
            sum = num_1 + num_2
            if sum <= bound:
                result.add(sum)

    return list(result)

x1 = 2
y1 = 3
bound1 = 10

x2 = 3
y2 = 5
bound2 = 15

x3 = 2
y3 = 1
bound3 = 10

print(powerfulIntegers(x3, y3, bound3))
