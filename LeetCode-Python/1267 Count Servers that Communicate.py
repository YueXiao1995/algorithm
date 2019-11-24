"""
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

Example 1:
    Input: grid = [[1,0],[0,1]]
    Output: 0
    Explanation: No servers can communicate with others.

Example 2:
    Input: grid = [[1,0],[1,1]]
    Output: 3
    Explanation: All three servers can communicate with at least one other server.

Example 3:
    Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    Output: 4
    Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m <= 250
    1 <= n <= 250
    grid[i][j] == 0 or 1
"""

def countServers(grid):
    height = len(grid)
    width = len(grid[0])
    rows = [0] * height
    columns = [0] * width

    servers = list()
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                servers.append([i, j])
                rows[i] += 1
                columns[j] += 1
    result = len(servers)
    for server in servers:
        if rows[server[0]] == 1 and columns[server[1]] == 1:
            result -= 1
    return result

grid1 = [[1,0],[0,1]]
print(countServers(grid1))
grid2 = [[1,0],[1,1]]
print(countServers(grid2))
grid3 = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
print(countServers(grid3))
grid4 = [[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]]
print(countServers(grid4))
