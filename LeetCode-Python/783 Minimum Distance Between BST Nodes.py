"""
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :
    Input: root = [4,2,6,1,3,null,null]
    Output: 1
    Explanation:
    Note that root is a TreeNode object, not an array.

    The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

              4
            /   \
          2      6
         / \
        1   3

    while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.

Note:
    The size of the BST will be between 2 and 100.
    The BST is always valid, each node's value is an integer, and each node's value is different.
"""

def minDiffInBST(root):
    def dfs(root):
        elements = list()
        if root.left:
            elements.extend(dfs(root.left))
        elements.append(root.value)
        if root.right:
            elements.extend(dfs(root.right))
        return elements

    elements = dfs(root)
    min_abs_diff = None
    for i in range(len(elements) - 1):
        abs_diff = abs(elements[i + 1] - elements[i])
        if min_abs_diff == None:
            min_abs_diff = abs_diff
        else:
            if abs_diff < min_abs_diff:
                min_abs_diff = abs_diff
    return min_abs_diff

from binarytree import build
root1 = build([4,2,6,1,3,None,None])
print(root1)

print(minDiffInBST(root1))

root2 = build([27,None,34,None, None, None,58, None, None, None, None, None, None, 50, None, None, None, None, None, None, None, None, None, None, None, None, None, 44])
print(root2)
print(minDiffInBST(root2))

root3 = build([90, 69, None, 49, 89, None, None, None, 52])
print(root3)
print(minDiffInBST(root3))
