"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

Example 1:
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    Output: 2
    Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Note:
    All of the nodes' values will be unique.
    p and q are different and both values will exist in the BST.
"""
from binarytree import build

def lowestCommonAncestor(root, p, q):
    return_list = [False, False]
    if root.left:
        left_return = lowestCommonAncestor(root.left, p, q)
        if type(left_return) != list:
            return left_return
        else:
            for i in range(2):
                if left_return[i] == True:
                    return_list[i] = True
    if root.right:
        right_return = lowestCommonAncestor(root.right, p, q)
        if type(right_return) != list:
            return right_return
        else:
            for i in range(2):
                if right_return[i] == True:
                    return_list[i] = True
    if root.value == p:
        return_list[0] = True

    if root.value == q:
        return_list[1] = True
        
    if return_list[0] == True and return_list[1] == True:
        return root
    else:
        return return_list

root1 = build([6, 2, 8, 0, 4, 7, 9, None, None,3, 5])
p1 = 2
q1 = 8

root2 = build([6, 2, 8, 0, 4, 7, 9, None, None,3, 5])
p2 = 2
q2 = 4

print(root1)
print(lowestCommonAncestor(root1, p2, q2))
