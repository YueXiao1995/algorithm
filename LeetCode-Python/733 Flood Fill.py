"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
    Input:
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr = 1, sc = 1, newColor = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation:
        From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
        by a path of the same color as the starting pixel are colored with the new color.
        Note the bottom corner is not colored 2, because it is not 4-directionally connected
        to the starting pixel.
Note:
    The length of image and image[0] will be in the range [1, 50].
    The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
    The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""

def floodFill(image, sr, sc, newColor):
    # take three parameters, return all of the start pixels
    def findStartPixels(coordinate, start_pixels, image):
        row = coordinate[0]
        column = coordinate[1]
        # generate four connected pixels
        connected_pixels = [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]
        # iterate the pixels list
        for pixel in connected_pixels:
            # check if the pixel exist
            if pixel[0] in range(len(image)) and pixel[1] in range(len(image[0])):
                # check if the color of the pixel equal to the start pixel
                if image[pixel[0]][pixel[1]] == image[row][column]:
                    # check if the pixel is already in pixels list, if not, update the pixels list
                    if pixel not in start_pixels:
                        start_pixels.add(pixel)
                        start_pixels = findStartPixels(pixel, start_pixels, image)
        return start_pixels
    # get the start pixels list
    start_pixels = findStartPixels((sr, sc), {(sr, sc)}, image)
    # perform a "flood fill", change the values of these start pixels in image
    for pixel in start_pixels:
        image[pixel[0]][pixel[1]] = newColor
    return image


image1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr1 = 1
sc1 = 1
newColor1 = 2

print(floodFill(image1, sr1, sc1, newColor1))
