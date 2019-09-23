"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
    Input: [1,12,-5,-6,50,3], k = 4
    Output: 12.75
    Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75


Note:
    1 <= k <= n <= 30,000.
    Elements of the given array will be in the range [-10,000, 10,000].
"""
def findMaxAverage(nums, k):
    max_sum = None
    temp_sum = None
    last_num = None

    for i in range(0, len(nums) - k + 1):
        if max_sum == None:
            sum = 0
            for j in range(0, k):
                sum += nums[j]
            max_sum = sum
            temp_sum = sum
            last_num = nums[i]
        else:
            temp_sum -= last_num
            temp_sum += nums[i + k - 1]
            last_num = nums[i]
            if temp_sum > max_sum:
                max_sum = temp_sum

    return float(max_sum)/ k

input1 = [1,12,-5,-6,50,3]
k1 = 4
print(findMaxAverage(input1, k1))
