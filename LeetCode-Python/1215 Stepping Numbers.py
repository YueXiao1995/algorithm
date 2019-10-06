"""
A Stepping Number is an integer such that all of its adjacent digits have an absolute difference of exactly 1. For example, 321 is a Stepping Number while 421 is not.

Given two integers low and high, find and return a sorted list of all the Stepping Numbers in the range [low, high] inclusive.

Example 1:
    Input: low = 0, high = 21
    Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]

Constraints:
    0 <= low <= high <= 2 * 10^9
"""

# Too slow
def countSteppingNumbers(low, high):
    result = list()
    for i in range(low, high + 1):
        num = str(i)
        isSteepingNumber = True
        last_digit = None
        for digit in num:
            if last_digit == None:
                last_digit = digit
            else:
                if abs(int(last_digit) - int(digit)) != 1:
                    isSteepingNumber = False
                    break
        if isSteepingNumber:
            result.append(i)
    return result

# generate stepping numbers digit by digit, not need to linear search
def countSteppingNumbers2(low, high):
    # the stepping numbers with one digit
    init = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # use a 2-D list to store all of the valid stepping number as string,
    # include the string begin with 0, it can be used to construct next array of stepping numbers
    stepping_numbers = list()
    stepping_numbers.append(init)
    # get the number of digits of the high value
    num_of_digit = len(str(high))
    time = 10
    # iterate over the digit position
    for i in range(num_of_digit - 1):
        # generate the new stepping numbers from the previous array of stepping numbers
        new_array = list()
        # iterate over the previous array of stepping number strings
        for num in stepping_numbers[i]:
            # get the first digit of the num
            first_digit = num[0]
            # for the number begin with 1-8, we can generate two numbers
            # for the number begin with 0 and 9, we can generate one number
            if int(first_digit) > 0:
                smaller = str(int(first_digit) - 1) + num
                new_array.append(smaller)
            if int(first_digit) < 9:
                bigger = str(int(first_digit) + 1) + num
                new_array.append(bigger)
        # sort the array and append it to the 2-D stepping number list
        stepping_numbers.append(sorted(new_array))
        time *= 10
    # remove the string begin with "0", convert the char to int
    result_set = set()
    for nums in stepping_numbers:
        nums = set(map(int, nums))
        result_set |= nums
    # select the numbers in range [low, high]
    result = list()
    for num in result_set:
        if num >= low and num <= high:
            result.append(num)
    # sort and return the result
    return sorted(result)

low = 10
high = 21

low2 = 0
high2 = 1000000000

print(countSteppingNumbers2(low, high))
