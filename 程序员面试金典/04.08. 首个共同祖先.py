"""
设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。

例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]

    3
   / \
  5   1
 / \ / \
6  2 0  8
  / \
 7   4

示例 1:
    输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    输出: 3
    解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2:
    输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    输出: 5
    解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

说明:
    所有节点的值都是唯一的。
    p、q 为不同节点且均存在于给定的二叉树中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-common-ancestor-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from binarytree import build
def lowestCommonAncestor(root, p, q):

    def dfs(root, p, q):
        # return = [is_ancestor_found, is_p_found, is_q_found, ancestor]
        r = [False, False, False, None]
        if root.value == p:
            r[1] = True
        elif root.value == q:
            r[2] = True
        if root.left:
            left_r = dfs(root.left, p, q)
            if left_r[0] == True:
                return left_r
            else:
                if left_r[1] == True:
                    r[1] = True
                if left_r[2] == True:
                    r[2] = True
        if root.right:
            right_r = dfs(root.right, p ,q)
            if right_r[0] == True:
                return right_r
            else:
                if right_r[1] == True:
                    r[1] = True
                if right_r[2] == True:
                    r[2] = True
        if r[1] == True and r[2] == True:
            return [True, True, True, root]
        else:
            return r
    return dfs(root, p, q)[3]



tree = build([3,5,1,6,2,0,8,None,None,7,4])
print(tree)
p = 5
q = 1
print(lowestCommonAncestor(tree, p, q))

tree = build([3,5,1,6,2,0,8,None,None,7,4])
print(tree)
p = 5
q = 4
print(lowestCommonAncestor(tree, p, q))
