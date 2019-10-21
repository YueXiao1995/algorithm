"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
    Input:
        3
       / \
      9  20
        /  \
       15   7
    Output: [3, 14.5, 11]
    Explanation:
        The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note:
    The range of node's value is in the range of 32-bit signed integer.
"""

from binarytree import build, Node

def averageOfLevels(root):
    # a function which can merge two 2-d list
    def merge2DLists(list1,list2):
        l = len(list1)
        for i in range(len(list2)):
            if i < l:
                list1[i] += list2[i]
            else:
                list1.append(list2[i])
        return list1
    #
    def valuesInEachLevel(root):
        two_d_list = list()
        if root.left:
            two_d_list = valuesInEachLevel(root.left)
        if root.right:
            two_d_list = merge2DLists(two_d_list, valuesInEachLevel(root.right))
        return [[root.value]] + two_d_list

    values = valuesInEachLevel(root)
    for i in range(len(values)):
        values[i] = float(sum(values[i]))/len(values[i])
    return values



root1 = build([3, 9, 20, None, None, 15, 7])
print(root1)

print(averageOfLevels(root1))
