"""
Remove all elements from a linked list of integers that have value val.

Example:
    Input:  1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5
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
node3 = ListNode(6)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(5)
node7 = ListNode(6)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7


def removeElements(head, val):
    newHead = None
    temHead = None
    while(head):
        if head.val != val:
            if newHead == None:
                newHead = ListNode(head.val)
                temHead = newHead
            else:
                newNode = ListNode(head.val)
                temHead.next = newNode
                temHead = newNode
        head = head.next
    return  newHead

printNodeList(removeElements(head, 6))




