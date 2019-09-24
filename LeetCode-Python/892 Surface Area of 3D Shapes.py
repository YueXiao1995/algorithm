"""
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

Example 1:
    Input: [[2]]
    Output: 10

Example 2:
    Input: [[1,2],[3,4]]
    Output: 34

Example 3:
    Input: [[1,0],[0,2]]
    Output: 16

Example 4:
    Input: [[1,1,1],[1,0,1],[1,1,1]]
    Output: 32

Example 5:
    Input: [[2,2,2],[2,1,2],[2,2,2]]
    Output: 46

Note:
    1 <= N <= 50
    0 <= grid[i][j] <= 50
"""

def surfaceArea(grid):
    # based on the grid, store the coordinate of all the 1*1*1 cubes into a set
    cubes = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for k in range(grid[i][j]):
                # store the coordinate in the form of a string, which can be stored in set
                coordinate = str(i) + ',' + str(j) + ',' + str(k)
                cubes.add(coordinate)
    # calculate the total surface area
    surface_s = 0
    # iterate the cubes in set
    for cube in cubes:
        cube = cube.split(',')
        # generate the coordinate of the 6 surrounding cubes
        top = cube[0] + ',' + cube[1] + ',' + str(int(cube[2]) + 1)
        bottom = cube[0] + ',' + cube[1] + ',' + str(int(cube[2]) - 1)
        front = str(int(cube[0]) + 1) + ',' + cube[1] + ',' + cube[2]
        back = str(int(cube[0]) - 1) + ',' + cube[1] + ',' + cube[2]
        left = cube[0] + ',' + str(int(cube[1]) + 1) + ',' + cube[2]
        right = cube[0] + ',' + str(int(cube[1]) - 1) + ',' + cube[2]
        surrounding_cubes = [top, bottom, front, back, left, right]
        # check if these cubes are exist in cubes set
        for cube in surrounding_cubes:
            if cube not in cubes:
                # if not, surface area plus one
                surface_s += 1
    return surface_s

input1 = [[2]]
input2 = [[1,2],[3,4]]
input3 = [[1,0],[0,2]]
input4 = [[1,1,1],[1,0,1],[1,1,1]]
input5 = [[2,2,2],[2,1,2],[2,2,2]]

print(surfaceArea(input5))
