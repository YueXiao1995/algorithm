"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

"""

from binarytree import build
root1 = build([3, 9, 20, None, None, 15, 7])
print(root1)
def levelOrderBottom(root):
    def merge(list1, list2):
        new_2d_list = list()
        l1 = len(list1)
        l2 = len(list2)
        for i in range(max(l1, l2)):
            new_list = list()
            if i < l1:
                new_list.extend(list1[-1 -i])
            if i < l2:
                new_list.extend(list2[-1-i])
            new_2d_list = [new_list] + new_2d_list
        return new_2d_list

    if root == None:
        return None

    return_list = list()
    children = [root.left, root.right]
    for child in children:
        child_list = levelOrderBottom(child)
        if child_list != None:
            return_list = merge(return_list, child_list)
    return return_list + [[root.value]]


print(levelOrderBottom(root1))
