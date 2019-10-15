"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:
    Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
    Output: 32

Example 2:
    Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
    Output: 23

Note:
    The number of nodes in the tree is at most 10000.
    The final answer is guaranteed to be less than 2^31.
"""

from binarytree import build

def rangeSumBST(root, L, R):
    # define a method which can traverse the tree using a depth first search
    # and get the sum in the same time
    def dfs(root):
        value = 0
        if root != None:
            if root.value >= L and root.value <= R:
                value += root.value
            value += dfs(root.left) + dfs(root.right)
        return value
    # call the dfs function to calculate the sumn
    sum_value = dfs(root)
    return sum_value

root1 = build([10,5,15,3,7,None,18])
L1 = 7
R1 = 15
print(root1)

root2 = build([10,5,15,3,7,13,18,1,None,6])
L2 = 6
R2 = 10

print(rangeSumBST(root2, L2, R2))
