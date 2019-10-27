"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
"""
from binarytree import build

def minDepth(root):
    if root == None:
        return 0
    depth = 0
    if root.left:
        depth = minDepth(root.left)
    if root.right:
        if depth == 0:
            depth = minDepth(root.right)
        else:
            depth = min(depth, minDepth(root.right))
    depth += 1
    return depth

root1 = build([3, 9, 20, None, None, 15, 7])
print(root1)
print(minDepth(root1))

root2 = build([1, None, 2])
print(root2)
print(minDepth(root2))
