"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:
    Input: nums = [3, 6, 1, 0]
    Output: 1
    Explanation: 6 is the largest integer, and for every other number in the array x,
    6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.


Example 2:
    Input: nums = [1, 2, 3, 4]
    Output: -1
    Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.


Note:
    nums will have a length in the range [1, 50].
    Every nums[i] will be an integer in the range [0, 99].
"""

def dominantIndex(nums):
    # if length os nums is 1, return 0
    l = len(nums)
    if l == 1:
        return 0
    # iterate the nums list to get the second_biggest number
    maxinum = None
    second_biggest = None

    for num in nums:
        if maxinum == None:
            maxinum = num
        else:
            if num > maxinum:
                second_biggest = maxinum
                maxinum = num
            else:
                if second_biggest == None:
                    second_biggest = num
                else:
                    if num > second_biggest:
                        second_biggest = num
    # double the second biggest number
    max_double = second_biggest * 2
    for i in range(0, l):
        # if max double is not 0, find the num which bigger or equal to it
        if max_double != 0:
            if nums[i] >= max_double:
                return i
        # if mas double is 0, find the num bigger than it
        else:
            if nums[i] > max_double:
                return i
    return -1


input1 = [3, 6, 1, 0]
input2 = [1, 2, 3, 4]
input3 = [0,0,0,1]

print(dominantIndex(input1))
