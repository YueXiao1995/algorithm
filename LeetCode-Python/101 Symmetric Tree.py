"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Note:
    Bonus points if you could solve it both recursively and iteratively.
"""

from binarytree import Node, build

def isSymmetric(root):
    if not root:
        return False
    left = root.left
    right = root.right

    if isMirror(left, right):
        return True
    else:
        return False

def isMirror(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.value == right.value and isMirror(left.right, right.left) and isMirror(left.left, right.right):
        return True
    else:
        return False

root1 = build([1,2,2,3,4,4,3])
root2 = build([1,2,2,None,3,None,3])
root3 = build([2,3,3,4,5,5])
print(root3)
print(isSymmetric(root3))
