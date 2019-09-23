"""
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:
    Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
    Output: true

Example 2:
    Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
    Output: false

Notes:
    Both rectangles rec1 and rec2 are lists of 4 integers.
    All coordinates in rectangles will be between -10^9 and 10^9.
"""

def isRectangleOverlap(rec1, rec2):
    # calculate the width and height of these two rectangles
    width_1 = rec1[2] - rec1[0]
    height_1 = rec1[3] - rec1[1]

    width_2 = rec2[2] - rec2[0]
    height_2 = rec2[3] - rec2[1]

    # calculate the distance between the top side of rec1 and the bottom side of rec2,
    if rec1[3] > rec2[3]:
        max_vertical_diff = abs(rec1[3] - rec2[1])
    else:
        max_vertical_diff = abs(rec2[3] - rec1[1])
    # calculate the distance between the right side of rec1 and the left side of rec2,
    if rec1[2] > rec2[2]:
        max_horizontal_diff = abs(rec1[2] - rec2[0])
    else:
        max_horizontal_diff = abs(rec2[2] - rec1[0])
    # check if the distances are smaller than the sum of the two rectangles' width and height
    if max_horizontal_diff < width_1 + width_2 and max_vertical_diff < height_1 + height_2:
        return True
    else:
        return False


rec1 = [0,0,2,2]
rec2 = [1,1,3,3]

rec3 = [0,0,1,1]
rec4 = [1,0,2,1]

rec5 = [4,0,6,6]
rec6 = [-5,-3,4,2]

print(isRectangleOverlap(rec5, rec6))
