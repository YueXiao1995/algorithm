"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \
    1   3
         \
          4
"""

from binarytree import build, Node

def insertIntoBST(root, val):
    if root.value > val:
        if  root.left == None:
            newNode = Node(val)
            root.left = newNode
        else:
            insertIntoBST(root.left, val)
    else:
        if  root.right == None:
            newNode = Node(val)
            root.right = newNode
        else:
            insertIntoBST(root.right, val)
    return root

root1 = build([4, 2, 7, 1, 3])
print(root1)
print(insertIntoBST(root1, 5))

a = (1/2) ** 16
print(a)
