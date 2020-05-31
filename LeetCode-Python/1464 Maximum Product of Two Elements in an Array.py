"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

Example 1:
    Input: nums = [3,4,5,2]
    Output: 12
    Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

Example 2:
    Input: nums = [1,5,4,5]
    Output: 16
    Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

Example 3:
    Input: nums = [3,7]
    Output: 12

Constraints:
    2 <= nums.length <= 500
    1 <= nums[i] <= 10^3
"""

def maxProduct(nums):
    max_values = [max(nums[0:2]), min(nums[0:2])]
    for i in range(2, len(nums)):
        if nums[i] > max_values[0]:
            max_values.insert(0, nums[i])
            del max_values[-1]
        elif nums[i] > max_values[1]:
            max_values.insert(1, nums[i])
            del max_values[-1]
        else:
            pass
    return (max_values[0] - 1) * (max_values[1] - 1)

nums = [3,4,5,2]
print(maxProduct(nums))

nums = [1,5,4,5]
print(maxProduct(nums))

nums = [3, 7]
print(maxProduct(nums))
