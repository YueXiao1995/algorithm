"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
    Input: [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

Example 2:
    Input: [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
    Input: [[0,2]]
    Output: 0
    Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

Note:
    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    grid[i][j] is only 0, 1, or 2.
"""

def orangesRotting2(grid):
    # return the new found rotted oranges and the grid after one minute
    def rotting(rotted_oranges_list, grid):
        new_rotted_oranges_set = set()
        for rotted_orange in rotted_oranges_list:
            row = rotted_orange[0]
            column = rotted_orange[1]
            connected_cell = [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]
            for cell in connected_cell:
                if cell[0] in range(len(grid)) and cell[1] in range(len(grid[0])):
                    if grid[cell[0]][cell[1]] == 1:
                        if cell not in rotted_oranges:
                            new_rotted_oranges_set.add(cell)
                            grid[cell[0]][cell[1]] = 2

        return new_rotted_oranges_set, grid

    # get the init rotted oranges
    rotted_oranges = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                rotted_oranges.add((i, j))

    # rotting minute by minute, until there is no new rotted oranges can be found
    time = 0
    while True:
        new_rotted_oranges, grid = rotting(rotted_oranges, grid)
        if len(new_rotted_oranges) == 0:
            break
        time += 1
        rotted_oranges = rotted_oranges | new_rotted_oranges

    # check if there still fresh oranges in the grid
    for row in grid:
        for cell in row:
            if cell == 1:
                return -1
    return time


input1 = [[2,1,1],[1,1,0],[0,1,1]]
input2 = [[2,1,1],[0,1,1],[1,0,1]]
input3 = [[0, 2]]

print(orangesRotting2(input1))
print(orangesRotting2(input2))
print(orangesRotting2(input3))
