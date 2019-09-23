"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
    Input: 1->1->2
    Output: 1->2

Example 2:
    Input: 1->1->2->3->3
    Output: 1->2->3
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

# NodeList 1
head = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)


head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def deleteDuplicates(head):
    if head != None:
        nums = list()
        newhead = ListNode(head.val)
        temphead = newhead
        nums.append(head.val)
        i = 0
        while (head):
            if head.val not in nums and i > 0:
                nums.append(head.val)
                newNode = ListNode(head.val)
                temphead.next = newNode
                temphead = newNode

            head = head.next
            print(nums)
            i += 1
        return newhead
    else:
        return None



printNodeList(head)
printNodeList(deleteDuplicates(head))
