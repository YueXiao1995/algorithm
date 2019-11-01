"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:
    [[0,0,0,0,0,0,0,0]]
    Given the above grid, return 0.
    Note: The length of each dimension in the given grid does not exceed 50.
"""

def maxAreaOfIsland(grid):
    width = len(grid[0])
    height = len(grid)

    # given a root cell, perform depth first search, return the area of a island
    def dfs(root, grid):
        y = root[0]
        x = root[1]
        # if the cell is outside the grid, return 0
        if y < 0 or y >= height or x < 0 or x >= width:
            return 0
        # fi the cell is water, return zero
        if grid[y][x] == 0:
            return 0
        # if the cell is ground
        # init the area to 1
        total_area = 1
        # change the value of the cell to 0, so if it is searched again, the process will stop here
        grid[y][x] = 0
        # get the for directionally connected cells
        directionally_connected_cells = [(y -1, x), (y+1,x), (y, x-1), (y, x + 1)]
        # search each cell and update the area of the island
        for cell in directionally_connected_cells:
            total_area += dfs(cell, grid)
        return total_area

    maximun_area = 0
    # iterate every cell in the grid, if the value is 1, perform the depth first search
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                maximun_area = max(maximun_area,(dfs((i, j), grid)))

    return maximun_area

input1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(input1))

input2 = [[0,0,0,0,0,0,0,0]]
print(maxAreaOfIsland(input2))
