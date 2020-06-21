"""
检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。

如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。

示例1:
     输入：t1 = [1, 2, 3], t2 = [2]
     输出：true

示例2:
     输入：t1 = [1, null, 2, 4], t2 = [3, 2]
     输出：false

提示：
    树的节点数目范围为[0, 20000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-subtree-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from binarytree import build, Node


def checkSubTree(t1, t2):
    def dfs(root):
        if root == None:
            return []
        left_child_tree = [None]
        right_child_tree = [None]
        if root.left:
            left_child_tree = dfs(root.left)
        if root.right:
            right_child_tree = dfs(root.right)
        return [root.value] + left_child_tree + right_child_tree

    t2 = dfs(t2)
    def dfs2(root, taragt):
        if root == None:
            if taragt == []:
                return True
            else:
                return False
        left_child_tree = [None]
        right_child_tree = [None]
        if root.left:
            left_child_tree = dfs2(root.left, t2)
            if isinstance(left_child_tree, bool):
                return True
        if root.right:
            right_child_tree = dfs2(root.right, t2)
            if isinstance(right_child_tree, bool):
                return True
        r = [root.value] + left_child_tree + right_child_tree
        if r == taragt:
            return True
        return r
    return isinstance(dfs2(t1, t2), bool)



tree1 = build([1, 2, 3])
tree2 = build([2])
print(checkSubTree(tree1, tree2))

tree1 = build([1, None, 2, None, None, 4])
tree2 = build([3, 2])
print(checkSubTree(tree1, tree2))
