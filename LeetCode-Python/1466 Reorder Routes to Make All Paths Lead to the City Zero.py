"""
There are n cities numbered from 0 to n-1 and n-1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [a, b] represents a road from city a to b.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach the city 0 after reorder.

Example 1:
    Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    Output: 3
    Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:
    Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
    Output: 2
    Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:
    Input: n = 3, connections = [[1,0],[2,0]]
    Output: 0

Constraints:
    2 <= n <= 5 * 10^4
    connections.length == n-1
    connections[i].length == 2
    0 <= connections[i][0], connections[i][1] <= n-1
    connections[i][0] != connections[i][1]
"""
# Time Limit Exceeded
def minReorder(n, connections):
    roads = dict()
    reversed_roads = dict()
    for c in connections:
        if c[0] not in roads:
            roads[c[0]] = [c[1]]
        else:
            roads[c[0]].append(c[1])

        if c[1] not in reversed_roads:
            reversed_roads[c[1]] = [c[0]]
        else:
            reversed_roads[c[1]].append(c[0])

    reorient = 0
    current_layer = [0]
    while len(current_layer) != 0:

        next_layer = list()
        for start in current_layer:
            if start in roads.keys():
                next_layer.extend(roads[start])
                reorient += len(roads[start])
                for end in roads[start]:
                    reversed_roads[end].remove(start)
                    if len(reversed_roads[end]) == 0:
                        reversed_roads.pop(end)
            if start in reversed_roads.keys():
                next_layer.extend(reversed_roads[start])
                for end in reversed_roads[start]:
                    roads[end].remove(start)
                    if len(roads[end]) == 0:
                        roads.pop(end)

        current_layer = next_layer
    return reorient

# Time Limit Exceeded
def minReorder2(n, connections):
    roads = dict()
    reversed_roads = dict()
    for c in connections:
        if c[0] not in roads:
            roads[c[0]] = [c[1]]
        else:
            roads[c[0]].append(c[1])

        if c[1] not in reversed_roads:
            reversed_roads[c[1]] = [c[0]]
        else:
            reversed_roads[c[1]].append(c[0])

    visited = set()
    reorient = 0
    current_layer = [0]
    visited.add(0)
    while len(current_layer) != 0:
        next_layer = list()
        for start in current_layer:
            if start in roads.keys():
                for city in roads[start]:
                    if city not in visited:
                        next_layer.append(city)
                        visited.add(city)
                        reorient += 1
            if start in reversed_roads.keys():
                for city in reversed_roads[start]:
                    if city not in visited:
                        next_layer.append(city)
                        visited.add(city)

        current_layer = next_layer
    return reorient



n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(minReorder2(n, connections))

n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]
print(minReorder2(n, connections))

n = 3
connections = [[1,0],[2,0]]
print(minReorder2(n, connections))

