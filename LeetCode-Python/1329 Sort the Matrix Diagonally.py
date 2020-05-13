"""
Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

Example 1:
    Input: mat = [[3,3,1,1],
                 [2,2,1,2],
                 [1,1,1,2]]
    Output: [[1,1,1,1],
            [1,2,2,2],
            [1,2,3,3]]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 100
    1 <= mat[i][j] <= 100
"""

def diagonalSort(mat):
    w = len(mat[0])
    h = len(mat)
    for i in range(w):
        diagonal = list()
        x = i
        for j in range(h):
            if x > w - 1:
                break
            diagonal.append(mat[j][x])
            x += 1
        diagonal = sorted(diagonal)
        x = i
        for j in range(h):
            if x > w - 1:
                break
            mat[j][x] = diagonal[j]
            x += 1

    for i in range(h):
        diagonal = list()
        y = i
        for j in range(w):
            if y > h - 1:
                break
            diagonal.append(mat[y][j])
            y += 1
        diagonal = sorted(diagonal)

        y = i
        for j in range(w):
            if y > h - 1:
                break
            mat[y][j] = diagonal[j]
            y += 1
    return mat



mat1 = [[3,3,1,1],
       [2,2,1,2],
       [1,1,1,2]]

mat2 = [[1], [2], [3]]
mat3 = [[1]]

print(diagonalSort(mat1))
