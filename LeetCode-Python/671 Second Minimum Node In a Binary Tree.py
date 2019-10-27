"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

    Input:
        2
       / \
      2   5
         / \
        5   7

    Output: 5
    Explanation: The smallest value is 2, the second smallest value is 5.


Example 2:

    Input:
        2
       / \
      2   2

    Output: -1
    Explanation: The smallest value is 2, but there isn't any second smallest value.
"""
from binarytree import build

def findSecondMinimumValue(root):

    def preorderTraversal(root, nums):
        if len(nums) == 2:
            if root.value > nums[1]:
                return nums
            elif root.value < nums[1] and root.value > nums[0]:
                nums[1] = root.value
        elif len(nums) == 1:
            if root.value != nums[0]:
                nums.append(root.value)
        elif len(nums) == 0:
            nums.append(root.value)

        if root.left:
            nums = preorderTraversal(root.left, nums)

        if root.right:
            nums = preorderTraversal(root.right, nums)

        return nums

    result = preorderTraversal(root, [])
    if len(result) == 1:
        return -1
    else:
        return result[1]



root1 = build([2, 2, 5, None, None, 5, 7])
print(root1)
print(findSecondMinimumValue(root1))


root2 = build([2, 2, 2])
print(root2)
print(findSecondMinimumValue(root2))


root3 = build([5, 8, 5])
print(root3)
print(findSecondMinimumValue(root3))

root4 = build([1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1])
print(root4)
print(findSecondMinimumValue(root4))
