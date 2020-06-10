"""
给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。

示例:
给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

          0
         / \
       -3   9
       /   /
     -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-height-tree-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

from binarytree import Node, build

def sortedArrayToBST(nums):
    def buildTree(nums):
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            node = Node(nums[0])
            return node
        else:
            mid = len(nums) // 2
            node = Node(nums[mid])
            node.left = buildTree(nums[:mid])
            node.right = buildTree(nums[mid+1:])
            return node
    return buildTree(nums)

nums = [0,-3,9,-10, 5]
print(print(sortedArrayToBST(nums)))
