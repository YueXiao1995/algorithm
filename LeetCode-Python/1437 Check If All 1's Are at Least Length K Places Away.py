"""
Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

Example 1:
    Input: nums = [1,0,0,0,1,0,0,1], k = 2
    Output: true
    Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:
    Input: nums = [1,0,0,1,0,1], k = 2
    Output: false
    Explanation: The second 1 and third 1 are only one apart from each other.

Example 3:
    Input: nums = [1,1,1,1,1], k = 0
    Output: true

Example 4:
    Input: nums = [0,1,0,1], k = 1
    Output: true

Constraints:
    1 <= nums.length <= 10^5
    0 <= k <= nums.length
    nums[i] is 0 or 1
"""

def kLengthApart(nums, k):
    is_at_least_k_places_away = True
    last_one_index = None
    for i in range(len(nums)):
        if nums[i] == 1:
            if last_one_index == None:
                last_one_index = i
            else:
                if i - last_one_index <= k:
                    is_at_least_k_places_away = False
                    break
                else:
                    last_one_index = i

    return is_at_least_k_places_away

nums1 = [1,0,0,0,1,0,0,1]
k1 = 2

nums2 = [1,0,0,1,0,1]
k2 = 2

nums3 = [1,1,1,1,1]
k3 = 0

nums4 = [0, 1, 0, 1]
k4 = 1

print(kLengthApart(nums1, k1))
print(kLengthApart(nums2, k2))
print(kLengthApart(nums3, k3))
print(kLengthApart(nums4, k4))
