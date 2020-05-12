"""
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend in order to collect all apples in the tree starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [fromi, toi] means that exists an edge connecting the vertices fromi and toi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple, otherwise, it does not have any apple.

Example 1:
    Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
    Output: 8
    Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.

Example 2:
    Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
    Output: 6
    Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.

Example 3:
    Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
    Output: 0

Constraints:
    1 <= n <= 10^5
    edges.length == n-1
    edges[i].length == 2
    0 <= fromi, toi <= n-1
    fromi < toi
    hasApple.length == n
"""


def minTime(n, edges, hasApple):
    class TreeNode:
        def __init__(self, data, has_apple):
            self.children = list()
            self.data = data
            self.has_apple = has_apple

    Nodes = list()
    for i in range(n):
        Nodes.append(TreeNode(i, hasApple[i]))

    for edge in edges:
        Nodes[edge[0]].children.append(Nodes[edge[1]])

    def dfs(node):
        has_apple_list = list()

        has_apple_list.append(node.has_apple)
        if len(node.children) == 0:
            return has_apple_list
        else:
            for i in range(len(node.children)):
                l= dfs(node.children[i])
                if l != [False] * len(l):
                    has_apple_list.extend(l)
                    has_apple_list.append(node.has_apple)
            return has_apple_list

    return len(dfs(Nodes[0])) - 1



n1 = 7
edges1 = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple1 = [False,False,True,False,True,True,False]

print(minTime(n1,edges1, hasApple1))

n2 = 7
edges2 = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple2 = [False,False,True,False,False,True,False]
print(minTime(n2, edges2, hasApple2))


n3 = 7
edges3 = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple3 = [False,False,False,False,False,False,False]
print(minTime(n3, edges3, hasApple3))
