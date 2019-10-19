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
    if root == None:
        return None
    def merge2DLists(list1,list2):
        new_list = list()
        for i in range(max(len(list1), len(list2))):
            sublist = list()
            if i < len(list1):
                sublist += list1[i]
            if i < len(list2):
                sublist += list2[i]
            new_list.append(sublist)
        return new_list

    if len(root.children) == 0:
        return [[root.val]]
    else:
        two_d_list = list()
        for child in root.children:
            two_d_list = merge2DLists(two_d_list, self.levelOrder(child))
        return [[root.val]] + two_d_list
