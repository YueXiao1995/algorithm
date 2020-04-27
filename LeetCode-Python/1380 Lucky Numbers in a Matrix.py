"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Example 1:
    Input: matrix = [[3,7,8],
                    [9,11,13],
                    [15,16,17]]
    Output: [15]
    Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column

Example 2:
    Input: matrix = [[1,10,4,2],
                    [9,3,8,7],
                    [15,16,17,12]]
    Output: [12]
    Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:
    Input: matrix = [[7,8],
                    [1,2]]
    Output: [7]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= n, m <= 50
    1 <= matrix[i][j] <= 10^5.
    All elements in the matrix are distinct.
"""

def luckyNumbers(matrix):
    h = len(matrix)
    w = len(matrix[0])

    min_in_row = list()
    for i in range(h):
        min_in_row.append(min(matrix[i]))

    max_in_column = list()
    for i in range(w):
        column = list()
        for j in range(h):
            column.append(matrix[j][i])
        max_in_column.append(max(column))

    lucky_nums = list(set(max_in_column) & set(min_in_row))

    return lucky_nums

matrix1 = [[3,7,8],[9,11,13],[15,16,17]]
matrix2 = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
matrix3 = [[7,8],[1,2]]

print(luckyNumbers(matrix3))
