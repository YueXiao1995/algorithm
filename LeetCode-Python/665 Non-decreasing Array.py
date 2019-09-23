"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
    Input: [4,2,3]
    Output: True
    Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
    Input: [4,2,1]
    Output: False
    Explanation: You can't get a non-decreasing array by modify at most one element.

Note: The n belongs to [1, 10,000].
"""

def checkPossibility(nums):
    l = len(nums)
    # find the first decrease number
    last_num = None
    index = None
    for i in range(0, l):
        if last_num != None:
            if nums[i] < last_num:
                index = i
                break
        last_num = nums[i]
    # if not find, return true
    if index == None:
            return True

    # move this number to the right place
    new_list1 = list()
    modified = False
    for i in range(0, l):
        if nums[i] > nums[index] and modified == False:
            new_list1.append(nums[index])
            modified = True
        if i != index:
            new_list1.append(nums[i])

    # check if the array is non-decreasing
    is_non_decreasing = True
    last_num = None
    for num in new_list1:
        if last_num != None:
            if num < last_num:
                is_non_decreasing = False
                break
        last_num = num
    # if the array is no-decreasing, return True
    if is_non_decreasing:
        return True

    # move the number before to the right place
    new_list2 = list()
    modified = False
    for i in reversed(range(0, l)):
        if nums[i] < nums[index - 1] and modified == False:
            new_list2.append(nums[index - 1])
            modified = True
        if i != index - 1:
            new_list2.append(nums[i])

    # check if the array is non-decreasing
    is_non_decreasing = True
    last_num = None
    for num in new_list2:
        if last_num != None:
            if num > last_num:
                is_non_decreasing = False
                break
        last_num = num

    if is_non_decreasing:
        return True
    else:
        return False

input1 = [4, 2, 3]
input2 = [4, 2, 1]
input3 = [1, 2, 4, 3, 3]
input4 = [1, 2, 4, 4, 3, 5]
input5 = [1]
input6 = [1, 1, 1, 1, 1]
input7 = [1, 2, 3, 4, 5]
print(checkPossibility(input7))
