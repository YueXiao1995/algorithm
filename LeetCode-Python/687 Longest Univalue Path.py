"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

Example 1:
    Input:

                  5
                 / \
                4   5
               / \   \
              1   1   5
    Output: 2

Example 2:
    Input:

                  1
                 / \
                4   5
               / \   \
              4   4   5
    Output: 2

Note:
    The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""

from binarytree import build
def longestUnivaluePath(root):
    def findPathWithSameValue(root):
        the_value = root.value
        return_list = [root.value, [root.value], 0]

        if not root.right and not root.left:
            return return_list

        if root.left and not root.right:
            left_return = findPathWithSameValue(root.left)
            if left_return[0] == the_value:
                return_list[1] = left_return[1] + return_list[1]
                return_list[2] = left_return[2]
            else:
                return_list[2] = max(left_return[2], len(left_return[1]) - 1)
            return return_list

        if root.right and not root.left:
            right_return = findPathWithSameValue(root.right)
            if right_return[0] == the_value:
                return_list[1] = right_return[1] + return_list[1]
                return_list[2] = right_return[2]
            else:
                return_list[2] = max(right_return[2], len(right_return[1]) - 1)
            return return_list

        if root.right and root.left:
            left_return = findPathWithSameValue(root.left)
            right_return = findPathWithSameValue(root.right)

            if left_return[0] != the_value and right_return[0] != the_value:
                return_list[2] = max(left_return[2], right_return[2], len(right_return[1]) - 1, len(left_return[1]) - 1)

            if left_return[0] == the_value and right_return[0] == the_value:
                if len(left_return[1]) > len(right_return[1]):
                    return_list[1] = left_return[1] + return_list[1]
                else:
                    return_list[1] = right_return[1] + return_list[1]
                return_list[2] = max(left_return[2], right_return[2], len(left_return[1]) + len(right_return[1]))

            if left_return[0] == the_value and right_return[0] != the_value:
                return_list[1] = left_return[1] + return_list[1]
                return_list[2] = max(left_return[2], right_return[2], len(right_return[1]) - 1)

            if left_return[0] != the_value and right_return[0] == the_value:
                return_list[1] = right_return[1] + return_list[1]
                return_list[2] = max(left_return[2], right_return[2], len(left_return[1]) - 1)

            return return_list

    if root == None:
        return 0
    result = findPathWithSameValue(root)
    return max(len(result[1]) - 1, result[2])

root1 = build([5, 4, 5, 1, 1, None, 5])
print(root1)
print(longestUnivaluePath(root1))

root2 = build([1, 4, 5, 4, 4, None, 5])
print(root2)
print(longestUnivaluePath(root2))

root3 = build([1, 2])
print(longestUnivaluePath(root3))

root4 = build([1,2, 3, 4, 2])
print(root4)
print(longestUnivaluePath(root4))

root5 = build([1, None, 1, None, None, 1, 1, None, None, None, None, 1, 1, 1])
print(root5)
print(longestUnivaluePath(root5))
