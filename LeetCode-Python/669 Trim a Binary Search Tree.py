"""
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:

Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:

Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1

"""

from binarytree import build, Node
def trimBST(root, L, R):
    # check if root smaller than the L,
    if root.value < L:
        # check it if has right child, move to the right child.
        if root.right:
            return trimBST(root.right, L, R)
        # if not, than return null, means this subtree dont have any node with value between L and R
        else:
            return None
    # if root bigger than the R, move to its left child, if it has
    if root.value > R:
        if root.left:
            return trimBST(root.left, L, R)
        else:
            return None
    # if the root is in the range, now
    if root.value >= L and root.value <= R:
        # if it has the left child, update it
        if root.left:
            root.left = trimBST(root.left, L, R)
        # if if has the right child, update it
        if root.right:
            root.right = trimBST(root.right, L, R)
        return root

root1 = build([1, 0, 2])
L1 = 1
R1 = 2
print(root1)
print(trimBST(root1, L1, R1))

root2 = build([3,0,4,None,2,None,None,None, None, None, 1])
print(root2)
L2 = 1
R2 = 3
print(trimBST(root2, L2, R2))
