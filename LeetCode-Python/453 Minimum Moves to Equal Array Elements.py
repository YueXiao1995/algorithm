"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal,
where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""

# Time Limit Exceeded
def minMoves2(nums):

    def areElementsEqual(nums):
        first_element = nums[0]
        for num in nums:
            if num != first_element:
                return False
        return True

    def findMinDiffToMaxValue(nums):
        l = len(nums)
        max_value = nums[0]
        max_value_index = 0
        for i in range(l):
            if nums[i] > max_value:
                max_value = nums[i]
                max_value_index = i
        i = 0
        while i < l:
            if nums[i] == max_value:
                del nums[i]
                l -= 1
            else:
                i += 1
        second_max_value = max(nums)
        return max_value - second_max_value, max_value_index

    num_of_moves = 0
    while areElementsEqual(nums) == False:
        min_diff, max_value_index = findMinDiffToMaxValue(list(nums))
        nums = [x + min_diff for x in nums]
        nums[max_value_index] -= min_diff
        num_of_moves += min_diff
        print(nums)
    return num_of_moves

input1 = [1, 2, 3]
input2 = [0, 0, 0]
input3 = [1, 2]
input4 = [-100, 0, 100]
input5 = [-1, 1]
print(minMoves2(input5))
