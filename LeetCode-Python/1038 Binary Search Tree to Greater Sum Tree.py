"""
Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the
sum of the values of the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:
    Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Note:
    The number of nodes in the tree is between 1 and 100.
    Each node will have value between 0 and 100.
    The given tree is a binary search tree.
"""

from binarytree import build
def bstToGst(root):
    # get all of the values in order
    def inorder_traversal(root):
        nums = list()
        if root.left:
            nums.extend(inorder_traversal(root.left))
        nums.append(root.value)
        if root.right:
            nums.extend(inorder_traversal(root.right))
        return nums

    # calculate the new value of the nodes
    nums = inorder_traversal(root)
    sumValue = sum(nums)
    for i in range(len(nums)):
        num = nums[i]
        nums[i] = sumValue
        sumValue -= num

    # modify the tree
    def inorder_traversal_modify(root, nums):
        if root.left:
            nums = inorder_traversal_modify(root.left, nums)
        root.value = nums[0]
        del nums[0]

        if root.right:
            nums = inorder_traversal_modify(root.right, nums)
        return nums
    inorder_traversal_modify(root, nums)
    return root

root = build([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
print(root)
print(bstToGst(root))
