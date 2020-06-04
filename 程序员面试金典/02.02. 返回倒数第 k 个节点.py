"""
实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

注意：本题相对原题稍作改动

示例：
    输入： 1->2->3->4->5 和 k = 2
    输出： 4

说明：
    给定的 k 保证是有效的。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def NodeListBuilder(nums):
    if len(nums) == 0:
        return None
    else:
        head = ListNode(nums[0])
        last = head
        for i in range(1, len(nums)):
            new_node = ListNode(nums[i])
            last.next = new_node
            last = new_node
        return head


def NodeListPrinter(head):
    node_list = list()
    while head != None:
        node_list.append(str(head.val))
        head = head.next
    return ('->').join(node_list)

# 快慢指针
def kthToLast(head, k):
    pointer_1 = head
    pointer_2 = head
    while pointer_1!= None:
        pointer_1 = pointer_1.next
        if k == 0:
            pointer_2 = pointer_2.next
        else:
            k -= 1
    return pointer_2.val

nums = [1, 2, 3, 4, 5]
k = 2
head = NodeListBuilder(nums)
print(NodeListPrinter(head))
print(kthToLast(head, k))
