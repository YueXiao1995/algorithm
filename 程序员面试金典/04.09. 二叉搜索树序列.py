"""
从左向右遍历一个数组，通过不断将其中的元素插入树中可以逐步地生成一棵二叉搜索树。给定一个由不同节点组成的二叉树，输出所有可能生成此树的数组。

示例:
    给定如下二叉树

            2
           / \
          1   3
返回:
    [
       [2,1,3],
       [2,3,1]
    ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bst-sequences-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from binarytree import build, Node

def buildTree(root, nums1, nums2):
    if len(nums1) > 0:
        left_node = Node(nums1[0])
        root.left = left_node
    if len(nums2) > 0:
        right_node = Node(nums2[0])
        root.right = right_node
    sequences = []
    if root.left:
        sequences.extend(buildTree(root.left, nums1[1:], nums2))
    if root.right:
        sequences.extend(buildTree(root.right, nums1, nums2[1:]))

    if len(sequences) == 0:
        return [[root.value]]
    else:
        for s in sequences:
            s.insert(0, root.value)
        return sequences

def BSTSequences(root):
    if root == None:
        return [[]]
    if not root.left and not root.right:
        return [[root.value]]
    if root.left and root.right:
        r = []
        left_r = BSTSequences(root.left)
        right_r = BSTSequences(root.right)

        for left_sequence in left_r:
            for right_sequence in right_r:
                r.extend(buildTree(Node(root.value), left_sequence, right_sequence))
        return r
    if root.left:
        left_r = BSTSequences(root.left)
        for sequence in left_r:
            sequence.insert(0, root.value)
        return left_r
    if root.right:
        right_r = BSTSequences(root.right)
        for sequence in right_r:
            sequence.insert(0, root.value)
        return right_r
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

tree = build([2, 1, 3])
print(tree)
print(BSTSequences(tree))

tree = build([1, 2])
print(tree)
print(BSTSequences(tree))

tree = None
print(BSTSequences(tree))

tree = build([5,2,None,1,4,None,None,None, None, 3])
print(tree)
print(BSTSequences(tree))


nums1 = [1, 2]
nums2 = [3, 4]
root = Node(0)
print(buildTree(root, nums1, nums2))
print(root)
