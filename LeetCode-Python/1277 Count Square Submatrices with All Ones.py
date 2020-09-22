"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:
    Input: matrix =
    [
      [0,1,1,1],
      [1,1,1,1],
      [0,1,1,1]
    ]
    Output: 15
    Explanation:
    There are 10 squares of side 1.
    There are 4 squares of side 2.
    There is  1 square of side 3.
    Total number of squares = 10 + 4 + 1 = 15.

Example 2:
    Input: matrix =
    [
      [1,0,1],
      [1,1,0],
      [1,1,0]
    ]
    Output: 7
    Explanation:
    There are 6 squares of side 1.
    There is 1 square of side 2.
    Total number of squares = 6 + 1 = 7.


Constraints:
    1 <= arr.length <= 300
    1 <= arr[0].length <= 300
    0 <= arr[i][j] <= 1
"""


def countSquares(matrix):
    h = len(matrix)
    w = len(matrix[0])
    max_size = min(h, w)
    valid_points = set()
    valid_submatrices = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                valid_points.add((i, j))
                valid_submatrices += 1
    size = 2
    while size <= max_size:
        new_valid_points = set()
        for point in valid_points:
            points = set()
            is_point_valid = True
            if point[0] < h - size + 1 and point[1] < w - size + 1:
                for i in range(point[0], point[0] + size):
                    for j in range(point[1], point[1] + size):
                        points.add(point)
                        if matrix[i][j] != 1:
                            is_point_valid = False
                            break
            else:
                is_point_valid = False
            if is_point_valid:
                valid_submatrices += 1
                new_valid_points = new_valid_points | points
        size += 1
        if len(new_valid_points) == 0:
            break
        else:
            valid_points = new_valid_points
    return valid_submatrices

matrix =[
      [0,1,1,1],
      [1,1,1,1],
      [0,1,1,1]]
print(countSquares(matrix))

matrix =[
      [1,0,1],
      [1,1,0],
      [1,1,0]]
print(countSquares(matrix))
