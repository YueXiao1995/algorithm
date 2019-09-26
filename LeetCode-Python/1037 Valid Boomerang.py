"""
A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

Example 1:
    Input: [[1,1],[2,3],[3,2]]
    Output: true

Example 2:
    Input: [[1,1],[2,2],[3,3]]
    Output: false

Note:
    points.length == 3
    points[i].length == 2
    0 <= points[i][j] <= 100
"""

def isBoomerang(points):
    # get the three points
    p1 = points[0]
    p2 = points[1]
    p3 = points[2]
    # calcuate the area of the triangle
    S = 0.5 * abs(((p1[0] * (p2[1] - p3[1])) + (p2[0] * (p3[1] - p1[1])) + (p3[0] * (p1[1] - p2[1]))))
    # if the area bigger than 0, return True
    if S > 0:
        return True
    else:
        return False

input1 = [[1,1],[2,3],[3,2]]
input2 = [[1,1],[2,2],[3,3]]
print(isBoomerang(input2))
