"""
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。

示例 1：
    输入：
    [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    输出：
    [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]

示例 2：
    输入：
    [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    输出：
    [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]
"""

# 储存为零的位置
def setZeroes(matrix):
    zero_positions = list()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_positions.append([i, j])

    for position in zero_positions:
        for i in range(len(matrix)):
            matrix[i][position[1]] = 0
        for i in range(len(matrix[0])):
            matrix[position[0]][i] = 0

# 储存为零的列和行
def setZeroes2(matrix):
    y_set = set()
    x_set = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                y_set.add(i)
                x_set.add(j)
    for x in x_set:
        for i in range(len(matrix)):
            matrix[i][x] = 0
    for y in y_set:
        for i in range(len(matrix[0])):
            matrix[y][i] = 0


matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]
setZeroes2(matrix)
print(matrix)

matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]
setZeroes2(matrix)
print(matrix)

