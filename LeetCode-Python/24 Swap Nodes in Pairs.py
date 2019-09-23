"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
    Given 1->2->3->4, you should return the list as 2->1->4->3.
"""



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        return

def printNodeList(node):
    string = ''
    while node:
        string += ' -> '+ str(node.val)
        node = node.next
    print(string)


def swapPairs(head):
    nodelist = list()
    while head:
        nodelist.append(head)
        head = head.next
    l = len(nodelist)

    if l == 1:
        return nodelist[0]

    index = 0
    newhead = None
    last_node = None
    while index < l:
        if l - index > 1:
            if newhead == None:
                newhead = nodelist[index + 1]
            else:
                last_node.next = nodelist[index + 1]
            nodelist[index].next = None
            nodelist[index + 1].next = nodelist[index]
            last_node = nodelist[index]
            index += 2
        else:
            if newhead == None:
                newhead = nodelist[index]
            else:
                last_node.next = nodelist[index]
            nodelist[index].next = None
            index += 1
    return newhead



head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

head.next = node2
node2.next = node3
#node3.next = node4

printNodeList(swapPairs(head))
