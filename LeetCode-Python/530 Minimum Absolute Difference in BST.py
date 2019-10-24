"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:
    Input:

       1
        \
         3
        /
       2

    Output:
    1

    Explanation:
    The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

Note: There are at least two nodes in this BST.
"""

from binarytree import build
def getMinimumDifference(root):
    # store all of the values in a list
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
        abs_diff = abs(elements[i] - elements[i + 1])
        if min_abs_diff == None:
            min_abs_diff = abs_diff
        else:
            if abs_diff < min_abs_diff:
                min_abs_diff = abs_diff
    return min_abs_diff

root1 = build([1, None, 3, None, None, 2])
print(root1)
print(getMinimumDifference(root1))
