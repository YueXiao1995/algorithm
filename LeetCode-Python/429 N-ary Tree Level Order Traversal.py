"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

We should return its level order traversal:

    [
         [1],
         [3,2,4],
         [5,6]
    ]


Note:
    The depth of the tree is at most 1000.
    The total number of nodes is at most 5000.
"""

def levelOrder(root):
    # define a function which can merge two 2-D list
    def merge2DLists(list1,list2):
        l = len(list1)
        for i in range(len(list2)):
            if i < l:
                list1[i] += list2[i]
            else:
                list1.append(list2[i])
        return list1

    # if root is None, return None
    if root == None:
        return None

    # merge its children
    two_d_list = list()
    if len(root.children) != 0:
        for child in root.children:
            two_d_list = merge2DLists(two_d_list, levelOrder(child))
    # return the root and its merged children list
    return [[root.val]] + two_d_list
