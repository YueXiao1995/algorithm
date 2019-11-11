"""
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.



Example 1:
    Input: n = 2, m = 3, indices = [[0,1],[1,1]]
    Output: 6
    Explanation: Initial matrix = [[0,0,0],[0,0,0]].
    After applying first increment it becomes [[1,2,1],[0,1,0]].
    The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.

Example 2:
    Input: n = 2, m = 2, indices = [[1,1],[0,0]]
    Output: 0
    Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.


Constraints:
    1 <= n <= 50
    1 <= m <= 50
    1 <= indices.length <= 100
    0 <= indices[i][0] < n
    0 <= indices[i][1] < m
"""

def oddCells(n, m, indices):
    rows = dict()
    for i in range(n):
        rows[i] = 0

    columns = dict()
    for i in range(m):
        columns[i] = 0

    for i in range(len(indices)):
        row = indices[i][0]
        column = indices[i][1]
        rows[row] += 1
        columns[column] += 1

    num_of_odd_values = 0
    for row in rows:
        for column in columns:
            if (rows[row] + columns[column]) % 2 != 0:
                num_of_odd_values += 1

    return num_of_odd_values

n1 = 2
m1 = 3
indices1 = [[0,1],[1,1]]

n2 = 2
m2 = 2
indices2 = [[1,1],[0,0]]

print(oddCells(n1, m1, indices1))
print(oddCells(n2, m2, indices2))
