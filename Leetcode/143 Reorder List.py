"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
    Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
    Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
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



def reorderList(head):
    nodelist = list()
    while head:
        nodelist.append(head)
        head = head.next

    l = len(nodelist)
    isodd = False
    if l%2 == 0:
        l = int(l/2)
    else:
        l = int(round(l / 2 - 0.5))
        isodd = True
    head = None
    last_node = None
    for i in range(0, l):
        if head != None:
            last_node.next = nodelist[i]
            nodelist[i].next = nodelist[-i-1]
            last_node = nodelist[-i-1]
            last_node.next = None
        else:
            head = nodelist[i]
            nodelist[i].next = nodelist[-i-1]
            last_node = nodelist[-i-1]
    if isodd:
        nodelist[l].next = None
        if head != None:
            last_node.next = nodelist[l]
        else:
            head = nodelist[l]

    return head

head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

head.next = node2
node2.next = node3
node3.next = node4

printNodeList(reorderList(head))
