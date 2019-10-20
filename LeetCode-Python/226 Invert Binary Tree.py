"""
Invert a binary tree.

Example:
    Input:

         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    Output:

         4
       /   \
      7     2
     / \   / \
    9   6 3   1
    Trivia:
    This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""
from binarytree import build, Node

def invertTree(root):
    if not root:
        return None
    # exchange the left child and right child
    temp = root.left
    root.left = root.right
    root.right = temp
    # if the right child is not None, invert the subtree
    if root.right:
        invertTree(root.right)
    if root.left:
        invertTree(root.left)
    return root

root1 = build([4, 2, 7, 1, 3, 6, 9])
print(root1)

print(invertTree(root1))
