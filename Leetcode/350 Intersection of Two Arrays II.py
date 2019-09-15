"""
Given two arrays, write a function to compute their intersection.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]

Note:
    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:
    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

def intersect(nums1, nums2):
    # count and record the freq of the nums in nums1 list
    num_freq_1 = dict()
    for num in nums1:
        if num in num_freq_1:
            num_freq_1[num] += 1
        else:
            num_freq_1[num] = 1
    # count and record the freq of the nums in nums2 list
    num_freq_2 = dict()
    for num in nums2:
        if num in num_freq_2:
            num_freq_2[num] += 1
        else:
            num_freq_2[num] = 1
    # iterate one of the dict, find the num exist in both dict as key
    result = list()
    for num in num_freq_1:
        if num in num_freq_2:
            # find the minimum freq of this num in these two dicts
            if num_freq_2[num] > num_freq_1[num]:
                min = num_freq_1[num]
            else:
                min = num_freq_2[num]
            # append min number of num into the result list
            for i in range(0, min):
                result.append(num)
    return result

nums1 = [1,2,2,1]
nums2 = [2,2]

nums3 = [4,9,5]
nums4 = [9,4,9,8,4]
print(intersect(nums3, nums4))
