"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
    Input: 4
    Output: 2

Example 2:
    Input: 8
    Output: 2

Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""
# Time Limit Exceeded
"""
def mySqrt1(x):
    i = 0
    while i < x + 1:
        if i * i > x:
            return i - 1
        elif i * i == x:
            return i
        i += 1
"""

def mySqrt(x):
    if x < 2:
        return x
    start = 0
    end = x
    while end - start > 1:
        # find the value in the middle
        middle = (start + end)//2
        # if the power of middle number bigger than x, use it as the end
        if middle * middle > x:
            end = middle
        # else, use it as the start
        else:
            start = middle
        print(middle)
    return start

input1 = 4
input2 = 8
input3 = 0
input4 = 2147395599
input5 = 100
print(mySqrt(input2))
