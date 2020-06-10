"""
实现一个函数，检查一棵二叉树是否为二叉搜索树。

示例 1:
    输入:
        2
       / \
      1   3
    输出: true

示例 2:
    输入:
        5
       / \
      1   4
         / \
        3   6
    输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/legal-binary-search-tree-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from binarytree import build

def isValidBST(root):
    def dfs(root):
        if root == None:
            return 0, 0, True
        if not root.left and not root.right:
            return root.value, root.value, True

        if root.left and root.right:
            left_min, left_max, is_left_balance = dfs(root.left)
            right_min, right_max, is_right_balance = dfs(root.right)

            if is_left_balance and is_right_balance and left_max < root.value and root.value < right_min:
                return min(left_min, right_min), max(left_max, right_max), True
            else:
                return 0, 0, False
        if root.left:
            left_min, left_max, is_left_balance = dfs(root.left)
            if is_left_balance and left_max < root.value:
                return left_min, root.value, True
            else:
                return 0, 0, False
        if root.right:
            right_min, right_max, is_right_balance = dfs(root.right)
            if is_right_balance and root.value < right_min:
                return root.value, right_max, True
            else:
                return 0, 0, False
    return dfs(root)[2]

tree = build([2, 1, 3])
print(tree)
print(isValidBST(tree))

tree = build([5, 1, 4, None, None, 3, 6])
print(tree)
print(isValidBST(tree))

tree = build([10,5,15,None,None,6,20])
print(tree)
print(isValidBST(tree))
