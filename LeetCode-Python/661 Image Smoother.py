"""
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
    Input:
        [[1,1,1],
         [1,0,1],
         [1,1,1]]
    Output:
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    Explanation:
        For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
        For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
        For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
    The value in the given matrix is in the range of [0, 255].
    The length and width of the given matrix are in the range of [1, 150].
"""

def imageSmoother(M):
    # create a new image
    smoothed_image = list()
    height = len(M)
    width = len(M[0])
    # iterate the image, find the top and bottom border of the surrounding area
    for i in range(0, height):
        top = i - 1
        bottom = i + 1
        # in case the target cell is in the first or the last row of the image
        if top < 0:
            top = 0
        if bottom > height - 1:
            bottom = height - 1
        # create a new row
        smoothed_row = list()
        # iterate each row, find the right and left border of the surrounding area
        for j in range(0, width):
            left = j - 1
            right = j + 1
            # in case the target cell is in the first or the last column of the row
            if left < 0:
                left = 0
            if right > width - 1:
                right = width - 1
            # calculate the number of the cells in surrounding area and itself
            num_of_cells = (bottom - top + 1) * (right - left + 1)
            sum = 0
            # iterate the surrounding area and calculate the sum
            for r in range(top, bottom + 1):
                for c in range(left, right + 1):
                    sum += M[r][c]
            # append the floor(sum value / number of cells) in to the new row
            smoothed_row.append(sum//num_of_cells)
        # append the new row to the new image
        smoothed_image.append(smoothed_row)
    # return the new image
    return smoothed_image


input = [[1,1,1],[1,0,1],[1,1,1]]
input2 = [[1]]
print(imageSmoother(input))
