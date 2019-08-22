"""
Reverse a singly linked list.

Example:
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        return

def printNodeList(node):
    while node:
        print(node.val)
        node = node.next

head= ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def reverseList(head):
    if head:
        nodeList = list()
        len = 0
        while(head):
            nodeList.append(head)
            head = head.next
            len += 1
        newHead = nodeList[-1]
        temHead = newHead
        for i in reversed(range(0, len-1)):
            temHead.next = nodeList[i]
            temHead = nodeList[i]
        temHead.next = None
        return newHead
    else:
        return None
printNodeList(reverseList(head))
