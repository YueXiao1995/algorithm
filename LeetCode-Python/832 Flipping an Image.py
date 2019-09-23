"""
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:
    Input:
            [[1,1,0],
            [1,0,1],
            [0,0,0]]
    Output:
            [[1,0,0],
            [0,1,0],
            [1,1,1]]
    Explanation: First reverse each row:
            [[0,1,1],
            [1,0,1],
            [0,0,0]].
    Then, invert the image:
            [[1,0,0],
            [0,1,0],
            [1,1,1]]

Example 2:
    Input:
            [[1,1,0,0],
            [1,0,0,1],
            [0,1,1,1],
            [1,0,1,0]]
    Output:
            [[1,1,0,0],
            [0,1,1,0],
            [0,0,0,1],
            [1,0,1,0]]
    Explanation: First reverse each row:
            [[0,0,1,1],
            [1,0,0,1],
            [1,1,1,0],
            [0,1,0,1]].
    Then invert the image:
            [[1,1,0,0],
            [0,1,1,0],
            [0,0,0,1],
            [1,0,1,0]]
Notes:
    1 <= A.length = A[0].length <= 20
    0 <= A[i][j] <= 1
"""

def flipAndInvertImage(A):
    l = len(A[0])
    # calculate the length of subarray need to be flipped
    if l % 2 == 0:
        flip_l = int(l / 2)
    else:
        flip_l = int(round(l / 2 - 0.5))
    # iterate the image to flip
    for row in A:
        # flip each row
        for i in range(0, flip_l):
            temp = row[i]
            row[i] = row[- 1 - i]
            row[- 1 - i] = temp
    # iterate the image to invert
    for i in range(0, len(A)):
        # invert the row
        for j in range(0, l):
            if A[i][j] == 0:
                A[i][j] = 1
            else:
                A[i][j] = 0
    return A

input1 = [[1,1,0],[1,0,1],[0,0,0]]
input2 = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

print(flipAndInvertImage(input2))
