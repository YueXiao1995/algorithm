"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:
    Input: [1,2,3,1]
    Output: true


Example 2:
    Input: [1,2,3,4]
    Output: false

Example 3:
    Input: [1,1,1,3,3,4,3,2,4,2]
    Output: true
"""

def containsDuplicate(nums):
    is_contain = False
    unique = set()
    for num in nums:
        if num in unique:
            is_contain = True
            break
        else:
            unique.add(num)
    return is_contain

input1 = [1,2,3,1]
input2 = [1,2,3,4]
input3 = [1,1,1,3,3,4,3,2,4,2]

print(containsDuplicate(input3))
