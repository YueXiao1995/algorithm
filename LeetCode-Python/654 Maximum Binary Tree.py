"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
    Input: [3,2,1,6,0,5]
    Output: return the tree root node representing the following tree:

          6
        /   \
       3     5
        \    /
         2  0
           \
            1
    Note:
    The size of the given array will be in the range [1,1000].
"""

from binarytree import Node
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def constructMaximumBinaryTree(nums):
    if len(nums) == 1:
        node = Node(nums[0])
        return node

    max_value = nums[0]
    max_index = 0

    for i in range(1, len(nums)):
        if nums[i] > max_value:
            max_value = nums[i]
            max_index = i

    node = Node(max_value)

    if max_index == 0:
        right_subarray = nums[1:]
        node.right = constructMaximumBinaryTree(right_subarray)
    elif max_index == len(nums) - 1:
        left_subarray = nums[:-1]
        node.left = constructMaximumBinaryTree(left_subarray)
    else:
        left_subarray = nums[:max_index]
        node.left = constructMaximumBinaryTree(left_subarray)
        right_subarray = nums[max_index+1:]
        node.right = constructMaximumBinaryTree(right_subarray)

    return node

nums = [3,2,1,6,0,5]
print(constructMaximumBinaryTree(nums))
