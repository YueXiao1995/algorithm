"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
    Given the sorted array: [-10,-3,0,5,9],

    One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

          0
         / \
       -3   9
       /   /
     -10  5
"""


from binarytree import build, Node

def sortedArrayToBST(nums):
    if len(nums) == 0:
        return None
    # get the middle index of the nums list
    l = len(nums)
    root_index = l // 2
    # generate a TreeNode as the root
    root = Node(nums[root_index])
    # generate the left subtree
    root.left = sortedArrayToBST(nums[0:root_index])
    # generate the right subtree
    root.right = sortedArrayToBST(nums[root_index + 1:])
    return root

input1 = [-10, -3, 0, 5, 9]
print(sortedArrayToBST(input1))
