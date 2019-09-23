"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:
    Input:
    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]

    Output: 16

    Explanation: The perimeter is the 16 yellow stripes in the image below:
"""
def islandPerimeter(grid):
    height = len(grid)
    width = len(grid[0])
    perimeter = 0
    # iterate the rows
    for i in range(0, height):
        # iterate the column
        for j in range(0, width):
            if grid[i][j] == 1:

                # the top
                if i == 0:
                    perimeter += 1
                else:
                    if grid[i - 1][j] == 0:
                        perimeter += 1

                # the bottom
                if i == height - 1:
                    perimeter += 1
                else:
                    if grid[i + 1][j] == 0:
                        perimeter += 1

                # the left
                if j == 0:
                    perimeter += 1
                else:
                    if grid[i][j - 1] == 0:
                        perimeter += 1

                # the right
                if j == width - 1:
                    perimeter += 1
                else:
                    if grid[i][j + 1] == 0:
                        perimeter += 1
    return perimeter

input1 = [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]

print(islandPerimeter(input1))
