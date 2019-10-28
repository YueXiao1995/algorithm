"""
Given an m * n matrix M initialized with all 0's and several update operations.

Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.

You need to count and return the number of maximum integers in the matrix after performing all the operations.

Example 1:
    Input:
        m = 3, n = 3
        operations = [[2,2],[3,3]]
    Output:
        4
    Explanation:
        Initially, M =
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

        After performing [2,2], M =
        [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 0]]

        After performing [3,3], M =
        [[2, 2, 1],
         [2, 2, 1],
         [1, 1, 1]]

        So the maximum integer in M is 2, and there are four of it in M. So return 4.

Note:
    The range of m and n is [1,40000].
    The range of a is [1,m], and the range of b is [1,n].
    The range of operations size won't exceed 10,000.
"""

# Memory Limit Exceeded
"""
def maxCount(m, n, ops):
    matrix = []
    for i in range(m):
        matrix.append([0] * n)

    for op in ops:
        a = op[0]
        b = op[1]
        for i in range(a):
            for j in range(b):
                matrix[i][j] += 1
        for row in matrix:
            print(row)

    num_freq = dict()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] in num_freq:
                num_freq[matrix[i][j]] += 1
            else:
                num_freq[matrix[i][j]] = 1
    max = sorted(num_freq.keys())[-1]
    return num_freq[max]
"""
# Memory Limit Exceeded
"""
def maxCount(m, n, ops):
    matrix = []
    for i in range(m):
        matrix.append([0] * n)
    for op in ops:
        for i in range(op[0]):
            for j in range(op[1]):
                matrix[i][j] += 1
    max_value = 0
    for row in matrix:
        row_max = max(row)
        if row_max > max_value:
            max_value = row_max
    num_of_max_value = 0
    for row in matrix:
        num_of_max_value += row.count(max_value)
    return num_of_max_value
"""

def maxCount(m, n, ops):
    min_x = m
    min_y = n
    for op in ops:
        if op[0] < min_x:
            min_x = op[0]
        if op[1] < min_y:
            min_y = op[1]
    return min_y * min_x

m1 = 3
n1 = 3
operations1 = [[2,2],[3,3]]
print(maxCount(m1, n1, operations1))
