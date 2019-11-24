"""
Given a 2D grid of size n * m and an integer k. You need to shift the grid k times.

In one shift operation:
    Element at grid[i][j] becomes at grid[i][j + 1].
    Element at grid[i][m - 1] becomes at grid[i + 1][0].
    Element at grid[n - 1][m - 1] becomes at grid[0][0].

Return the 2D grid after applying shift operation k times.

Example 1:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
    Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:
    Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
    Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
    Output: [[1,2,3],[4,5,6],[7,8,9]]

Constraints:
    1 <= grid.length <= 50
    1 <= grid[i].length <= 50
    -1000 <= grid[i][j] <= 1000
    0 <= k <= 100
"""

def shiftGrid(grid, k):
    grid_1D = list()
    for row in grid:
        grid_1D.extend(row)
    n = len(grid)
    m = len(grid[0])
    size = n * m
    k = k % size
    grid_1D = grid_1D[-k:] + grid_1D[:-k]
    shifted_grid = list()
    for i in range(n):
        shifted_grid.append(grid_1D[i * m:(i + 1) * m])
    return shifted_grid

grid1 = [[1,2,3],[4,5,6],[7,8,9]]
k1 = 1
print(shiftGrid(grid1, k1))

grid2 = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k2 = 4
print(shiftGrid(grid2, k2))

grid3 = [[1,2,3],[4,5,6],[7,8,9]]
k3 = 9
print(shiftGrid(grid3, k3))
