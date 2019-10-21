"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:
    Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    Output: true

Example 2:
    Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    Output: false

Constraints:
    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point.
"""
def checkStraightLine(coordinates):
    # if there are only two points, it definitely a lint
    if len(coordinates) == 2:
        return True
    # get the difference of the first two coordinates in horizontal and vertical directions
    dy = coordinates[1][1] - coordinates[0][1]
    dx = coordinates[1][0] - coordinates[0][0]
    # if dy is zero, than this line should be horizontal
    if dy == 0:
        for point in coordinates[2:]:
            if point[1] != coordinates[0][1]:
                return False
        return True
    # if dx is zero, than this line should be vertical
    if dx == 0:
        for point in coordinates[2:]:
            if point[0] != coordinates[0][0]:
                return False
        return True
    # if both of them are not zero, we can use them to form a function y = k * x + d
    if dx != 0 and dy != 0:
        k = dy/dx
        d = coordinates[0][1] - coordinates[0][0] * k
        # check if the rest of points are in this line
        for point in coordinates[2:]:
            if point[1] != point[0] * k + d:
                return False
        return True


input1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
input2 = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]

print(checkStraightLine(input2))

