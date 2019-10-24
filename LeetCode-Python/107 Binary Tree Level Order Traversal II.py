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

def levelOrderBottom(root):
    # a function to merge two 2-d lists, for example:
    # a = [[1], [2], [3, 4]],  b = [[5], [6]]
    # merge(a, b) = [[1], [2, 5], [3, 4, 6]]
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

    children_list = list()
    # put the right child and left child into a list
    children = [root.left, root.right]
    # get the 2-d list of its children
    for child in children:
        child_list = levelOrderBottom(child)
        if child_list != None:
            children_list = merge(children_list, child_list)

    return children_list + [[root.value]]

root1 = build([3, 9, 20, None, None, 15, 7])
print(root1)
print(levelOrderBottom(root1))
