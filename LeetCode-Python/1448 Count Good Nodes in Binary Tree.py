"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:
    Input: root = [3,1,4,3,null,1,5]
    Output: 4
    Explanation: Nodes in blue are good.
    Root Node (3) is always a good node.
    Node 4 -> (3,4) is the maximum value in the path starting from the root.
    Node 5 -> (3,4,5) is the maximum value in the path
    Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
    Input: root = [3,3,null,4,2]
    Output: 3
    Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
    Input: root = [1]
    Output: 1
    Explanation: Root is considered as good.

Constraints:
    The number of nodes in the binary tree is in the range [1, 10^5].
    Each node's value is between [-10^4, 10^4].
"""
from binarytree import build
def goodNodes(root):
    def dfs(root, max_ancestor=None):
        good_node_count = 0
        if max_ancestor == None:
            good_node_count += 1
            max_ancestor = root.value
        else:
            if root.value >= max_ancestor:
                good_node_count += 1
                max_ancestor = root.value

        if not root.left and not root.right:
            return good_node_count

        if root.left:
            good_node_count += dfs(root.left, max_ancestor)
        if root.right:
            good_node_count += dfs(root.right, max_ancestor)

        return good_node_count

    return dfs(root)


root = build([3,1,4,3,None,1,5])
print(root)
print(goodNodes(root))

root = build([3,3,None,4,2])
print(root)
print(goodNodes(root))

root = build([1])
print(root)
print(goodNodes(root))
