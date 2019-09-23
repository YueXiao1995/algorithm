"""
Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all rows.

If there is no common element, return -1

Example 1:
    Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
    Output: 5

Constraints:
    1 <= mat.length, mat[i].length <= 500
    1 <= mat[i][j] <= 10^4
    mat[i] is sorted in increasing order.
"""

def smallestCommonElement(mat):
    num_in_mat = dict()
    l = len(mat)
    for i in range(l):
        num_in_row = set()
        for j in range(len(mat[i])):
            num_in_row.add(mat[i][j])
        print(num_in_row)

        for num in num_in_row:
            if num in num_in_mat:
                num_in_mat[num] += 1
            else:
                num_in_mat[num] = 1
    print(num_in_mat)
    for num in sorted(num_in_mat.keys()):
        if num_in_mat[num] == l:
            return num
    return -1


mat1 = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
mat2 = [[1]]
print(smallestCommonElement(mat2))
