"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such
that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true

Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true

Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false
"""

def containsNearbyDuplicate(nums, k):
    position = dict()
    for i in range(0, len(nums)):
        if nums[i] not in position:
            position[nums[i]] = [i]
        else:
            position[nums[i]].append(i)
    for char_p_list in position.values():
        for i in range(0, len(char_p_list)):
            for j in range(i + 1, len(char_p_list)):
                if char_p_list[j] - char_p_list[i] <= k:
                    return True
    return False


input1 = [1,2,3,1]
k1 = 3
input2 = [1,0,1,1]
k2 = 1
input3 = [1,2,3,1,2,3]
k3 = 2

print(containsNearbyDuplicate(input3, k3))
