"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
    Input:
        nums =
        [[1,2],
         [3,4]]
        r = 1, c = 4
    Output:
        [[1,2,3,4]]
    Explanation:
        The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.


Example 2:
    Input:
        nums =
        [[1,2],
        [3,4]]
        r = 2, c = 4
    Output:
        [[1,2],
        [3,4]]
    Explanation:
        There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Note:
    The height and width of the given matrix is in range [1, 100].
    The given r and c are all positive.
"""


def matrixReshape(nums, r, c):
    # if the number of numbers in original matrix and new reshaped matrix are not equal, return the original matrix
    if r * c != len(nums) * len(nums[0]):
        return nums
    # read all of the nums into a 1-D list
    nums_list = list()
    for row in nums:
        for num in row:
            nums_list.append(num)
    new_nums = list()
    index = 0
    # store the subarrays into new nums list as rows
    while index < r * c:
        print(nums_list[index:index + c])
        new_nums.append(nums_list[index: index + c])
        index += c
    return new_nums

nums1 = [[1, 2], [3, 4]]
r1 = 1
c1 = 4

nums2 = [[1, 2], [3, 4]]
r2 = 2
c2 = 4

print(matrixReshape(nums1, r1, c1))
