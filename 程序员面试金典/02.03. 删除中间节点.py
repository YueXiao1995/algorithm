"""
实现一种算法，删除单向链表中间的某个节点（即不是第一个或最后一个节点），假定你只能访问该节点。

示例：
    输入：单向链表a->b->c->d->e->f中的节点c
    结果：不返回任何数据，但该链表变为a->b->d->e->f
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

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next


head = ListNode('a')
node2 = ListNode('b')
node3 = ListNode('c')
node4 = ListNode('d')
node5 = ListNode('e')

head.next = node2
node2.next = node3
node3.next = node4
node5.next = node5

print(NodeListPrinter(head))
deleteNode(node3)
print(NodeListPrinter(head))
