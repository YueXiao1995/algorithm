"""
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

Example 1:
    Input: nums = [3,5]
    Output: 2
    Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

Example 2:
    Input: nums = [0,0]
    Output: -1
    Explanation: No numbers fit the criteria for x.
    If x = 0, there should be 0 numbers >= x, but there are 2.
    If x = 1, there should be 1 number >= x, but there are 0.
    If x = 2, there should be 2 numbers >= x, but there are 0.
    x cannot be greater since there are only 2 numbers in nums.

Example 3:
    Input: nums = [0,4,3,0,4]
    Output: 3
    Explanation: There are 3 values that are greater than or equal to 3.

Example 4:
    Input: nums = [3,6,7,7,0]
    Output: -1

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 1000
"""


def specialArray(nums):
    l = len(nums)
    nums = sorted(nums, reverse=True)
    print(nums)
    count = list()
    unique_nums = list()
    for i in range(l):
        if i == l - 1:
            count.append(i + 1)
            unique_nums.append(nums[i])
        elif nums[i + 1] < nums[i]:
            count.append(i + 1)
            unique_nums.append(nums[i])
    print(count)
    print(unique_nums)
    index = -1
    for i in range(max(unique_nums), 0, -1):
        if i in unique_nums:
            index += 1
        if i == count[index]:
            return i
    return - 1


nums = [3,5]
print(specialArray(nums))

nums = [0,0]
print(specialArray(nums))

nums = [0,4,3,0,4]
print(specialArray(nums))

nums = [3,6,7,7,0]
print(specialArray(nums))

nums = [3,9,7,8,3,8,6,6]
print(specialArray(nums))

nums =[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
print(specialArray(nums))
