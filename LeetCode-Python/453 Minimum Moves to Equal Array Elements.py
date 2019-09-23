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

"""
def minMoves(nums):
    l = len(nums)
    min = nums[0]
    min_index = 0
    max = nums[0]
    max_index = 0
    index = 0
    while index < l:
        if nums[index] > max:
            max_index = index
            max = nums[index]
        elif nums[index] < min:
            min_index = index
            min = nums[index]
        index += 1
    print(min)
    print(max)

    num_of_move = 0
    while min != max:
        num_of_move += max - min
        for i in range(0, l):
            if i != max_index:
                nums[i] += max - min
        index = 0
        min = nums[0]
        min_index = 0
        max = nums[0]
        max_index = 0
        while index < l:
            if nums[index] > max:
                max_index = index
                max = nums[index]
            elif nums[index] < min:
                min_index = index
                min = nums[index]
            index += 1

    return num_of_move
"""
def minMoves(nums):
    l = len(nums)
    min = nums[0]
    max = nums[0]
    max_index = 0
    index = 0

    while index < l:
        if nums[index] > max:
            max = nums[index]
            max_index = index
        elif nums[index] < min:
            min = nums[index]
        index += 1
    print(min)
    print(max)

    all_equal_except_max = True
    index = 0
    while index < l:
        if index != max_index and nums[index] != min:
            all_equal_except_max = False
        index += 1


    diff_sum = 0
    index = 0
    while index < l:
        diff_sum += max - nums[index]
        index += 1

    if diff_sum == 0:
        return 0
    print(diff_sum)
    if all_equal_except_max == False:
        diff_sum += l

    while diff_sum % (l - 1) != 0:
        diff_sum += l

    return diff_sum // (l - 1)




input1 = [1, 2, 3]
input2 = [0, 0, 0]
input3 = [1, 2]
input4 = [-100, 0, 100]
print(minMoves(input4))
