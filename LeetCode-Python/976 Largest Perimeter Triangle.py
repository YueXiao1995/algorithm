"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

Example 1:
    Input: [2,1,2]
    Output: 5

Example 2:
    Input: [1,2,1]
    Output: 0

Example 3:
    Input: [3,2,3,4]
    Output: 10

Example 4:
    Input: [3,6,2,3]
    Output: 8

Note:
    3 <= A.length <= 10000
    1 <= A[i] <= 10^6
"""

def largestPerimeter(A):
    # sort the lengths list A
    A = sorted(A)
    longest_perimeter = 0
    # reversely iterate over the lengths list A
    for i in reversed(range(2, len(A))):
        # calculate the sum of the previous two nums
        sum = A[i - 2] + A[i - 1]
        # it the sum is bigger than this one, the triangle is valid
        if sum > A[i]:
            sum += A[i]
            # update the longest perimeter
            if sum > longest_perimeter:
                longest_perimeter = sum
    return longest_perimeter

input1 = [2,1,2]
input2 = [1,2,1]
input3 = [3,2,3,4]
input4 = [3,6,2,3]
print(largestPerimeter(input4))
