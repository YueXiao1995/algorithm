"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

from binarytree import build
def sumOfLeftLeaves(root):
    if root == None:
        return 0
    left_child = root.left
    right_child = root.right
    sum_value = 0
    if left_child:
        if not left_child.left and not left_child.right:
            sum_value += left_child.value
        else:
            sum_value += sumOfLeftLeaves(left_child)
    sum_value += sumOfLeftLeaves(right_child)

    return sum_value



root1 = build([3, 9, 20, None, None, 15, 7])
print(root1)
print(sumOfLeftLeaves(root1))
