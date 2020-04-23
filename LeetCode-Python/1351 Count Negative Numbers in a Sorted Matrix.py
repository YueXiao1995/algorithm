"""
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.

Return the number of negative numbers in grid.

Example 1:
    Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    Output: 8
    Explanation: There are 8 negatives number in the matrix.

Example 2:
    Input: grid = [[3,2],[1,0]]
    Output: 0

Example 3:
    Input: grid = [[1,-1],[-1,-1]]
    Output: 3

Example 4:
    Input: grid = [[-1]]
    Output: 1

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100
"""
def countNegatives(grid):
    w = len(grid[0])
    h = len(grid)
    num_of_negative_num = 0

    for i in range(h):
        if w == 0:
            break
        for j in range(w):
            if grid[i][j] < 0:
                num_of_negative_num += (w - j) * (h - i)
                w = j
                break
    return num_of_negative_num

grid1 = [[4,3,2,-1],
        [3,2,1,-1],
        [1,1,-1,-2],
        [-1,-1,-2,-3]]

grid2 = [[3,2],
        [1,0]]

grid3 = [[1,-1],
        [-1,-1]]

grid4 = [[-1]]


print(countNegatives(grid4))
