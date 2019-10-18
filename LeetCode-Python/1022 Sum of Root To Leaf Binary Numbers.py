"""
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

Example 1:
    Input: [1,0,1,0,1,0,1]
    Output: 22
    Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Note:
    The number of nodes in the tree is between 1 and 1000.
    node.val is 0 or 1.
    The answer will not exceed 2^31 - 1.
"""

from binarytree import build, Node
def sumRootToLeaf(root):
    # generate all of the paths and store them in a list
    def getPaths(root):
        if not root.left and not root.right:
            return [str(root.value)]
        return_list = list()
        if root.left:
            left_list = getPaths(root.left)
            for i in range(len(left_list)):
                left_list[i] = str(root.value) + left_list[i]
            return_list.extend(left_list)
        if root.right:
            right_list = getPaths(root.right)
            for i in range(len(right_list)):
                right_list[i] = str(root.value) + right_list[i]
            return_list.extend(right_list)
        return return_list
    # convert the binary strings to ints and calculate the sum value
    sum = 0
    for binary in getPaths(root):
        sum += int(binary, 2)

    return sum


root1 = build([1,0,1,0,1,0,1])
print(root1)
print(sumRootToLeaf(root1))
