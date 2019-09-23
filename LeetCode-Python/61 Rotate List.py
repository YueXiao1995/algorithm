"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
    Input: 1->2->3->4->5->NULL, k = 2
    Output: 4->5->1->2->3->NULL
    Explanation:
    rotate 1 steps to the right: 5->1->2->3->4->NULL
    rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
    Input: 0->1->2->NULL, k = 4
    Output: 2->0->1->NULL
    Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        return

def printNodeList(node):
    string = ' -> '
    while node:
        string += str(node.val) + ' -> '
        node = node.next
    print(string)

def rotateRight(head, k):
    node_list = list()
    while head:
        node_list.append(head)
        head = head.next
    l = len(node_list)

    if l == 0:
        return None

    k = k % l
    newhead = node_list[0]
    if k != 0:
        last_node_index = l - k - 1
        node_list[last_node_index].next = None
        node_list[l-1].next = node_list[0]
        newhead = node_list[last_node_index + 1]
    return newhead

head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

printNodeList(rotateRight(head, 1))
