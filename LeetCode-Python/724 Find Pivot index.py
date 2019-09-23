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
def pivotIndex(nums):
    left_sum = 0
    right_sum = 0
    left_index = 0
    right_index = 1
    if len(nums) == 0:
        return -1
    sum = 0
    for num in nums:
        sum += num
    if sum >= 0:
        while (left_index + right_index <= len(nums) - 1):
            if left_sum > right_sum:
                right_sum += nums[-right_index]
                right_index += 1
            else:
                left_sum += nums[left_index]
                left_index += 1
            print(left_sum)
            print(right_sum)
    else:
        while (left_index + right_index <= len(nums) - 1):
            if left_sum < right_sum:
                right_sum += nums[-right_index]
                right_index += 1
            elif left_sum == right_sum:
                if nums[-right_index] == 0:
                    right_sum += nums[-right_index]
                    right_index += 1
                else:
                    left_sum += nums[left_index]
                    left_index += 1
            else:
                left_sum += nums[left_index]
                left_index += 1
            print(left_sum)
            print(right_sum)

    if left_sum == right_sum:
        return left_index
    else:
        return -1

input1 = [1, 7, 3, 6, 5, 6]
input2 = [1, 2, 3]
input3 = [-1,-1,-1,-1,-1,0]
input4 = [-1,-1,-1,0,-1,-1]
input5 = [-1,-1,0,-1,-1,-1]
input6 = [-1,-1,-1,0,1,-1]
print(pivotIndex(input6))
