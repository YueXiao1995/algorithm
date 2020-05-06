def reverseBinary(num):
    binary_num = bin(num)[2:]
    new_binary_num = binary_num[::-1]
    base = 1
    new_num = 0
    for i in range(len(new_binary_num)):
        new_num += int(new_binary_num[-i-1]) * base
        base *= 2
    return new_num


num1 = 10
num2 = 43261596
print(reverseBinary(num2))


def shortestPath(matrix):
    h = len(matrix)
    paths = list()
    paths.append(matrix[0])
    paths_end_index = list()
    paths_end_index.append(0)

    for i in range(1, h):
        new_paths = list()
        new_paths_end_index = list()

        for j in range(len(paths)):
            index = paths_end_index[j]

            if index != 0:
                new_paths.append(paths[j] + [matrix[i][index - 1]])
                new_paths_end_index.append(index - 1)

            new_paths.append(paths[j] + [matrix[i][index]])
            new_paths_end_index.append(index)

            new_paths.append(paths[j] + [matrix[i][index + 1]])
            new_paths_end_index.append(index + 1)

        paths = new_paths
        paths_end_index = new_paths_end_index

    lengths = list()

    for path in paths:
        lengths.append(sum(path))

    min_path = min(lengths)
    for i in range(len(paths)):
        if lengths[i] == min_path:
            print(paths[i])

    return min(lengths)

matrix1 = [[2],
           [1, 4],
           [6, 2, 7],
           [4, 1, 7, 3]]

matrix2 = [[2],
           [2, 2],
           [2, 5, 2],
           [2, 1, 5, 3],
           [3, 2, 1, 5, 3],
           [4, 10,10,10, 1, 10],
           [9, 7, 10,15, 3, 6, 5]]


print(shortestPath(matrix2))


def water(heights):
    unique_heights = sorted(list(set(heights)))
    if 0 in unique_heights:
        unique_heights.remove(0)
    water = 0
    pillars = list(range(len(heights)))
    for i in range(len(unique_heights)):
        new_pillars = list()
        for j in range(len(pillars)):
            if heights[pillars[j]] >= unique_heights[i]:
                new_pillars.append(pillars[j])
        pillars = new_pillars
        if len(pillars) > 1:
            water += (pillars[-1] - pillars[0] + 1) - len(pillars)

    return water

heights1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
heights2 = [3,1,3,0,5,4,5,0,3,2,1,3]
print(water(heights2))

