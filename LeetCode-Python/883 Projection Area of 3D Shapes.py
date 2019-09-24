"""
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.



Example 1:
    Input: [[2]]
    Output: 5

Example 2:
    Input: [[1,2],[3,4]]
    Output: 17
    Explanation:
    Here are the three projections ("shadows") of the shape made with each axis-aligned plane.

Example 3:
    Input: [[1,0],[0,2]]
    Output: 8

Example 4:
    Input: [[1,1,1],[1,0,1],[1,1,1]]
    Output: 14

Example 5:
    Input: [[2,2,2],[2,1,2],[2,2,2]]
    Output: 21

Note:
    1 <= grid.length = grid[0].length <= 50
    0 <= grid[i][j] <= 50
"""

def projectionArea(grid):
    top_view_s = 0
    front_view_s = 0
    side_view_s = 0

    # use two dicts to store the biggest height in each row and column
    front_height_dict = dict()
    side_height_dict = dict()

    # iterate the grid
    for i in range(len(grid)):
        # iterate the row
        for j in range(len(grid[i])):
            # top view s plus one if the height of tower bigger than 0
            if grid[i][j] > 0:
                top_view_s += 1
            # update the biggest height in each column
            if j not in front_height_dict:
                front_height_dict[j] = grid[i][j]
            else:
                if grid[i][j] > front_height_dict[j]:
                    front_height_dict[j] = grid[i][j]
            # update the biggest height in each row
            if i not in side_height_dict:
                side_height_dict[i] = grid[i][j]
            else:
                if grid[i][j] > side_height_dict[i]:
                    side_height_dict[i] = grid[i][j]
    # iterate over the dicts to calculate the area of the front view and the side view
    for h in front_height_dict.values():
        front_view_s += h
    for h in side_height_dict.values():
        side_view_s += h
    # calculate the total view
    total_s = top_view_s + front_view_s + side_view_s
    return total_s

input1 = [[2]]
input2 = [[1,2],[3,4]]
input3 = [[1,0],[0,2]]
input4 = [[1,1,1],[1,0,1],[1,1,1]]
input5 = [[2,2,2],[2,1,2],[2,2,2]]

print(projectionArea(input3))
