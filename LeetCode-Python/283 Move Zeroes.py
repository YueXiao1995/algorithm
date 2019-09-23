"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""
def moveZeroes(nums):
    index = 0
    l = len(nums)
    temp_l = 0 # to record how many element we have iterated
    while index < l:
        if nums[index] == 0:        # if the index-th item is 0
            if temp_l < l:
                nums.append(0)      # append a 0 to the end of list
                del nums[index]     # delete this 0
                temp_l += 1
            else:
                break  # break the loop if the arrive the end of list
        else:
            index += 1
            temp_l += 1
    return nums

input = [0,1,0,3,12]
input2 = [0, 0, 1]
print(moveZeroes(input2))
