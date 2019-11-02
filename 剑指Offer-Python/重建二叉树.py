"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


from binarytree import Node

def reConstructBinaryTree(pre, tin):
    # the first element in pre list is the root
    root = Node(pre[0])

    # find the index of the root value in tin list
    root_index = 0
    for i in range(len(tin)):
        if tin[i] == root.value:
            root_index = i
    # remove the root from the pre list
    del pre[0]

    # build left subtree
    if root_index > 0:
        left = tin[:root_index]
        root.left = reConstructBinaryTree(pre[:len(left)+1], left)
        # remove the elements of left subtree in pre list
        pre = pre[len(left):]

    # build right subtree
    if root_index < len(tin) - 1:
        right = tin[root_index + 1:]
        root.right = reConstructBinaryTree(pre, right)

    return root


pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]

print(reConstructBinaryTree(pre, tin))
