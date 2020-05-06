"""
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

Example 1:
    Input: N = 3, paths = [[1,2],[2,3],[3,1]]
    Output: [1,2,3]

Example 2:
    Input: N = 4, paths = [[1,2],[3,4]]
    Output: [1,2,1,2]

Example 3:
    Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
    Output: [1,2,3,4]

Note:
    1 <= N <= 10000
    0 <= paths.size <= 20000
    No garden has 4 or more paths coming into or leaving it.
    It is guaranteed an answer exists.
"""

def gardenNoAdj(N, paths):
    paths_from_each_garden = dict()
    for path in paths:
        if str(path[0]) not in paths_from_each_garden:
            paths_from_each_garden[str(path[0])] = [path[1]]
        else:
            paths_from_each_garden[str(path[0])].append(path[1])

        if str(path[1]) not in paths_from_each_garden:
            paths_from_each_garden[str(path[1])] = [path[0]]
        else:
            paths_from_each_garden[str(path[1])].append(path[0])

    valid_types = [[1,2,3,4] for i in range(N)]
    valid_types[0] = [1]

    for i in range(N):
        connected_gardens = []
        if str(i+1) in paths_from_each_garden:
            connected_gardens = paths_from_each_garden[str(i + 1)]

        for garden in connected_gardens:
            if len(valid_types[garden - 1]) == 1:
                if valid_types[garden - 1][0] in valid_types[i]:
                    valid_types[i].remove(valid_types[garden - 1][0])
        valid_types[i] = [valid_types[i][0]]

    for i in range(N):
        valid_types[i] = valid_types[i][0]

    return valid_types


N1 = 3
paths1 = [[1,2],[2,3],[3,1]]
print(gardenNoAdj(N1, paths1))

N2 = 4
paths2 = [[1,2],[3,4]]
print(gardenNoAdj(N2, paths2))

N3 = 4
paths3 = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
print(gardenNoAdj(N3, paths3))

N4 = 1
paths4 = []
print(gardenNoAdj(N4, paths4))

N5 = 2
paths5 = [[1,2]]
print(gardenNoAdj(N5, paths5))


N6 = 8
paths6 =[[7,4],[3,7],[1,5],[5,4],[7,1],[3,1],[4,3],[6,5]]
print(gardenNoAdj(N6, paths6))
