"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

Example 1:
    Input: [1,1,1,1,1,null,1]
    Output: true

Example 2:
    Input: [2,2,2,5,2]
    Output: false

Note:
    The number of nodes in the given tree will be in the range [1, 100].
    Each node's value will be an integer in the range [0, 99].
"""

from binarytree import build
def isUnivalTree(root):
    def dfs(root):
        # if both children are None
        if not root.left and not root.right:
            return [True, root.value]

        # if one of the child is None
        if not root.left or not root.right:
            if root.left:
                returned_judge = dfs(root.left)
            else:
                returned_judge = dfs(root.right)

            if returned_judge[0]:
                if returned_judge[1] != root.value:
                    returned_judge[0] = False
            return returned_judge

        # if both children are not None
        left_judge = dfs(root.left)
        right_judge = dfs(root.right)
        judge = [False, root.value]
        # check if the left and right subtrees of the root are univalued
        if left_judge[0] and right_judge[0]:
            # check if the tree is univalued
            if left_judge[1] == root.value and right_judge[1] == root.value:
                judge[0] = True
        return judge

    # get the result and return the boolean value
    result = dfs(root)
    return result[0]

root1 = build([1,1,1,1,1,None,1])
root2 = build([2,2,2,5,2])
root3 = build([3,3,3,None,None,2,3])
print(root1)
print(isUnivalTree(root1))

