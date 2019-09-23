"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Example:
    Input: 28
    Output: True
    Explanation: 28 = 1 + 2 + 4 + 7 + 14
    Note: The input number n will not exceed 100,000,000. (1e8)
"""

# Time Limit Exceeded
"""
def checkPerfectNumber(num):
    i = 1
    divisors_sum = 0
    while i < num:
        if num % i == 0:
            divisors_sum += i
        i += 1
    if divisors_sum == num:
        return True
    else:
        return False
"""
def checkPerfectNumber(num):
    # if num smaller then 2, directly return False
    if num <= 2:
        return False
    # copy the num
    orignial = num
    # calculate and set num = sqrt(num)
    if num > 2:
        start = 0
        end = num
        while end - start > 1:
            # find the value in the middle
            middle = (start + end)//2
            # if the power of middle number bigger than x, use it as the end
            if middle * middle > num:
                end = middle
            # else, use it as the start
            else:
                start = middle
        num = start
    # creat a list
    list = [True] * num
    divisors_sum = 0
    # the start and end point of search
    start = 1
    end = num
    while start <= end:
        if list[start - 1] == True:
            # check if the start is the divisor of the original num
            if orignial % start == 0:
                # update the divisors sum
                divisors_sum += start
                if start != 1:
                    divisors_sum += orignial // start
                if divisors_sum > orignial:
                    return False
            # if the start is not the divisor,
            # find all of the position with index n * start in the range of (start, end)
            # update these position to False
            else:
                if start != 1:
                    index = start
                    while index < end:
                        list[index - 1] = False
                        index += start
        start += 1
    # if the divisors sum equal to original num, return True
    if divisors_sum == orignial:
        return True
    else:
        return False

input1 = 2
print(checkPerfectNumber(input1))
