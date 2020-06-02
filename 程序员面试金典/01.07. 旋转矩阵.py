"""
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

不占用额外内存空间能否做到？

示例 1:
    给定 matrix =
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ],

    原地旋转输入矩阵，使其变为:
    [
      [7,4,1],
      [8,5,2],
      [9,6,3]
    ]

示例 2:
    给定 matrix =
    [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ],

    原地旋转输入矩阵，使其变为:
    [
      [15,13, 2, 5],
      [14, 3, 4, 1],
      [12, 6, 8, 9],
      [16, 7,10,11]
    ]。
"""

# 暴力解法
def rotate(matrix):
    rotated_matrix = []
    for row in matrix:
        for i in range(len(row)):
            if len(rotated_matrix) <= i:
                rotated_matrix.append([row[i]])
            else:
                rotated_matrix[i].insert(0, row[i])

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = rotated_matrix[i][j]

# 根据规律，4个一组转动变换
def rotate2(matrix):
    for i in range(len(matrix)//2):
        for j in range(i, len(matrix) - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[-1-j][i]
            matrix[-1-j][i] = matrix[-i-1][-1-j]
            matrix[-i-1][-1-j] = matrix[j][-i-1]
            matrix[j][-i-1] = temp
    return 0

matrix = [[1,2,3],
         [4,5,6],
         [7,8,9]]

rotate2(matrix)
print(matrix)

matrix =[[ 5, 1, 9,11],
         [ 2, 4, 8,10],
         [13, 3, 6, 7],
         [15,14,12,16]]
rotate2(matrix)
print(matrix)

