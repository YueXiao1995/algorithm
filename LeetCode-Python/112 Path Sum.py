"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

from binarytree import build
def hasPathSum(root, sum):
    if root == None:
        return False
    if not root.left and not root.right:
        if sum - root.value == 0:
            return True
        else:
            return False
    sum -= root.value
    if root.left:
        if hasPathSum(root.left, sum) == True:
            return True
    if root.right:
        if hasPathSum(root.right, sum) == True:
            return True
    return False

root1 = build([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
print(root1)
sum1 = 22

print(hasPathSum(root1, sum1))
