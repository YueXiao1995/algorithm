"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


Example 1:
    Input:
        matrix = [[1,2,3,4],
                  [5,1,2,3],
                  [9,5,1,2]]
    Output: True
    Explanation:
        In the above grid, the diagonals are:
        "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
        In each diagonal all elements are the same, so the answer is True.

Example 2:
    Input:
        matrix = [[1,2],
                  [2,2]]
    Output: False
    Explanation:
        The diagonal "[1, 2]" has different elements.

Note:
    matrix will be a 2D array of integers.
    matrix will have a number of rows and columns in range [1, 20].
    matrix[i][j] will be integers in range [0, 99].

Follow up:
    What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
    What if the matrix is so large that you can only load up a partial row into the memory at once?
"""


def isToeplitzMatrix(matrix):
    height = len(matrix)
    width = len(matrix[0])
    for i in range(0, width):
        start = matrix[0][i]
        x = i
        if i + height <= width:
            h = height
        else:
            h = height - (i + height - width)
        for j in range(0, h):
            print(matrix[j][x])
            if matrix[j][x] != start:
                return False
            x += 1

    for i in range(0, height):
        start = matrix[i][0]
        y = i
        if i + width <= height:
            w = width
        else:
            w = width - (i + width - height)
        for j in range(0, w):
            print(matrix[y][j])
            if matrix[y][j] != start:
                return False
            y += 1

    return True

input1 = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
input2 = [[1, 2], [2, 2]]
input3 = [[1, 2, 3, 4]]
input4 = [[1], [2], [3], [4]]


print(isToeplitzMatrix(input2))
