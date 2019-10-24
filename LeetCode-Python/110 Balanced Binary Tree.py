"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
    Given the following tree [3,9,20,null,null,15,7]:

        3
       / \
      9  20
        /  \
       15   7
    Return true.

Example 2:
    Given the following tree [1,2,2,3,3,null,null,4,4]:

           1
          / \
         2   2
        / \
       3   3
      / \
     4   4
    Return false.
"""

from binarytree import build
def isBalanced(root):
    def dfs(root):
        if root == None:
            return 0
        if not root.left and not root.right:
            return 1
        left_height = dfs(root.left)
        right_height = dfs(root.right)

        if type(left_height) == bool or type(right_height) == bool:
            return False

        if abs(left_height - right_height) > 1:

            return False
        else:
            return max(left_height, right_height) + 1

    if dfs(root) == False:
        return False
    else:
        return True

root1 = build([3, 9, 20, None, None, 15, 7])
print(root1)
print(isBalanced(root1))

root2 = build([1, 2, 2, 3, 3, None, None, 4, 4])
print(root2)
print(isBalanced(root2))

root3 = build([1,2])
print(root3)
print(isBalanced(root3))

print(type(True))
