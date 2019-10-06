"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
    Given nums = [-2, 0, 3, -5, 2, -1]
    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3

Note:
    You may assume that the array does not change.
    There are many calls to sumRange function.
"""


class NumArray(object):

    def __init__(self, nums):
        self.sum_list = list()
        sum = 0
        for num in nums:
            sum += num
            self.sum_list.append(sum)
        """
        :type nums: List[int]
        """

    def sumRange(self, i, j):
        if i > 0:
            return self.sum_list[j] - self.sum_list[i - 1]
        else:
            return self.sum_list[j]

nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 5))
