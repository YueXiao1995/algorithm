"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        return

def addTwoNumbers(l1, l2):
    num = 0
    i = 1
    while (l1):
        num += i * l1.val
        i = i * 10
        l1 = l1.next

    i = 1
    while (l2):
        num += i * l2.val
        i *= 10
        l2 = l2.next

    num = list(map(int, str(num)))

    head = ListNode(num[-1])
    node = head
    for i in reversed(range(len(num) - 1)):
        newNode = ListNode(num[i])
        node.next = newNode
        node = newNode
    return head

def printNodeList(node):
    while node:
        print(node.val)
        node = node.next

# NodeList 1
node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

# NodeList 2
node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)

node4.next = node5
node5.next = node6



printNodeList(addTwoNumbers(node1, node4))
