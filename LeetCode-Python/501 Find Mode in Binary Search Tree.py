"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

Note:
    If a tree has more than one mode, you can return them in any order.

Follow up:
    Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""

from binarytree import build

def findMode(root):
    def mergeTwoFreqDict(dict1, dict2):
        if len(dict1) > len(dict2):
            small = dict2
            big = dict1
        else:
            small = dict1
            big = dict2

        for num in small:
            if num in big:
                big[num] += small[num]
            else:
                big[num] = small[num]
        return big

    def dfs(root):
        freq = {root.value: 1}
        if root.left:
            left_dict = dfs(root.left)
            freq = mergeTwoFreqDict(freq, left_dict)
        if root.right:
            right_dict = dfs(root.right)
            freq = mergeTwoFreqDict(freq, right_dict)
        return freq

    if root == None:
        return None
    freq_dict = dfs(root)
    modes = list()
    max_freq = 0

    for num in freq_dict:
        freq = freq_dict[num]
        if freq > max_freq:
            max_freq = freq
            modes = [num]
        elif freq == max_freq:
            modes.append(num)
    return modes

root1 = build([1, None, 2, None, None, 2])
print(root1)
print(findMode(root1))
root2 = build([10, 5, None, 5, None, None, None, 5])
print(root2)
print(findMode(root2))

root3 = build([6,2,8,0,4,7,9,None,None,2,6])
print(root3)
print(findMode(root3))

