"""
Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.



Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16


Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""

def numberOfSubarrays(nums, k):
    new_nums = list()
    odd_index = list()
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_nums.append(0)
        else:
            new_nums.append(1)
            odd_index.append(i)
    print(odd_index)

    if len(odd_index) < k:
        return 0

    print(new_nums)




    return 0

nums1 = [1,1,2,1,1]
k1 = 3
print(numberOfSubarrays(nums1, k1))

nums2 = [2,4,6]
k2 = 1
print(numberOfSubarrays(nums2, k2))

nums3 = [2,2,2,1,2,2,1,2,2,2]
k3 = 2
print(numberOfSubarrays(nums3, k3))

