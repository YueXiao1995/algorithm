"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Note:
    You may assume that all elements in nums are unique.
    n will be in the range [1, 10000].
    The value of each element in nums will be in the range [-9999, 9999].
"""

def search(nums, target):
    # init the start and end point of the search
    start = 0
    end = len(nums) - 1

    # if the length of the nums is 1
    if end == 0:
        if nums[0] == target:
            return 0
        else:
            return -1
    # check if the target is smaller than the smallest num in the nums list
    if nums[start] > target:
        return -1
    # check if the target is bigger than the biggest num in the nums list
    if nums[end] < target:
        return -1
    # binary search, until the start + 1 = end
    while start <= end - 1:
        # get the middle point
        middle = (start + end) // 2
        # return index or update the start or end point
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            end = middle
        else:
            start = middle
        # if the start and end point are next to each other, check them
        if start == end - 1:
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            return -1


nums1 = [-1,0,3,5,9,12]
target1 = 9

nums2 = [-1,0,3,5,9,12]
target2 = 2

nums3 = [5]
target3 = 5

nums4 = [2, 5]
target4 = 2

nums5 = [5]
target5 = [-5]

nums6 = [2, 5]
target6 = 0


print(search(nums1, target1))
print(search(nums2, target2))
print(search(nums3, target3))
print(search(nums4, target4))
print(search(nums5, target5))



