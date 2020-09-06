"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Example 1:
    Input: nums = [1,2,3,1,1,3]
    Output: 4
    Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
    Input: nums = [1,1,1,1]
    Output: 6
    Explanation: Each pair in the array are good.

Example 3:
    Input: nums = [1,2,3]
    Output: 0

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 100
"""


def numIdenticalPairs(nums):
    def factorial(n):
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f

    num_index = dict()
    for i in range(len(nums)):
        if nums[i] not in num_index:
            num_index[nums[i]] = [i]
        else:
            num_index[nums[i]].append(i)
    pairs = 0
    for num in num_index:
        n = len(num_index[num])
        if n < 2:
            continue
        r = 2
        c = factorial(n) // (factorial(r) * factorial(n - r))

        pairs += c

    return pairs


nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))

nums = [1,1,1,1]
print(numIdenticalPairs(nums))

nums = [1,2,3]
print(numIdenticalPairs(nums))

