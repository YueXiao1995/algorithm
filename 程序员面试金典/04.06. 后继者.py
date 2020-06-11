"""
设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。

如果指定节点没有对应的“下一个”节点，则返回null。

示例 1:
    输入: root = [2,1,3], p = 1

      2
     / \
    1   3

    输出: 2

示例 2:
    输入: root = [5,3,6,2,4,null,null,1], p = 6

          5
         / \
        3   6
       / \
      2   4
     /
    1

    输出: null

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/successor-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from binarytree import build

def inorderSuccessor(root, p):
    is_p_found = False
    tree_node = None
    def dfs(root, p):
        nonlocal is_p_found

        if root.left:
            dfs(root.left, p)

        nonlocal tree_node
        if is_p_found and tree_node is None:
            tree_node = root
        else:
            if root.value == p:
                is_p_found = True

        if root.right:
            dfs(root.right, p)

    dfs(root, p)
    return tree_node


tree = build([2, 1, 3])
p = 1
print(tree)
print(inorderSuccessor(tree, p))

tree = build([5, 3, 6, 2, 4, None, None, 1])
p = 6
print(tree)
print(inorderSuccessor(tree, p))


tree = build([6,2,8,0,4,7,9,None,None,3,5])
p = 2
print(tree)
print(inorderSuccessor(tree, p))
