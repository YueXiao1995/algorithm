"""
实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。


示例 1:
    给定二叉树 [3,9,20,null,null,15,7]
        3
       / \
      9  20
        /  \
       15   7
    返回 true 。

示例 2:
    给定二叉树 [1,2,2,3,3,null,null,4,4]
          1
         / \
        2   2
       / \
      3   3
     / \
    4   4
    返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-balance-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from binarytree import build
def isBalanced(root):
    if root == None:
        return True
    def heightOfTree(root):
        left_h = 0
        right_h = 0
        if not root.left and not root.right:
            return 1, True
        if root.left:
            left_h, is_balance = heightOfTree(root.left)
            if not is_balance:
                return 0, is_balance
        if root.right:
            right_h, is_balance = heightOfTree(root.right)
            if not is_balance:
                return 0, is_balance

        if abs(left_h - right_h) > 1:
            return max(left_h, right_h) + 1, False
        else:
            return max(left_h, right_h) + 1, True

    _, is_balance = heightOfTree(root)
    return is_balance


tree = build([3,9,20,None,None,15,7])
print(tree)
print(isBalanced(tree))

tree = build([1,2,2,3,3,None, None,4,4])
print(tree)
print(isBalanced(tree))

tree = build([1,2,2,3,3,3,3,4,4,4,4,4,4,None,None,5,5])
print(tree)
print(isBalanced(tree))
