"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


Example:
    Input: 3
    Output: [1,3,3,1]
"""

def getRow(rowIndex):
    result = list()
    for i in range(1, rowIndex+2):
        temp = list()
        for j in range(0, i):
            if j == 0 or j == i-1:
                temp.append(1)
            else:
                temp.append(result[i-2][j-1]+result[i-2][j])
        result.append(temp)
    return result[rowIndex]

print(getRow(3))
