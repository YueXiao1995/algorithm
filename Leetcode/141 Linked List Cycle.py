"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the
linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where tail connects to the second node.
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
head = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(4)


head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

def hasCycle(head):
    map = list()
    hasCycle = False
    while (head):
        if head not in map:
            map.append(head)
            head = head.next
            #print(map)
        else:
            hasCycle = True
            break
    return hasCycle

print(hasCycle(head))
