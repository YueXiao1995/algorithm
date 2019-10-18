"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Note:
    Both of the given trees will have between 1 and 100 nodes.
"""
from binarytree import build, Node

def leafSimilar(root1, root2):
    def getLeaves(root):
        leaves = list()
        if not root.left and not root.right:
            return [root.value]
        else:
            if root.left:
                leaves += getLeaves(root.left)
            if root.right:
                leaves += getLeaves(root.right)
            return leaves

    leaves_of_tree1 = getLeaves(root1)
    leaves_of_tree2 = getLeaves(root2)

    if leaves_of_tree1 == leaves_of_tree2:
        return True
    else:
        return False

root1 = build([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
print(root1)
print(leafSimilar(root1,root1))
