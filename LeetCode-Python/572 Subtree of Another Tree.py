"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

from binarytree import build
def isSubtree(s, t):

    def getPreorderList(root):
        value_list = [root.value]
        node_list = [root]
        if root.left:
            left_value_list, left_node_list = getPreorderList(root.left)
            value_list += left_value_list
            node_list += left_node_list
        if root.right:
            right_value_list, right_node_list = getPreorderList(root.right)
            value_list += right_value_list
            node_list += right_node_list
        return value_list, node_list

    def ifcontains(list1, target_list):
        l1 = len(list1)
        l2 = len(target_list)
        start_points = list()
        for i in range(l1 - l2 + 1):
            if list1[i:i + l2] == target_list:
                start_points.append(i)
        if len(start_points) == 0:
            return False, []
        else:
            return True, start_points

    s_value, s_node = getPreorderList(s)
    t_value, t_node = getPreorderList(t)
    is_contain, start_points = ifcontains(s_value, t_value)
    if is_contain:
        for point in start_points:
            s_subtree_value, s_subtree_node = getPreorderList(s_node[point])
            if s_subtree_value == t_value:
                return True
    return False




s1 = build([3, 4, 5, 1, 2])
t1 = build([4, 1, 2])
print(isSubtree(s1, t1))

s2 = build([3, 4, 5, 1, 2, None, None, None, None, 0])
print(s2)
t2 = build([4, 1, 2])
print(isSubtree(s2, t2))

s3 = build([1, 1])
t3 = build([1])
print(s3)
print(isSubtree(s3, t3))
