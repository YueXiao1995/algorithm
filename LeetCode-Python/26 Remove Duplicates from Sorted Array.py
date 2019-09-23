"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


Example 1:

    Given nums = [1,1,2],

    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

    It doesn't matter what you leave beyond the returned length.


Example 2:

    Given nums = [0,0,1,1,1,2,2,3,3,4],

    Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

    It doesn't matter what values are set beyond the returned length.

"""

"""
def removeDuplicates(nums):
    single_nums = list()
    l = len(nums)
    i = 0
    while(i < l):
        if nums[i] not in single_nums:
            single_nums.append(nums[i])
            i += 1
        else:
            del nums[i]
            l -= 1

    return len(single_nums), nums
"""

def removeDuplicates(nums):
    l = len(nums)
    i = 0
    while (i < l - 1):
        if nums[i] == nums[i + 1]:
            del nums[i]
            l -= 1
        else:
            i += 1

    return l



input = [1,1,1,1]

print(removeDuplicates(input))
