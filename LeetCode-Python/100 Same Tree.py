"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

    Input:     1         1
              / \       / \
             2   3     2   3

            [1,2,3],   [1,2,3]

    Output: true

Example 2:

    Input:     1         1
              /           \
             2             2

            [1,2],     [1,null,2]

    Output: false

Example 3:

    Input:     1         1
              / \       / \
             2   1     1   2

            [1,2,1],   [1,1,2]

    Output: false
"""

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def isSameTree(p, q):
    if not p and not q:
        return True
    if not q or not p:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.right, q.right) and isSameTree(p.left, q.left)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)


print(isSameTree(root1, root2))
