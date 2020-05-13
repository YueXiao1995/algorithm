"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:
    Input: [8,5,1,7,10,12]
    Output: [8,5,10,1,7,null,12]

Constraints:
    1 <= preorder.length <= 100
    1 <= preorder[i] <= 10^8
    The values of preorder are distinct.
"""

from binarytree import Node
def bstFromPreorder(preorder):
    node = Node(preorder[0])
    if len(preorder) == 1:
        return node
    right_tree_root = None
    for i in range(1, len(preorder)):
        if preorder[i] > preorder[0]:
            right_tree_root = i
            break
    if right_tree_root != None:
        if right_tree_root >= 2:
            node.left = bstFromPreorder(preorder[1: right_tree_root])
        node.right = bstFromPreorder(preorder[right_tree_root:])
    else:
        node.left = bstFromPreorder(preorder[1:])
    return node

p1 = [8,5,1,7,10,12]
print(bstFromPreorder(p1))
