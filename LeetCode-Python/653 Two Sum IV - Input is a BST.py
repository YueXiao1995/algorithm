"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
    Input:
        5
       / \
      3   6
     / \   \
    2   4   7

    Target = 9

    Output: True

Example 2:
    Input:
        5
       / \
      3   6
     / \   \
    2   4   7

    Target = 28

    Output: False
"""

from binarytree import build, Node
def findTarget(root, k):
    # get all of the values in the tree
    def getAllValuesSmallerThanTarget(root, k):
        value_list = list()
        if root.left:
            value_list += getAllValuesSmallerThanTarget(root.left, k)

        if root.right:
            value_list += getAllValuesSmallerThanTarget(root.right, k)

        value_list.append(root.value)
        return value_list

    value_list = getAllValuesSmallerThanTarget(root, k)

    # two sum algorithm
    diff = set()
    pair = None
    for num in value_list:
        if num in diff:
            pair = {num, k - num}
            break
        diff.add((k - num))
    # if the pair is found, return True
    if pair != None:
        return True
    else:
        return False

root1 = build([5, 3, 6, 2, 4, 7])
target1 = 9

root2 = build([5, 3, 6, 2, 4, 7])
target2 = 28

root3 = build([2,0,3,-4,1])
target3 = -1

print(root3)
print(findTarget(root3, target3))
