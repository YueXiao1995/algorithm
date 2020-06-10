"""
给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。

示例：
    输入：[1,2,3,4,5,null,7,8]

            1
           /  \
          2    3
         / \    \
        4   5    7
       /
      8

    输出：[[1],[2,3],[4,5,7],[8]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/list-of-depth-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from binarytree import build

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


def listOfDepth(tree):
    current_list = [tree]

    next_list = []
    result = []
    root_node = ListNode(tree.value)
    result.append(root_node)
    next_node_list = None
    pointer = None

    while len(current_list) != 0:
        for i in range(len(current_list)):

            if current_list[i].left:
                next_list.append(current_list[i].left)
                node = ListNode(current_list[i].left.value)
                if pointer == None:
                    next_node_list = node
                    pointer = next_node_list
                else:
                    pointer.next = node
                    pointer = pointer.next

            if current_list[i].right:
                next_list.append(current_list[i].right)
                node = ListNode(current_list[i].right.value)
                if pointer == None:
                    next_node_list = node
                    pointer = next_node_list
                else:
                    pointer.next = node
                    pointer = pointer.next

            if i == len(current_list) - 1:
                if len(next_list) != 0:
                    result.append(next_node_list)
                current_list = next_list
                next_list = []
                pointer = None
                next_node_list = None
    return result


nums = [1, 2, 3, 4, 5, None, 7, 8]
root = build(nums)
print(root)

for head in listOfDepth(root):
    nums = []
    while head != None:
        nums.append(str(head.val))
        head = head.next
    print(('->').join(nums))

