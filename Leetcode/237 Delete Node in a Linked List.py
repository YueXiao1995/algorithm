"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Example 1:
    Input: head = [4,5,1,9], node = 5
    Output: [4,1,9]
    Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
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

def deleteNode(node):
    nextNode = node.next
    node.val = nextNode.val
    node.next = nextNode.next
    node = nextNode

deleteNode(head)
printNodeList(head)
