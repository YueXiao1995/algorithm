"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

Example 1:
    Input: [[4,3,8,4],
            [9,5,1,9],
            [2,7,6,2]]
    Output: 1
    Explanation:
        The following subgrid is a 3 x 3 magic square:
            438
            951
            276

        while this one is not:
            384
            519
            762

        In total, there is only one magic square inside the given grid.

Note:
    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    0 <= grid[i][j] <= 15
"""

def numMagicSquaresInside(grid):
    height = len(grid)
    width = len(grid[0])
    if height < 3 or width < 3:
        return 0
    num_of_magic_square = 0
    for i in range(0, height - 2):
        for j in range(0, width - 2):
            top = i
            bottom = i + 2
            left = j
            right = j + 2

            #for h in range(top, bottom + 1):
            #    print(str(grid[h][left]) + str(grid[h][left + 1]) + str(grid[h][left + 2]))
            #print('******')

            # check if is contiguous
            continues = list(range(1, 10))
            for h in range(top, bottom + 1):
                for w in range(left, right + 1):
                    if grid[h][w] in continues:
                        continues.remove(grid[h][w])
                    else:
                        break
            if len(continues) != 0:
                continue

            sum = None

            # check the rows
            is_row_magic = True
            for h in range(top, bottom + 1):
                tem_sum = grid[h][left] + grid[h][left + 1] + grid[h][left + 2]
                if sum == None:
                    sum = tem_sum
                else:
                    if tem_sum != sum:
                        is_row_magic = False
                        break
            if is_row_magic == False:
                continue


            # check the columns
            is_column_magic = True
            for w in range(left, right + 1):
                tem_sum = grid[top][w] + grid[top + 1][w] + grid[top + 2][w]
                if tem_sum != sum:
                    is_column_magic = False
                    break
            if is_column_magic == False:
                continue

            # check the diagonals
            d1_sum = grid[top][left] + grid[top + 1][left + 1] + grid[top + 2][left + 2]
            if d1_sum != sum:
                continue
            d2_sum = grid[bottom][left] + grid[bottom - 1][left + 1] + grid[bottom - 2][left + 2]
            if d2_sum != sum:
                continue
            num_of_magic_square += 1

            for h in range(top, bottom + 1):
                print(str(grid[h][left]) + str(grid[h][left + 1]) + str(grid[h][left + 2]))
    return num_of_magic_square

input1 = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
input2 = [[5,5,5],[5,5,5],[5,5,5]]
input3 = [[3,10,2,3,4],
          [4,5,6,8,1],
          [8,8,1,6,8],
          [1,3,5,7,1],
          [9,4,9,2,9]]

print(numMagicSquaresInside(input3))
