"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

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


"""
def removeNthFromEnd(head, n):
    nodelist = list()
    while head:
        nodelist.append(head.val)
        head = head.next

    l = len(nodelist)

    newlist = None
    newhead = None
    for i in range(0, l):
        if i != l - n:
            if newhead == None:
                newlist = ListNode(nodelist[i])
                newhead = newlist
            else:
                newNode = ListNode(nodelist[i])
                newlist.next = newNode
                newlist = newNode
    return newhead
"""

def removeNthFromEnd(head, n):
    nodelist = list()
    while head:
        nodelist.append(head)
        head = head.next

    l = len(nodelist)
    if n == 1:
        if l == 1:
            return None
        else:
            nodelist[-2].next = None
    elif n < l:
        nodelist[l-n-1].next = nodelist[l-n+1]
    else:
        return nodelist[1]

    return nodelist[0]


# NodeList 1
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)


head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

printNodeList(removeNthFromEnd(head, 2))
