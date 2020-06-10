"""
节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。

示例1:
     输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
     输出：true

示例2:
     输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
     输出 true

提示：
    节点数量n在[0, 1e5]范围内。
    节点编号大于等于 0 小于 n。
    图中可能存在自环和平行边。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/route-between-nodes-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# dfs
def findWhetherExistsPath(n, graph, start, target):
    connected_point = dict()
    for edge in graph:
        if edge[0] not in connected_point:
            connected_point[edge[0]] = [edge[1]]
        else:
            connected_point[edge[0]].append(edge[1])
    visited = set()
    def dfs(connected_point, start, targt):
        if start not in connected_point:
            return False
        adjacent_points = connected_point[start]
        if len(adjacent_points) == 0:
            return False

        for i in range(len(adjacent_points)):
            if adjacent_points[i] == target:
                return True
            if adjacent_points[i] != visited:
                if dfs(connected_point, adjacent_points[i], target) == True:
                    return True
                visited.add(adjacent_points[i])
        return False
    return dfs(connected_point, start, target)

# dfs
def findWhetherExistsPath2(n, graph, start, target):
    connected_point = dict()
    for edge in graph:
        if edge[0] not in connected_point:
            connected_point[edge[0]] = [edge[1]]
        else:
            connected_point[edge[0]].append(edge[1])
    visited = set()
    queue = [start]
    while len(queue) != 0:
        if queue[0] == target:
            return True
        if queue[0] not in visited and queue[0]in connected_point:
            queue.extend(connected_point[queue[0]])
            visited.add(queue[0])
        del queue[0]
    return False


n = 3
graph = [[0, 1], [0, 2], [1, 2], [1, 2]]
start = 0
target = 2
print(findWhetherExistsPath2(n, graph, start, target))

n = 5
graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]]
start = 0
target = 4
print(findWhetherExistsPath2(n, graph, start, target))
