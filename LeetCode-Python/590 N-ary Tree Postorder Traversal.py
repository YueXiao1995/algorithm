"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its postorder traversal as: [5,6,3,2,4,1].


Note:
    Recursive solution is trivial, could you do it iteratively?
"""

def postorder(root):
    if not root:
        return []
    val_list = list()
    if len(root.children) != 0:
        for child in root.children:
            val_list += postorder(child)
    val_list += [root.val]
    return val_list
