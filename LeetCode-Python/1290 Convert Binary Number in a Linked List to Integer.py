"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:
    Input: head = [1,0,1]
    Output: 5
    Explanation: (101) in base 2 = (5) in base 10

Example 2:
    Input: head = [0]
    Output: 0

Example 3:
    Input: head = [1]
    Output: 1

Example 4:
    Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
    Output: 18880

Example 5:
    Input: head = [0,0]
    Output: 0

Constraints:
    The Linked List is not empty.
    Number of nodes will not exceed 30.
    Each node's value is either 0 or 1.
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def createLinkedList(arr):
    head = None
    current = None
    for num in arr:
        new_node = ListNode(num)
        if head == None:
            head = new_node
            current = new_node
        else:
            current.next = new_node
            current = new_node
    return head


def getDecimalValue(head):
    num = 0
    while head:
        num = num * 2 + head.val
        head = head.next
    return num


head1 = [1,0,1]
head2 = [0]
head3 = [1]
head4 = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
head5 = [0,0]

print(getDecimalValue(createLinkedList(head5)))
