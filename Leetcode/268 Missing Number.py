"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2

Example 2:
    Input: [9,6,4,2,3,5,7,0,1]
    Output: 8
"""

"""
def missingNumber(nums):
    # create a list contains 0, 1, ... n, where n = len(nums) + 1
    new_nums = list(range(len(nums)+1))
    # sort the nums list
    nums = sorted(nums)
    # delete the nums which is in nums
    for num in nums:
        new_nums.remove(num)
    return new_nums[0]
"""
# faster method, because list.remove() need to iterate the nums to find the target num
def missingNumber(nums):
    # create a list contains 0, 1, ... n, where n = len(nums) + 1
    new_nums = list(range(len(nums)+1))
    # set the num in new list which index is exist in nums to None
    for num in nums:
        new_nums[num] = None
    # return the num in new list which is not None
    for num in new_nums:
        if num != None:
            return num

input1 = [3, 0 ,1]
input2 = [9,6,4,2,3,5,7,0,1]
print(missingNumber(input1))
