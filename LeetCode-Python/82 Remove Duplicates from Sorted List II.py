"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:
    Input: 1->2->3->3->4->4->5
    Output: 1->2->5

Example 2:
    Input: 1->1->1->2->3
    Output: 2->3
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

def deleteDuplicates(head):
    newList = None
    newhead = None
    last_node = None
    last_val = None
    while head:
        if head.val == last_val:
            last_node = None
        else:
            if last_node != None:
                if newhead == None:
                    newList = last_node
                    newhead = newList
                else:
                    newList.next = last_node
                    newList = last_node
            last_val = head.val
            last_node = ListNode(last_val)
        head = head.next
    if last_node != None:
        if newhead != None:
            newList.next = last_node
        else:
            newhead = last_node
    return newhead

head1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(4)

head1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

printNodeList(deleteDuplicates(head1))
