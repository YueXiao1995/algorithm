"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

Example 1:
    Input: [1,2,3,3]
    Output: 3

Example 2:
    Input: [2,1,2,5,3,2]
    Output: 2

Example 3:
    Input: [5,1,5,2,5,3,5,4]
    Output: 5

Note:
    4 <= A.length <= 10000
    0 <= A[i] < 10000
    A.length is even
"""

def repeatedNTimes(A):
    # store the numbers into a dict, if it is already exist in the dict, return it
    nums = dict()
    for num in A:
        if num in nums:
            return num
        else:
            nums[num] = 1

input1 = [1,2,3,3]
input2 = [2,1,2,5,3,2]
input3 = [5,1,5,2,5,3,5,4]
print(repeatedNTimes(input1))
