"""
Given the following details of a matrix with n columns and 2 rows :

The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
The sum of elements of the 0-th(upper) row is given as upper.
The sum of elements of the 1-st(lower) row is given as lower.
The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is given as an integer array with length n.
Your task is to reconstruct the matrix with upper, lower and colsum.

Return it as a 2-D integer array.

If there are more than one valid solution, any of them will be accepted.

If no valid solution exists, return an empty 2-D array.

Example 1:
    Input: upper = 2, lower = 1, colsum = [1,1,1]
    Output: [[1,1,0],[0,0,1]]
    Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.

Example 2:
    Input: upper = 2, lower = 3, colsum = [2,2,1,1]
    Output: []

Example 3:
    Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
    Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]

Constraints:
    1 <= colsum.length <= 10^5
    0 <= upper, lower <= colsum.length
    0 <= colsum[i] <= 2
"""


def reconstructMatrix(upper, lower, colsum):
    if (upper + lower) != sum(colsum):
        return []


    num = colsum.count(2)
    if num > upper or num > lower:
        return []
    upper -= num
    lower -= num

    row1 = []
    row2 = []
    i = 0
    while i < len(colsum):
        print(upper)
        print(lower)
        if colsum[i] == 0:
            row1.append(0)
            row2.append(0)
        elif colsum[i] == 2:
            row1.append(1)
            row2.append(1)
        else:
            if upper > 0:
                row1.append(1)
                row2.append(0)
                upper -= 1
            else:
                row1.append(0)
                row2.append(1)
                lower -= 1
        i += 1
    return [row1, row2]

upper1 = 2
lower1 = 1
colsum1 = [1,1,1]
print(reconstructMatrix(upper1, lower1, colsum1))

upper2 = 2
lower2 = 3
colsum2 = [2,2,1,1]
print(reconstructMatrix(upper2, lower2, colsum2))

upper3 = 5
lower3 = 5
colsum3 = [2,1,2,0,1,0,1,2,0,1]
print(reconstructMatrix(upper3, lower3, colsum3))

upper4 = 9
lower4 = 2
colsum4 = [0,1,2,0,0,0,0,0,2,1,2,1,2]
print(reconstructMatrix(upper4, lower4, colsum4))
