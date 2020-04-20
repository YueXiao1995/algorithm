"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


def moveZeroes(nums):
    num_of_zero = 0
    l = len(nums)
    i = 0
    while i < l:
        if nums[i] == 0:
            del nums[i]
            l -= 1
            num_of_zero += 1
        else:
            i += 1
    nums.extend(num_of_zero*[0])
    return nums

print(moveZeroes([0,1,0,3,12]))
