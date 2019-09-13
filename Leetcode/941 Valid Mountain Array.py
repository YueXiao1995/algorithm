"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

Example 1:
    Input: [2,1]
    Output: false

Example 2:
    Input: [3,5,5]
    Output: false

Example 3:
    Input: [0,3,2,1]
    Output: true

Note:
    0 <= A.length <= 10000
    0 <= A[i] <= 10000
"""

def validMountainArray(A):
    # if length smaller than 3, it is impossible to form a mountain with less than 3 nums
    if len(A) < 3:
        return False
    # check if the array if a mountain
    is_increase = None
    last_num = None
    # iterate the array
    for num in A:
        if last_num != None:
            if is_increase == None:
                # check if the first two nums are in ascending order, if not, return False
                if last_num < num:
                    is_increase = True
                else:
                    return False
            else:
                # when the nums before are in ascending order
                if is_increase:
                    if last_num > num:
                        is_increase = False
                    elif last_num == num:
                        return False
                # when the nums before are in descending order
                else:
                    if last_num <= num:
                        return False
        # update the last num
        last_num = num
    # check if the array is ended with a descending order part
    if is_increase:
        return False
    else:
        return True

input1 = [2, 1]
input2 = [3, 5, 5]
input3 = [0, 3, 2, 1]
input4 = []
input5 = [1]
print(validMountainArray(input3))
