"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""


from binarytree import build


def diameterOfBinaryTree(root):
    def heightOfsubtrees(root):
        if not root.left and not root.right:
            return [0, 0, 0]
        # [left, right, maxlength]
        heights = [0, 0, 0]
        if root.left:
            left_return = heightOfsubtrees(root.left)
            heights[0] += max(left_return[0], left_return[1]) + 1
            heights[2] = max(heights[2], left_return[2])
        if root.right:
            right_return = heightOfsubtrees(root.right)
            heights[1] += max(right_return[0], right_return[1]) + 1
            heights[2] = max(heights[2], right_return[2])
        heights[2] = max(heights[2], heights[0] + heights[1])
        return heights

    if root == None:
        return 0
    return heightOfsubtrees(root)[2]

root1 = build([1, 2, 3, 4, 5])
print(root1)
print(diameterOfBinaryTree(root1))
