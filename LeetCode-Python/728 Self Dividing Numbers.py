"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
    Input:
    left = 1, right = 22
    Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Note:
    The boundaries of each input argument are 1 <= left <= right <= 10000.
"""
def selfDividingNumbers(left, right):
    result = list()
    for i in range(left, right + 1):
        # get the digits of the num
        digits = list(str(i))
        is_self_dividing = True
        # iterate the digits
        for d in digits:
            if int(d) == 0:
                is_self_dividing = False
                break
            elif i % int(d) != 0:
                is_self_dividing = False
                break
        if is_self_dividing:
            result.append(i)
    return result

left1 = 1
right1 = 22

print(selfDividingNumbers(left1, right1))

