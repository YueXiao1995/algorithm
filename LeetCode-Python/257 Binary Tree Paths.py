"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""

from binarytree import build

def binaryTreePaths(root):
    if root == None:
        return None
    paths = list()
    # get the
    if root.left:
        paths.extend(binaryTreePaths(root.left))
    if root.right:
        paths.extend(binaryTreePaths(root.right))
    l = len(paths)
    # check if this node is a leaf
    if l == 0:
        return [str(root.value)]
    else:
        # for each path string, add the value of this node to the start point
        for i in range(l):
            paths[i] = str(root.value) + "->" + paths[i]
        return paths

root1 = build([1, 2, 3, None, 5])
print(root1)
print(binaryTreePaths(root1))
