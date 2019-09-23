"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

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

head = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(1)
node4 = ListNode(3)

head.next = node2
node2.next = node3
node3.next = node4

def middleNode(head):
    nodelist = list()
    len = 0
    while(head):
        nodelist.append(head)
        head = head.next
        len += 1

    if len%2 ==0:
        len = int(len/2)
    else:
        len = int(round(len/2))

    return nodelist[len]

printNodeList(middleNode(head))

