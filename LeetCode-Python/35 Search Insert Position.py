"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
    Input: [1,3,5,6], 5
    Output: 2

Example 2:
    Input: [1,3,5,6], 2
    Output: 1

Example 3:
    Input: [1,3,5,6], 7
    Output: 4

Example 4:
    Input: [1,3,5,6], 0
    Output: 0
"""
# method
def searchInsert(nums, target):
    l = len(nums)
    for i in range(0, l):
        # if num is bigger than or equal to the target, return its index
        if nums[i] >= target:
            return i
        # if num is less than target
        else:
            # if has reached the end of list, the target should be append to the end of nums
            if i == l - 1:
                return i + 1




# test cases
input1 = [1,3,5,6]
target1 = 5
input2 = [1,3,5,6]
target2 = 2
input3 = [1,3,5,6]
target3 = 7
input4 = [1,3,5,6]
target4 = 0

# test
print(searchInsert(input2, target2))
