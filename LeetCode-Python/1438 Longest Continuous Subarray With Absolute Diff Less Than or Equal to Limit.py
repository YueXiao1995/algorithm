"""
Given an array of integers nums and an integer limit, return the size of the longest continuous subarray such that the absolute difference between any two elements is less than or equal to limit.

In case there is no subarray satisfying the given condition return 0.

Example 1:
    Input: nums = [8,2,4,7], limit = 4
    Output: 2
    Explanation: All subarrays are:
    [8] with maximum absolute diff |8-8| = 0 <= 4.
    [8,2] with maximum absolute diff |8-2| = 6 > 4.
    [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
    [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
    [2] with maximum absolute diff |2-2| = 0 <= 4.
    [2,4] with maximum absolute diff |2-4| = 2 <= 4.
    [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
    [4] with maximum absolute diff |4-4| = 0 <= 4.
    [4,7] with maximum absolute diff |4-7| = 3 <= 4.
    [7] with maximum absolute diff |7-7| = 0 <= 4.
    Therefore, the size of the longest subarray is 2.

Example 2:
    Input: nums = [10,1,2,4,7,2], limit = 5
    Output: 4
    Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:
    Input: nums = [4,2,2,2,4,4,2,2], limit = 0
    Output: 3

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    0 <= limit <= 10^9
"""

import math
def longestSubarray(nums, limit):
    start_point = 0
    max_length = 0
    max_value = nums[0]
    max_index = 0
    min_value = nums[0]
    min_index = 0
    i = 0

    while i < len(nums):
        # check if the max/min_value changed
        if nums[i] > max_value or nums[i] < min_value:
            # check if the limit is breaked
            if max(nums[i], max_value) - min(nums[i], min_value) > limit:
                # update the max length, update the start point
                max_length = max(max_length, i - start_point)
                if nums[i] > max_value:
                    start_point = min_index + 1
                    i = start_point
                else:
                    start_point = max_index + 1
                    i = start_point
                max_value = nums[start_point]
                max_index = start_point
                min_value = nums[start_point]
                min_index = start_point
            # if not breaked, update the max/value value and the their index
            else:
                if nums[i] > max_value:
                    max_value = nums[i]
                    max_index = i
                else:
                    min_value = nums[i]
                    min_index = i
        # if not changed, move forward 1 step
        else:
            i += 1
            # check if reached the end of the nums array
            if i == len(nums):
                # update the max length
                max_length = max(i - start_point, max_length)
    return max_length


nums1 = [8,2,4,7]
limit1 = 4

nums2 = [10,1,2,4,7,2]
limit2 = 5

nums3 = [4,2,2,2,4,4,2,2]
limit3 = 0

print(longestSubarray(nums1, limit1))
print(longestSubarray(nums2, limit2))
print(longestSubarray(nums3, limit3))
