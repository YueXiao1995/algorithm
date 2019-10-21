"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""

from binarytree import build, Node

def convertBST(root):
    # define a function, return the sum of the tree, add the bigger_sum to the value
    def addSumOfBiggerNumber(root, bigger_sum):
        sum_of_tree = 0
        if root.right:
            sum_of_right_subtree = addSumOfBiggerNumber(root.right, bigger_sum) # get the sum of right subtree
            bigger_sum += sum_of_right_subtree # update the bigger sum
            sum_of_tree += sum_of_right_subtree # update the sum of tree
        # update the sum of the tree
        sum_of_tree += root.value
        # update the bigger sum, since the root always bigger than the left subtree
        root.value += bigger_sum
        if root.left:
            sum_of_tree += addSumOfBiggerNumber(root.left, root.value) # get the sum of the left subtree
        return sum_of_tree

    if root == None:
        return None
    else:
        addSumOfBiggerNumber(root, 0)
        return root

root1 = build([5, 2, 13])
print(root1)
convertBST(root1)
print(root1)
