"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
    Input: 1->2->3->4->5->NULL, m = 2, n = 4
    Output: 1->4->3->2->5->NULL
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

def reverseBetween(head, m, n):
    node_list = list()
    while head:
        node_list.append(head)
        head = head.next
    l = len(node_list)
    newhead = node_list[0]

    if m == 1:
        last_node = None
    else:
        last_node = node_list[m - 2]

    if n == l:
        next_node = None
    else:
        next_node = node_list[n]

    for i in reversed(range(m - 1, n)):
        if last_node != None:
            last_node.next = node_list[i]
        else:
            newhead = node_list[i]
        last_node = node_list[i]
    last_node.next = next_node
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


printNodeList(reverseBetween(head, 4, 5))
