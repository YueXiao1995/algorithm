"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
    Input: [[0,0],[1,0],[2,0]]
    Output: 2
    Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""
def numberOfBoomerangs(points):
    num_of_boomerangs = 0
    distances_matrix = list()
    l = len(points)
    for i in range(0, l):
        distances_freq = dict()
        distances_list = list()

        for j in range(i, l):
            distence = pow(points[j][0]-points[i][0], 2) + pow(points[j][1]-points[i][1], 2)
            if distence != 0:
                if distence in distances_freq:
                    distances_freq[distence] += 1
                else:
                    distances_freq[distence] = 1
            distances_list.append(distence)
        distances_matrix.append(distances_list)

        for j in range(0, i):
            if distances_matrix[j][i-j] in distances_freq:
                distances_freq[distances_matrix[j][i-j]] += 1
            else:
                distances_freq[distances_matrix[j][i - j]] = 1

        for d in distances_freq:
            num_of_boomerangs += 2 * sum(range(distances_freq[d]))
    return num_of_boomerangs


input1 = [[0,0],[1,0],[2,0]]
input2 = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8]]
input3 = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
print(numberOfBoomerangs(input2))
