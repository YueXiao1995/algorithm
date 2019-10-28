"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:

    Input: nums = [1, 7, 3, 6, 5, 6]
    Output: 3
    Explanation:
    The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
    Also, 3 is the first index where this occurs.


Example 2:
    Input: nums = [1, 2, 3]
    Output: -1
    Explanation:
    There is no index that satisfies the conditions in the problem statement.

Note:
    The length of nums will be in the range [0, 10000].
    Each element nums[i] will be an integer in the range [-1000, 1000].
"""

def pivotIndex2(nums):
    # calculate the sum of the nums list
    sum_value = sum(nums)
    # iterate the nums, and grow a temp sum value step by step
    temp_sum = 0
    for i in range(len(nums)):
        # it the temp sum equal to half of the (sum - num), return the index i
        if temp_sum == (sum_value - nums[i]) / 2.0:
            return i
        temp_sum += nums[i]
    return -1


input1 = [1, 7, 3, 6, 5, 6]
input2 = [1, 2, 3]
input3 = [-1,-1,-1,-1,-1,0]
input4 = [-1,-1,-1,0,-1,-1]
input5 = [-1,-1,0,-1,-1,-1]
input6 = [-1,-1,-1,0,1,-1]
input7 = [-1,-1,-1,-1,-1,-1]
print(pivotIndex2(input7))
