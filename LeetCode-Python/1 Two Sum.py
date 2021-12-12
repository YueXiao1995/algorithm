"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
""""""
def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# match more faster
def twoSum2(nums, target):
    diff = dict()
    result = None
    for i in range(len(nums)):
        if nums[i] in diff:
            result = [diff[nums[i]], i]
            break
        diff[target - nums[i]] = i
    return result

#  faster than 99.7%
def twoSum3(nums, target):
    diff = set()
    pair = None
    for num in nums:
        if num in diff:
            pair = {num, target - num}
            break
        diff.add((target - num))

    result = list()
    for i in range(len(nums)):
        if nums[i] in pair:
            result.append(i)
    return result

nums1 = [1, 2, 3]
target1 = 5
print(twoSum3(nums1, 5))

nums2 = [2, 7, 11, 15]
target2 = 9
print(twoSum3(nums2, 9))
