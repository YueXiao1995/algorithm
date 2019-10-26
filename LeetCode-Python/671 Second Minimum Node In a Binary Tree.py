"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

    Input:
        2
       / \
      2   5
         / \
        5   7

    Output: 5
    Explanation: The smallest value is 2, the second smallest value is 5.


Example 2:

    Input:
        2
       / \
      2   2

    Output: -1
    Explanation: The smallest value is 2, but there isn't any second smallest value.
"""
from binarytree import build
def findSecondMinimumValue(root):
    def inorderTraversal(root):
        return_list = list()
        if root.left:
            left_return = inorderTraversal(root.left)
            if len(left_return) == 2:
                return left_return
            else:
                return_list.extend(left_return)

        if len(return_list) == 0:
            return_list.append(root.value)
        elif len(return_list) == 1 and root.value != return_list[0]:
            return_list.append(root.value)
            return sorted(return_list)

        if root.right:
            right_return = inorderTraversal(root.right)
            for value in right_return:
                if value > root.value:
                    return_list.append(value)
                    return return_list
        return return_list
    if root == None:
        return None
    else:
        result = inorderTraversal(root)
        print(result)
        if len(result) == 1:
            return -1
        else:
            return result[-1]

def findSecondMinimumValue2(root):
    def preorderTraversal(root):
        if left_return ==


root1 = build([2, 2, 5, None, None, 5, 7])
print(root1)
print(findSecondMinimumValue(root1))


root2 = build([2, 2, 2])
print(root2)
print(findSecondMinimumValue(root2))


root3 = build([5, 8, 5])
print(root3)
print(findSecondMinimumValue(root3))

root4 = build([1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1])
print(root4)
print(findSecondMinimumValue(root4))
