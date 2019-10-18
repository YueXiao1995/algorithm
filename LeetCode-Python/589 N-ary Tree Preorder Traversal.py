"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its preorder traversal as: [1,3,5,6,2,4].

Note:
    Recursive solution is trivial, could you do it iteratively?
"""
def preorder(root):
    if not root:
        return []
    val_list = [root.val]
    if len(root.children) != 0:
        for child in root.children:
            val_list += preorder(child)
    return val_list
