"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

"""

"""

def maxSubArray(nums):
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    print(max)
    sum_list = list()
    sum = 0
    max_sum = nums[0]
    max_sum_index = 0
    i = 0
    for num in nums:
        sum += num
        sum_list.append(sum)
        if sum > max_sum:
            max_sum_index = i
            max_sum = sum
        i += 1
        print(sum_list)

    print(max_sum)
    print(max_sum_index)

    if max_sum < 0:
        return max
    sum_list2 = list()
    sum2 = 0
    max_sum2 = 0
    max_sum_index2 = 0

    for i in reversed(range(0, max_sum_index + 1)):
        print(i)
        sum2 += nums[i]
        sum_list2.append(sum2)
        if sum2 > max_sum2:
            max_sum_index2 = i
            max_sum2 = sum2

        print(sum_list2)

    result = 0
    for i in range(max_sum_index2, max_sum_index+1):
        print(nums[i])
        result += nums[i]

    return result


input = [-2,-1]
print(maxSubArray(input))
"""
