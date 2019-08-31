"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
    Input: [1,3,5,4,7]
    Output: 3
    Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
    Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.

Example 2:
    Input: [2,2,2,2,2]
    Output: 1
    Explanation: The longest continuous increasing subsequence is [2], its length is 1.
    Note: Length of the array will not exceed 10,000.
"""


def findLengthOfLCIS(nums):
    max_length = 0
    current_length = 0
    last_num = 0
    l = len(nums)
    for i in range(0, l):
        if i == 0:
            last_num = nums[i]
            current_length = 1
        else:
            if nums[i] > last_num:
                current_length += 1
            else:
                if current_length > max_length:
                    max_length = current_length
                current_length = 1
            last_num = nums[i]

    if current_length > max_length:
        max_length = current_length
    return max_length


input = [1, 3, 5, 4, 7]
input2 = [2, 2, 2, 2, 2]
input3 = [1, 3, 5, 7]
input4= [1,3,5,4,2,3,4,5]
print(findLengthOfLCIS(input4))
