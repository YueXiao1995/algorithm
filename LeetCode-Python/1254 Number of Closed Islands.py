"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:
    Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    Output: 2
    Explanation:
    Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
    Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
    Output: 1

Example 3:
    Input: grid = [[1,1,1,1,1,1,1],
                   [1,0,0,0,0,0,1],
                   [1,0,1,1,1,0,1],
                   [1,0,1,0,1,0,1],
                   [1,0,1,1,1,0,1],
                   [1,0,0,0,0,0,1],
                   [1,1,1,1,1,1,1]]
    Output: 2

Constraints:
    1 <= grid.length, grid[0].length <= 100
    0 <= grid[i][j] <=1
"""

def closedIsland(grid):
    def dfs(root, h, s, grid):
        row = root[0]
        column = root[1]
        if grid[row][column] == 1:
            return grid, True
        if grid[row][column] == 0:
            if row == 0 or row == height - 1 or column == 0 or column == width - 1:
                return grid, False
        grid[row][column] = 1
        is_closed_island = True
        connected_cells = [[row - 1, column],[row + 1, column],[row, column - 1],[row, column + 1]]
        for cell in connected_cells:
            if cell[0] >= 0 and cell[0] < height and cell[1] >= 0 and cell[1] < width:
                grid, is_closed = dfs(cell, h, s, grid)
                if not is_closed:
                    is_closed_island = False
        return grid, is_closed_island

    height = len(grid)
    width = len(grid[0])
    num_of_closed_islands = 0
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if grid[i][j] == 0:
                grid, is_closed_island = dfs([i, j], height, width, grid)
                if is_closed_island == True:
                    num_of_closed_islands += 1
    return num_of_closed_islands

grid1 = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]
print(closedIsland(grid1))

grid2 = [[0,0,1,0,0],
         [0,1,0,1,0],
         [0,1,1,1,0]]
print(closedIsland(grid2))

grid3 = [[1,1,1,1,1,1,1],
         [1,0,0,0,0,0,1],
         [1,0,1,1,1,0,1],
         [1,0,1,0,1,0,1],
         [1,0,1,1,1,0,1],
         [1,0,0,0,0,0,1],
         [1,1,1,1,1,1,1]]
print(closedIsland(grid3))

grid4 = [[0,0,1,1,0,1,0,0,1,0],
         [1,1,0,1,1,0,1,1,1,0],
         [1,0,1,1,1,0,0,1,1,0],
         [0,1,1,0,0,0,0,1,0,1],
         [0,0,0,0,0,0,1,1,1,0],
         [0,1,0,1,0,1,0,1,1,1],
         [1,0,1,0,1,1,0,0,0,1],
         [1,1,1,1,1,1,0,0,0,0],
         [1,1,1,0,0,1,0,1,0,1],
         [1,1,1,0,1,1,0,1,1,0]]
print(closedIsland(grid4))
