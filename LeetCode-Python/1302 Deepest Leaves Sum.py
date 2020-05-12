"""
Given a binary tree, return the sum of values of its deepest leaves.

Example 1:
    Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
    Output: 15

Constraints:
    The number of nodes in the tree is between 1 and 10^4.
    The value of nodes is between 1 and 100.
"""
from binarytree import build
def deepestLeavesSum(root):
    def dfs(root, deep):
        r = [deep + 1, [root.value]]

        if root.left:
            left_r = dfs(root.left, deep + 1)
            r = left_r

        if root.right:
            right_r = dfs(root.right, deep + 1)

            if right_r[0] > r[0]:
                r = right_r

            elif right_r[0] == r[0]:
                r[1].extend(right_r[1])
        return r

    return sum(dfs(root, 0)[1])



root = build([1,
              2,3,
              4,5,None,6,
              7, None,None,None,None,None,None,8])
print(root)
print(deepestLeavesSum(root))
