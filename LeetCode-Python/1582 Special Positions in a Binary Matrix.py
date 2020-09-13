"""
Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.

A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Example 1:
    Input: mat = [[1,0,0],
                  [0,0,1],
                  [1,0,0]]
    Output: 1
    Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:
    Input: mat = [[1,0,0],
                  [0,1,0],
                  [0,0,1]]
    Output: 3
    Explanation: (0,0), (1,1) and (2,2) are special positions.

Example 3:
    Input: mat = [[0,0,0,1],
                  [1,0,0,0],
                  [0,1,1,0],
                  [0,0,0,0]]
    Output: 2

Example 4:
    Input: mat = [[0,0,0,0,0],
                  [1,0,0,0,0],
                  [0,1,0,0,0],
                  [0,0,1,0,0],
                  [0,0,0,1,1]]
    Output: 3

Constraints:
    rows == mat.length
    cols == mat[i].length
    1 <= rows, cols <= 100
    mat[i][j] is 0 or 1.
"""

def numSpecial(mat):
    column_zero_count = dict()
    row_zero_count = dict()
    positions = list()
    w = len(mat[0])
    h = len(mat)
    for i in range(h):
        for j in range(w):
            if mat[i][j] == 1:
                positions.append([i, j])
                if i not in row_zero_count:
                    row_zero_count[i] = 1
                else:
                    row_zero_count[i] += 1

                if j not in column_zero_count:
                    column_zero_count[j] = 1
                else:
                    column_zero_count[j] += 1

    special_positions_count = 0
    for position in positions:
        row_idnex = position[0]
        column_index = position[1]
        if column_zero_count[column_index] == 1 and row_zero_count[row_idnex] == 1:
            special_positions_count += 1

    return special_positions_count


mat = [[1,0,0],
                  [0,0,1],
                  [1,0,0]]
print(numSpecial(mat))

mat = [[1,0,0],
                  [0,1,0],
                  [0,0,1]]
print(numSpecial(mat))

mat = [[0,0,0,1],
                  [1,0,0,0],
                  [0,1,1,0],
                  [0,0,0,0]]
print(numSpecial(mat))

mat = [[0,0,0,0,0],
                  [1,0,0,0,0],
                  [0,1,0,0,0],
                  [0,0,1,0,0],
                  [0,0,0,1,1]]
print(numSpecial(mat))
