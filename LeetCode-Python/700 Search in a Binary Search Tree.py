"""
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2
     / \
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.
"""

from binarytree import build, Node

def searchBST(root, val):
    # return root if the value equal to val
    if root.value == val:
        return root
    else:
        # check if the root has left child
        if root.left:
            r = searchBST(root.left, val)
            # check if the return of left child is not None
            if r:
                return r
        if root.right:
            r = searchBST(root.right, val)
            if r:
                return r
        return None

tree1 = build([4,2,7,1,3])
val1 = 2

print(tree1)
print(searchBST(tree1, val1))
