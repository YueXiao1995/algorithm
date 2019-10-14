"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

    Input:
        Tree 1                     Tree 2
              1                         2
             / \                       / \
            3   2                     1   3
           /                           \   \
          5                             4   7
    Output:
    Merged tree:
             3
            / \
           4   5
          / \   \
         5   4   7

Note:
    The merging process must start from the root nodes of both trees.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# the return value of the method should be a TreeNode
def mergeTrees(t1, t2):
    # if t2 is not exist
    if not t2:
        return t1
    # if t2 exist
    else:
        # if t1 not exist
        if not t1:
            return t2
        # if t1 and t2 both exist, change the value, left and right children of the t1 and return it
        else:
            t1.value += t2.value
            t1.left = mergeTrees(t1.left, t2.left)
            t1.right = mergeTrees(t1.right, t2.right)
            return t1


from binarytree import Node
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

root2 = Node(1)
root2.left = Node(2)

print(mergeTrees(root1, root2))
