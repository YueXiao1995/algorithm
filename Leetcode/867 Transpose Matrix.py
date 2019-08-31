"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.



Example 1:
    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
    Input: [[1,2,3],[4,5,6]]
    Output: [[1,4],[2,5],[3,6]]
"""


def transpose(A):
    row = len(A)
    column = len(A[0])

    result = list()
    for i in range(0, column):
        result.append(list())
        for j in range(0, row):
            result[i].append(A[j][i])
    return result


input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(transpose(input))
