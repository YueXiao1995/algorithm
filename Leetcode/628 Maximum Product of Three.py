"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
    Input: [1,2,3]
    Output: 6

Example 2:
    Input: [1,2,3,4]
    Output: 24

Note:
    The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
    Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""

def maximumProduct(nums):
    # sort the list
    nums = sorted(nums)
    l = len(nums)
    # find the position of the first non-negative number
    n = 0
    for i in range(0, l):
        if nums[i] >= 0:
            n = i
            break
    # the number of non-negative numbers
    right = l - n
    # the number of negative numbers
    left = n
    max_product = None

    # if there are 3 or more than 3 non-negative numbers
    if right >= 3:
        # if there are 2 or more negative numbers
        if left >= 2:
            max_left_product = nums[0] * nums[1]
            max_right_product = nums[-2] * nums[-3]
            if max_left_product > max_right_product:
                max_product = nums[-1] * max_left_product
            else:
                max_product = nums[-1] * max_right_product
        else:
            max_product = nums[-1] * nums[-2] * nums[-3]
    elif right == 2:
        if left >= 3:
            left_min_product = nums[n - 2] * nums[n - 3]
            right_product = nums[-1] * nums[-2]
            if left_min_product > right_product:
                max_product = nums[n - 1] * right_product
            else:
                max_product = nums[n -1] * left_min_product
        else:
            max_product = nums[-1] * nums[-2] * nums[-3]
    elif right == 1:
        max_product = nums[0] * nums[1] * nums[-1]

    elif right == 0:
        max_product = nums[-1] * nums[-2] * nums[-3]

    return max_product






input1 = [1, 2, 3]
input2 = [1, 2, 3, 4]
input3 = [-2, -1, 0, 1, 2]
input4 = [-4, -3, -2, -1]
input5 = [-1, 1, 2]
input6 = [-3, -2, -1, 1, 1]
input7 = [-3, -2, -1, 3]

print(maximumProduct(input7))
