"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        return

def mergeTwoLists(l1, l2):
    nums = list()
    while (l1):
        nums.append(l1.val)
        l1 = l1.next

    while (l2):
        nums.append(l2.val)
        l2 = l2.next
    nums.sort()
    if len(nums)>0:
        head = ListNode(nums[0])
        node = head
        for i in range(1, len(nums)):
            newNode = ListNode(nums[i])
            node.next = newNode
            node = newNode
        return head
    else:
        return None

def printNodeList(node):
    while node:
        print(node.val)
        node = node.next

# NodeList 1
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

node1.next = node2
node2.next = node3

# NodeList 2
node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)

node4.next = node5
node5.next = node6

printNodeList(mergeTwoLists(node1, node4))




