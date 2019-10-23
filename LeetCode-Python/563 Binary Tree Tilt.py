"""
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
    Input:
             1
           /   \
          2     3
    Output: 1
    Explanation:
    Tilt of node 2 : 0
    Tilt of node 3 : 0
    Tilt of node 1 : |2-3| = 1
    Tilt of binary tree : 0 + 0 + 1 = 1

Note:
    The sum of node values in any subtree won't exceed the range of 32-bit integer.
    All the tilt values won't exceed the range of 32-bit integer.
"""

from binarytree import build
def findTilt(root):

    def calculateTilt(root):
        if not root.left and not root.right:
            # if the node is a leaf,return tilt 0 and its value
            return [0, root.value]
        # init tilt and the sum of the right and left subtrees
        tilt = 0
        sum_of_left_subtree = 0
        sum_of_right_subtree = 0
        # check it the left subtree exist
        if root.left:
            # call the function to get a returned list
            left_return = calculateTilt(root.left)
            # update the tilt
            tilt += left_return[0]
            # update the sum of the left subtree
            sum_of_left_subtree = left_return[1]
        # check if the right subtree exist
        if root.right:
            right_return = calculateTilt(root.right)
            tilt += right_return[0]
            sum_of_right_subtree = right_return[1]
        # calculate the tilt of this root, and add it to the total tilt sum
        tilt += abs(sum_of_right_subtree - sum_of_left_subtree)
        # return a list [total tilt, sum of the tree]
        return [tilt, sum_of_right_subtree + sum_of_left_subtree + root.value]

    if root == None:
        return 0
    return calculateTilt(root)[0]


root1 = build([1, 2, 3])
print(root1)
print(findTilt(root1))
root2 = build([1, None, 2])
print(root2)
print(findTilt(root2))
