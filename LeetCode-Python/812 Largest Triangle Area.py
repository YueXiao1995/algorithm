"""
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
    Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    Output: 2
    Explanation:
    The five points are show in the figure below. The red triangle is the largest.

Notes:
    3 <= points.length <= 50.
    No points will be duplicated.
     -50 <= points[i][j] <= 50.
    Answers within 10^-6 of the true value will be accepted as correct.
"""
def largestTriangleArea(points):
    max_S = 0
    num_of_points = len(points)
    # iterate all of the possible three points groups
    for i in range(num_of_points):
        for j in range(i + 1, num_of_points):
            for k in range(j + 1, num_of_points):
                # use these three points to calculate the area of the triangle
                p1 = points[i]
                p2 = points[j]
                p3 = points[k]
                S = 0.5 * abs(((p1[0] * (p2[1] - p3[1])) + (p2[0] * (p3[1] - p1[1])) + (p3[0] * (p1[1] - p2[1]))))
                # update the max area
                if S > max_S:
                    max_S = S
    return max_S

points1 = [[0,0],[0,1],[1,0],[0,2],[2,0]]
print(largestTriangleArea(points1))
